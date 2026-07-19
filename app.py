# app.py
import streamlit as pd  # Usado normalmente por compatibilidad de alias si la UI lo requiere
import streamlit as st
from database import inicializar_patu_db
from engine import analizar_caso_patu, consultar_guia_trastorno

# =====================================================================
# 1. AUTO-INICIALIZACIÓN AUTOMÁTICA AL ARRANCAR LA WEB
# =====================================================================
# Ejecuta la migración de datos al vuelo para asegurar sincronización 100%
try:
    inicializar_patu_db()
except Exception as e:
    st.sidebar.error(f"Aviso de inicialización: {e}")

# Configuración de diseño de la interfaz de Streamlit
st.set_page_config(
    page_title="Patu AI - Consultor Clínico DSM-5",
    page_icon="🦆",
    layout="wide"
)

# Título y encabezado principal
st.title("🦆 Patu AI: Asistente Clínico de Diagnóstico DSM-5")
st.caption("Arquitectura Inteligente Automática • Versión de Producción 2026")
st.markdown("---")

# =====================================================================
# 2. ENRUTAMIENTO DE PANELES (Módulos Gratuitos y Premium)
# =====================================================================
tabs = st.tabs(["🟢 MODO GRATUITO (Aprende y Diagnóstica)", "👑 MODO PREMIUM (Análisis Avanzado Clínico)"])

# ---------------------------------------------------------------------
# PANEL 1: MODO GRATUITO (Motor de Scoring Avanzado)
# ---------------------------------------------------------------------
with tabs[0]:
    st.header("📝 Análisis de Caso Clínico")
  st.write("Ingresa el reporte de la entrevista clínica, anamnesis o motivo de consulta detallado para evaluar su concordancia con los criterios del DSM-5.")
    
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
    if st.button("🚀 Evaluar Sintomatología"):
        if caso_clinico.strip() == "":
            st.warning("Por favor, ingresa una descripción válida para realizar el análisis.")
        else:
            with st.spinner("Analizando concordancias con los criterios oficiales del DSM-5..."):
                resultados = analizar_caso_patu(caso_caso_clinico := caso_clinico)
                
                if not resultados:
                    st.info("No se encontraron coincidencias significativas que superen el umbral clínico mínimo. Intenta detallar más síntomas.")
                else:
                    st.success(f"Análisis completado. Se hallaron {len(resultados)} posibles sospechas diagnósticas:")
                    
                    # Mostrar resultados en tarjetas scannables
                    for res in resultados:
                        with st.expander(f"📋 {res['nombre']} — Coincidencia: {res['coincidencia']}%"):
                            st.write(f"**Categoría:** {res['categoria']}")
                            st.write(f"**Criterios Clínicos Detectados:** {res['criterios_match']}")
                            st.info("💡 Consejo: Revisa la pestaña PREMIUM para desplegar la guía diferencial y criterios completos de este ID.")

# ---------------------------------------------------------------------
# PANEL 2: MODO PREMIUM (Lecciones Guiadas del DSM-5)
# ---------------------------------------------------------------------
with tabs[1]:
    st.header("🎓 Lecciones guiadas del DSM-5")
    st.write("👉 Selecciona un trastorno para desplegar sus criterios oficiales y diagnósticos diferenciales:")
    
    # Selector mapeado con los IDs reales inyectados por database.py
    opciones_trastornos = {
        "1. Trastorno del Espectro del Autismo (TEA)": 1,
        "2. Trastorno por Déficit de Atención con Hiperactividad (TDAH)": 2,
        "3. Trastorno Límite de la Personalidad (TLP)": 3,
        "4. Trastorno de la Personalidad Antisocial": 4,
        "5. Trastorno de la Personalidad Narcisista": 5,
        "6. Trastorno de la Personalidad Histriónica": 6,
        "10. Trastorno Depresivo Mayor": 10,
        "11. Trastorno Bipolar I": 11,
        "12. Trastorno de Ansiedad Generalizada (TAG)": 12,
        "13. Trastorno de Pánico": 13,
        "20. Esquizofrenia": 20,
        "21. Anorexia Nerviosa": 21,
        "22. Bulimia Nerviosa": 22
    }
    
    seleccion = st.selectbox("Selecciona un trastorno:", list(opciones_trastornos.keys()))
    id_seleccionado = opciones_trastornos[seleccion]
    
    # Llamada segura a la función híbrida sin caídas por base de datos vacía
    nombre, categoria, descripcion_criterios, guia_diferencial = consultar_guia_trastorno(id_seleccionado)
    
    # Renderizado estético y limpio en pantalla
    st.markdown(f"## {nombre}")
    st.markdown(f"**Categoría Oficial:** *{categoria}*")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Criterios Clínicos (DSM-5)")
        st.markdown(descripcion_criterios)
        
    with col2:
        st.subheader("🔍 Guía de Diagnóstico Diferencial")
        st.warning(guia_diferencial)
