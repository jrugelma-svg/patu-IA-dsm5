import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA Y TÍTULO
# ==========================================
st.set_page_config(
    page_title="Asistente DSM-5",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Evaluador de Criterios Clínicos DSM-5")
st.write("Herramienta de soporte y análisis de sintomatología basada en inteligencia artificial.")

# ==========================================
# 2. FUNCIÓN DE ANÁLISIS (MOCK / SIMULACIÓN)
# ==========================================
# Nota: Modifica o vincula esta función con tu backend real de IA
def analizar_caso_patu(texto_caso):
    # Aquí iría la lógica de tu LLM o API
    return "Análisis completado exitosamente con el modelo de IA."

# ==========================================
# 3. INTERFAZ GRÁFICA Y PESTAÑAS (TABS)
# ==========================================
tabs = st.tabs(["Análisis de Caso", "Historial", "Configuración"])

with tabs[0]:
    st.header("📝 Análisis de Caso Clínico")
    st.write("Ingresa el reporte de la entrevista clínica, anamnesis o motivo de consulta detallado para evaluar su concordancia con los criterios del DSM-5.")
    
    # Bloque del área de texto perfectamente tabulado
    caso_clinico = st.text_area(
        label="Descripción formal del caso / Notas de la Entrevista Clínica:",
        placeholder=(
            "Ejemplo de uso profesional:\n"
            "Paciente masculino de 24 años refiere un estado de ánimo deprimido la mayor parte del día, "
            "manifestado por llanto frecuente reportado por familiares. Presenta una marcada disminución "
            "del interés o placer por casi todas las actividades habituales (anhedonia) que ha persistido "
            "durante las últimas 3 semanas, acompañado de insomnio de conciliación, fatiga diaria y dificultades "
            "para concentrarse en sus actividades laborales..."
        ),
        height=200
    )
    
    # Bloque de ejecución del botón perfectamente alineado
    if st.button("🚀 Evaluar Sintomatología"):
        if caso_clinico.strip() == "":
            st.warning("Por favor, ingresa una descripción válida para realizar el análisis.")
        else:
            with st.spinner("Analizando concordancias con los criterios oficiales del DSM-5..."):
                resultados = analizar_caso_patu(caso_clinico)
                st.success("¡Análisis finalizado!")
                st.write(resultados)

with tabs[1]:
    st.header("⏳ Historial de Evaluaciones")
    st.info("Aquí se mostrarán los casos clínicos analizados previamente en esta sesión.")

with tabs[2]:
    st.header("⚙️ Configuración del Sistema")
    st.write("Ajustes del motor de evaluación y parámetros del modelo.")
