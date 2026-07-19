# database.py
import sqlite3
import os

def inicializar_patu_db():
    """
    Crea la base de datos relacional y migra de forma automática todos los 
    trastornos clínicos oficiales desde los módulos de producción.
    """
    db_path = "patu_db.db"
    
    # Forzamos una inicialización limpia si hay problemas en la nube
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Crear la tabla maestra con la estructura que requiere el motor analítico
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trastornos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            cie10 TEXT,
            descripcion_criterios TEXT,
            guia_diferencial TEXT
        )
    """)
    
    # Limpiamos registros viejos para evitar duplicados o IDs cruzados
    cursor.execute("DELETE FROM trastornos")
    
    # Importaciones seguras de los tres bloques masivos de datos
    try:
        from data.neuro_personalidad import TRASTORNOS_NEURO_PERSONALIDAD
    except ImportError:
        TRASTORNOS_NEURO_PERSONALIDAD = []
        
    try:
        from data.afectivos_ansiedad import TRASTORNOS_AFEC_ANSI
    except ImportError:
        TRASTORNOS_AFEC_ANSI = []
        
    try:
        from data.psicoticos_alimentarios import TRASTORNOS_PSIC_ALIM
    except ImportError:
        TRASTORNOS_PSIC_ALIM = []
        
    # Unificamos toda la carga clínica para la migración relacional
    pool_completo = TRASTORNOS_NEURO_PERSONALIDAD + TRASTORNOS_AFEC_ANSI + TRASTORNOS_PSIC_ALIM
    
    for t in pool_completo:
        t_id = t.get("id")
        nombre = t.get("nombre")
        categoria = t.get("categoria")
        cie10 = t.get("cie10", "N/A")
        guia = t.get("guia_diferencial", "No disponible.")
        
        # El motor analítico de engine.py lee texto plano en la BD.
        # Convertimos la lista de tuplas a texto plano estructurado con separadores estables.
        criterios_lista = t.get("criterios", [])
        criterios_texto = " ".join([f"{cod}: {txt}." for cod, txt in criterios_lista])
        
        cursor.execute("""
            INSERT INTO trastornos (id, nombre, categoria, cie10, descripcion_criterios, guia_diferencial)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (t_id, nombre, categoria, cie10, criterios_texto, guia))
        
    conn.commit()
    conn.close()
    print(f" Migración exitosa: {len(pool_completo)} trastornos inyectados en patu_db.db.")

if __name__ == "__main__":
    inicializar_patu_db()
