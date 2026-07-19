# engine.py
import sqlite3

DB_NAME = "patu_dsm5.db"

def consultar_guia_trastorno(id_trastorno):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, cie10, categoria, guia_diferencial FROM trastornos WHERE id = ?;", (id_trastorno,))
    trastorno = cursor.fetchone()
    cursor.execute("SELECT codigo_criterio, descripcion FROM criterios WHERE trastorno_id = ?;", (id_trastorno,))
    criterios = cursor.fetchall()
    conn.close()
    return trastorno, criterios

def analizar_caso_patu(texto_caso):
    if not texto_caso:
        return []

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, cie10, categoria, guia_diferencial FROM trastornos;")
    trastornos = cursor.fetchall()
    
    resultados = []
    texto_caso_minusculas = texto_caso.lower()
    
    PALABRAS_PROHIBIDAS = [
        "todos", "sobre", "entre", "cuando", "partes", "tiene", "lugar", "presencia", 
        "como", "para", "cada", "unos", "unas", "hacia", "desde", "pero", "este", "esta",
        "uno", "más", "campos", "debajo", "antes", "inicio", "frecuencia", "falla", "sino"
    ]
    
    for t_id, nombre, cie10, cat, guia in trastornos:
        cursor.execute("SELECT codigo_criterio, descripcion FROM criterios WHERE trastorno_id = ?;", (t_id,))
        criterios = cursor.fetchall()
        
        cumplidos = []
        faltantes = []
        
        for codigo, desc in criterios:
            palabras_clave = [p.strip(",.()") for p in desc.lower().split() if len(p) > 4]
            palabras_clave = [p for p in palabras_clave if p not in PALABRAS_PROHIBIDAS]
            
            coincidencias = sum(1 for p in palabras_clave if p in texto_caso_minusculas)
            
            if coincidencias >= 2 or codigo.lower() in texto_caso_minusculas:
                cumplidos.append(f"[{codigo}] {desc}")
            else:
                faltantes.append(f"[{codigo}] {desc}")
        
        total_criterios = len(criterios)
        tasa = int((len(cumplidos) / total_criterios) * 100) if total_criterios > 0 else 0
        
        if tasa >= 25:
            resultados.append({
                "nombre": nombre,
                "cie10": cie10,
                "categoria": cat,
                "guia": guia,
                "cumplidos": cumplidos,
                "faltantes": faltantes,
                "compatibilidad": tasa
            })
            
    conn.close()
    return sorted(resultados, key=lambda x: x["compatibilidad"], reverse=True)
