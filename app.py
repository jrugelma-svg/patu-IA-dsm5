import streamlit as st
from google import genai

# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Asistente DSM-5",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Evaluador de Similitud Criterios DSM-5")
st.write("Analiza el nivel de concordancia y similitud de un caso clínico con los trastornos del manual.")

# ==========================================
# 2. CONEXIÓN REAL CON GOOGLE GEMINI
# ==========================================
# Tu clave API ya está colocada correctamente aquí adentro entre las comillas:
API_KEY = "AQ.Ab8RN6LVcdf6oUMMsXSLF8x8o_-S0MpL_2Cxr9YTwsXpws1dng"

def evaluar_similitud_dsm5(texto_caso):
    try:
        # Inicializamos el cliente forzando la API v1 estable para evitar el error 404
        client = genai.Client(api_key=API_KEY, http_options={'api_version': 'v1'})
        
        prompt_clinico = f"""
        Actúa como un psicólogo clínico experto y un algoritmo de cribado psicopatológico.
        Analiza el siguiente motivo de consulta y calcula numéricamente el porcentaje de similitud o concordancia con los trastornos del DSM-5 que tengan más coincidencia.
        
        Caso clínico a evaluar:
        "{texto_caso}"
        
        Tu respuesta debe ser exclusivamente una tabla en formato Markdown con las siguientes columnas:
        | Trastorno Sospechado (DSM-5) | % Similitud | Criterios Clave Coincidentes | Justificación Breve |
        
        Reglas estrictas:
        - Ordena la tabla de mayor a menor porcentaje de similitud.
        - Incluye de 2 a 4 trastornos diferenciales que muestren alguna similitud o con los que se pueda confundir.
        - No agregues introducciones, saludos, notas aclaratorias ni textos largos debajo de la tabla. Sé directo, puramente estadístico y cuantitativo.
        """
        
        # Usamos el modelo ultra-estable de amplio soporte
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt_clinico,
        )
        return response.text
        
    except Exception as e:
        return f"❌ Error en el motor de análisis: {str(e)}"

# ==========================================
# 3. INTERFAZ GRÁFICA (TABS)
# ==========================================
tabs = st.tabs(["Análisis de Caso", "Historial", "Configuración"])

with tabs[0]:
    st.header("📝 Matriz de Concordancia Clínica")
    st.write("Introduce el motivo de consulta para evaluar estadísticamente los trastornos con mayor índice de similitud.")
    
    caso_clinico = st.text_area(
        label="Descripción formal del caso / Notas de la Entrevista Clínica:",
        placeholder="Pega aquí el caso clínico para calcular sus similitudes...",
        height=200
    )
    
    if st.button("📊 Calcular Similitud Diagnóstica"):
        if caso_clinico.strip() == "":
            st.warning("Por favor, ingresa un texto para realizar la evaluación.")
        else:
            with st.spinner("Calculando índices de similitud con el DSM-5..."):
                tabla_resultados = evaluar_similitud_dsm5(caso_clinico)
                st.success("¡Cálculo de similitud finalizado!")
                st.markdown(tabla_resultados)

with tabs[1]:
    st.header("⏳ Historial de Evaluaciones")
    st.info("Aquí se mostrarán los casos clínicos analizados previamente en esta sesión.")

with tabs[2]:
    st.header("⚙️ Configuración del Sistema")
    st.write("Ajustes del motor de evaluación y parámetros del modelo.")
