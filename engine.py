# engine.py
import re
import sqlite3
import math

# =====================================================================
# 1. DICCIONARIO MASIVO DE EXPANSIÓN SEMÁNTICA (Mapeo Coloquial a DSM-5)
# =====================================================================
# Traduce el lenguaje cotidiano, metáforas y errores comunes a términos del DSM-5.
DICCIONARIO_SINTOMAS = {
    # --- ESTADO DE ÁNIMO / AFECTO / DEPRESIÓN ---
    "triste": ["deprimido", "tristeza", "llanto", "vacio", "desesperanza", "infeliz", "decaido", "desanimado", "melancolia", "nostalgia", "pena", "desgana"],
    "llora": ["llanto", "tristeza", "deprimido", "sensible", "decaido", "lagrimas", "quebrantado"],
    "gana": ["anhedonia", "apatia", "desinteres", "aburrido", "placer", "motivacion", "desgano", "flojera", "aburrimiento"],
    "placer": ["anhedonia", "desinteres", "apatico", "placer", "disfrutar", "gozar", "entusiasmo"],
    "culpable": ["culpa", "inutilidad", "autoreproche", "malo", "error", "remordimiento", "responsable", "fracaso"],
    "morir": ["suicida", "muerte", "suicidio", "matarse", "autolesion", "hacerse daño", "morirme", "desaparecer", "dejar de existir", "ahorcar", "pastillas"],
    "bipolar": ["mania", "euforia", "maniaco", "irritable", "grandiosidad", "exaltado", "ciclotimia", "cambios de humor"],
    "feliz": ["euforia", "mania", "exaltado", "elevado", "grandiosidad", "acelerado", "dios", "invencible", "subidon"],
    "inutil": ["inutilidad", "culpa", "incompetente", "estorbo", "inservible", "desvalorizacion"],
    "desesperanzado": ["desesperanza", "sin futuro", "pesimismo", "negativo", "oscuro", "sin salida"],
    
    # --- ANSIEDAD / MIEDOS / ESTRÉS / PÁNICO ---
    "miedo": ["ansiedad", "temor", "panico", "fobia", "asustado", "pavor", "terror", "horror", "cagado", "panico", "alarma"],
    "nervioso": ["ansiedad", "nerviosismo", "tension", "preocupacion", "inquietud", "alterado", "acelerado", "hipervigilancia"],
    "preocupado": ["preocupacion", "ansiedad", "angustia", "rumiacion", "pensadera", "comerse la cabeza", "obsesion", "intranquilo"],
    "panico": ["panico", "terror", "angustia", "ahogo", "palpitaciones", "taquicardia", "morirme", "loco", "desesperacion"],
    "tiembla": ["temblor", "agitacion", "tension", "sudoracion", "temblores", "tiritar", "sacudidas"],
    "suda": ["sudoracion", "hiperhidrosis", "calor", "transpiracion", "sudor", "mojado"],
    "ahogo": ["disnea", "asfixia", "ahogarse", "falta de aire", "opresion en el pecho", "nudo en la garganta"],
    "corazon": ["taquicardia", "palpitaciones", "latidos", "acelerado", "pecho", "punzadas"],
    "tenso": ["tension", "muscular", "rigidez", "agarrotado", "cuello", "espalda", "dolor"],
    "peligro": ["hipervigilancia", "alerta", "amenaza", "inseguro", "perseguido", "miedo"],
    "social": ["fobia social", "timidez", "verguenza", "exponer", "hablar en publico", "miradas", "juzgado", "evaluado"],
    "obsesion": ["obsesivo", "compulsivo", "ideas fijas", "manias", "rituales", "repetir", "limpieza", "orden", "duda"],
    "trauma": ["estres postraumatico", "recuerdo", "flashback", "pesadilla", "accidente", "abuso", "asalto", "evitacion"],

    # --- SUEÑO / ENERGÍA / FATIGA ---
    "dormir": ["insomnio", "sueño", "hipersomnia", "pesadillas", "desvelado", "despertar", "no duermo", "desvelo", "nocturno"],
    "insomnio": ["insomnio", "desvelo", "no duerme", "despertarse", "madrugada", "sin sueño"],
    "cansado": ["fatiga", "energia", "agotado", "debilidad", "cansancio", "sin fuerzas", "desgastado", "molido", "sin ganas"],
    "energia": ["fatiga", "energia", "hiperactividad", "activo", "agotamiento", "pila", "fuerza"],

    # --- ALIMENTACIÓN / PESO / IMAGEN CORPORAL ---
    "comer": ["apetito", "alimentacion", "atracones", "ayuno", "restriccion", "bulimia", "anorexia", "tragar", "hambre", "ansiedad por comer"],
    "gordo": ["peso", "imagen", "silueta", "engordar", "obesidad", "dismorfia", "lleno", "grasa", "cuerpo"],
    "flaco": ["peso", "delgadez", "perder peso", "bajar peso", "adelgazar", "kilos"],
    "vomito": ["vomitar", "purga", "laxantes", "bulimia", "devolver", "inducido"],

    # --- COGNICIÓN / ATENCIÓN / MEMORIA ---
    "olvida": ["memoria", "olvidadizo", "amnesia", "demencia", "deterioro cognitivo", "lagunas", "despiste"],
    "concentro": ["concentracion", "atencion", "distraccion", "enfocarse", "desatento", "distraido", "en las nubes", "pajaron"],
    "decidir": ["indecision", "duda", "decisiones", "inseguridad", "bloqueo"],

    # --- SÍNTOMAS PSICÓTICOS / PERCEPCIÓN ---
    "voces": ["alucinacion", "delirio", "escucha", "psicotico", "percepcion", "hablan", "ruidos", "susurros"],
    "persiguen": ["delirio", "paranoia", "persecucion", "camaras", "espian", "daño", "conspiracion", "trama", "observado"],
    "raro": ["delirio", "despersonalizacion", "desrealizacion", "extraño", "sueño", "irreal"],
    "mente": ["control", "pensamiento", "telepatia", "roban", "insertan", "transmiten"],

    # --- IMPULSIVIDAD / CONDUCTA / PERSONALIDAD ---
    "ira": ["irritable", "enojo", "furia", "agresividad", "rabia", "peleas", "discusiones", "violencia", "humor"],
    "impulso": ["impulsividad", "compras", "apuestas", "velocidad", "riesgo", "frenesi", "autocontrol"],
    "amigos": ["relaciones", "aislamiento", "soledad", "evitacion", "social", "confianza", "abandono", "rechazo"],
    "personalidad": ["identidad", "vacio", "inestabilidad", "cambiante", "borde", "limite"],
    
    # --- INFANTIL / DESARROLLO / APRENDIZAJE ---
    "niño": ["desarrollo", "infantil", "escuela", "hiperactivo", "rabietas", "berrinches", "juguetes"],
    "hablar": ["lenguaje", "comunicacion", "mudez", "tartamudeo", "fluidez", "expresion"],
    "quieto": ["hiperactividad", "inquietud", "impulsivo", "saltando", "moverse", "inquieto"]
}

