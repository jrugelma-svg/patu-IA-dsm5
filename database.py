# database.py
import sqlite3
import os

# Importamos las listas modulares de la carpeta data
try:
    from data.afectivos_ansiedad import TRASTORNOS_AFECTIVOS_ANSIEDAD
    from data.neuro_personalidad import TRASTORNOS_NEURO_PERSONALIDAD
    from data.psicoticos_alimentarios import TRASTORNOS_PSICOTICOS_ALIMENTARIOS
except ModuleNotFoundError:
    TRASTORNOS_AFECTIVOS_ANSIEDAD = []
    TRASTORNOS_NEURO_PERSONALIDAD = []
    TRASTORNOS_PSICOTICOS_ALIMENTARIOS = []

# En la nube es mejor usar una ruta relativa directa
DB_NAME = "patu_dsm5.db"

def inicializar_patu_db():
    # Evitamos reescribir la DB en la nube si ya está creada y tiene datos
    if os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM trastornos;")
            count = cursor.fetchone()[0]
            if count > 0:
                conn.close()
                print("🦆 Patu Database: La base de datos ya existe en la nube con datos válidos.")
                return
        except:
            pass
        conn.close()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Estructura relacional SQL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trastornos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        cie10 TEXT NOT NULL,
        categoria TEXT NOT NULL,
        guia_diferencial TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS criterios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trastorno_id INTEGER,
        codigo_criterio TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        FOREIGN KEY (trastorno_id) REFERENCES trastornos(id) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("DELETE FROM criterios;")
    cursor.execute("DELETE FROM trastornos;")
    
    compendio_completo_dsm5 = (
        TRASTORNOS_AFECTIVOS_ANSIEDAD + 
        TRASTORNOS_NEURO_PERSONALIDAD + 
        TRASTORNOS_PSICOTICOS_ALIMENTARIOS
    )
    
    for t in compendio_completo_dsm5:
        cursor.execute("""
        INSERT INTO trastornos (id, nombre, cie10, categoria, guia_diferencial)
        VALUES (?, ?, ?, ?, ?);
        """, (t["id"], t["nombre"], t["cie10"], t["categoria"], t["guia_diferencial"]))
        
        for codigo, desc in t["criterios"]:
            cursor.execute("""
            INSERT INTO criterios (trastorno_id, codigo_criterio, descripcion)
            VALUES (?, ?, ?);
            """, (t["id"], codigo, desc))
            
    conn.commit()
    conn.close()
    print("🦆 Patu Database: ¡Base de datos desplegada con éxito!")

if __name__ == "__main__":
    inicializar_patu_db()