# =====================================================================
# 2. FUNCIONES DE PROCESAMIENTO LINGÜÍSTICO Y LIMPIEZA
# =====================================================================
def normalizar_texto(texto):
    """
    Limpia agresivamente el texto del usuario: elimina tildes, puntuación,
    convierte a minúsculas y remueve espacios innecesarios.
    """
    if not texto:
        return ""
    texto = texto.lower()
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ü": "u", "ñ": "ñ", "ç": "c"
    }
    for orig, rep in reemplazos.items():
        texto = texto.replace(orig, rep)
    
    texto = re.sub(r'[^\w\sñ]', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def extraer_raices(palabra):
    """
    Aplica una lematización/stemming manual simple truncando sufijos plurales 
    y derivaciones verbales comunes para maximizar coincidencia léxica.
    """
    if len(palabra) <= 4:
        return palabra
    
    sufijos = ["es", "s", "mente", "ado", "ada", "ido", "ida", "ando", "iendo", "ar", "er", "ir"]
    for sufijo in sufijos:
        if palabra.endswith(sufijo):
            return palabra[:-len(sufijo)]
    return palabra

# =====================================================================
# 3. LISTA DE PALABRAS VACÍAS (STOP WORDS)
# =====================================================================
STOP_WORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "a", "ante", 
    "bajo", "cabe", "con", "contra", "desde", "en", "entre", "hacia", "hasta", "para", 
    "por", "segun", "sin", "so", "sobre", "tras", "y", "o", "u", "pero", "mas", "e", 
    "que", "porque", "como", "cuando", "donde", "quien", "cual", "cuyo", "mi", "mis", 
    "tu", "tus", "su", "sus", "nuestro", "nuestra", "me", "te", "se", "nos", "lo", "le", 
    "les", "yo", "tu", "el", "ella", "ellos", "ellas", "nosotros", "este", "esta", "estos", 
    "estas", "ese", "esa", "esos", "esas", "aquel", "aquella", "muy", "mucho", "poco", 
    "bastante", "tan", "asi", "siento", "tengo", "paciente", "persona", "sintoma", "sintomas",
    "doctor", "psicologo", "creo", "parece", "presenta", "sufre", "padece", "tiene"
}

# =====================================================================
# 4. MOTOR DE ANALÍTICA Y CÁLCULO DE RELEVANCIA (SCORING)
# =====================================================================
def analizar_caso_patu(descripcion_caso):
    """
    Analiza clínicamente la descripción del caso ingresado por el usuario.
    """
    if not descripcion_caso:
        return []

    texto_limpio = normalizar_texto(descripcion_caso)
    palabras_usuario = texto_limpio.split()

    tokens_base = []
    for pal in palabras_usuario:
        if pal not in STOP_WORDS:
            tokens_base.append(extraer_raices(pal))

    tokens_expandidos = set(tokens_base)
    for pal in palabras_usuario:
        if pal in DICCIONARIO_SINTOMAS:
            for sinonimo in DICCIONARIO_SINTOMAS[pal]:
                tokens_expandidos.add(normalizar_texto(sinonimo))
                tokens_expandidos.add(extraer_raices(normalizar_texto(sinonimo)))

    conn = sqlite3.connect("patu_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, categoria, descripcion_criterios FROM trastornos")
    trastornos = cursor.fetchall()

    resultados = []

    for t_id, nombre, categoria, criterios in trastornos:
        if not criterios:
            continue
        
        lista_criterios = [normalizar_texto(c) for c in re.split(r'[.;•\-]', criterios) if len(c.strip()) > 5]
        
        coincidencias_totales = 0
        criterios_activados = 0
        
        for criterio in lista_criterios:
            criterio_tokens = criterio.split()
            criterio_raices = [extraer_raices(t) for t in criterio_tokens if t not in STOP_WORDS]
            
            hits_en_criterio = 0
            for token in tokens_expandidos:
                if token in criterio_tokens or token in criterio_raices or any(token in raiz for raiz in criterio_raices):
                    hits_en_criterio += 1
            
            if hits_en_criterio > 0:
                criterios_activados += 1
                coincidencias_totales += hits_en_criterio

        if criterios_activados == 0 or len(lista_criterios) == 0:
            continue
            
        factor_cobertura = criterios_activados / len(lista_criterios)
        factor_frecuencia = math.log1p(coincidencias_totales)
        
        score_bruto = (factor_cobertura * 60) + (factor_frecuencia * 40)
        porcentaje_coincidencia = min(98.5, round(score_bruto, 2))

        if porcentaje_coincidencia >= 15.0:
            resultados.append({
                "id": t_id,
                "nombre": nombre,
                "categoria": categoria,
                "coincidencia": porcentaje_coincidencia,
                "criterios_match": f"{criterios_activados} de {len(lista_criterios)}"
            })

    conn.close()
    return sorted(resultados, key=lambda x: x["coincidencia"], reverse=True)


def consultar_guia_trastorno(trastorno_id):
    """
    Recupera la ficha técnica y los criterios clínicos completos del DSM-5.
    """
    conn = sqlite3.connect("patu_db.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, categoria, descripcion_criterios, guia_diferencial 
        FROM trastornos WHERE id = ?
    """, (trastorno_id,))
    fila = cursor.fetchone()
    conn.close()

    if fila:
        return {
            "nombre": fila[0],
            "categoria": fila[1],
            "criterios": fila[2],
            "diferencial": fila[3] if fila[3] else "No se dispone de guía diferencial específica en la base de datos."
        }
    return None
