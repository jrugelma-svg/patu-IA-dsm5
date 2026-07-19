# app.py
import streamlit as st
from database import inicializar_patu_db
from engine import analizar_caso_patu, consultar_guia_trastorno

# Aseguramos regeneración limpia en la laptop
@st.cache_resource
def iniciar_sistema_patu():
    try:
        inicializar_patu_db()
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")

iniciar_sistema_patu()

st.set_page_config(page_title="Patu AI - DSM-5", page_icon="🦆", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #F3F4F6 !important; }
        p, span, label, li, div, h3, h4 { color: #111827 !important; font-weight: bold !important; }
        div[data-baseweb="select"] *, div[data-baseweb="textarea"] * { color: #111827 !important; font-weight: bold !important; }
        div[data-baseweb="select"] > div { background-color: #FFFFFF !important; border: 2px solid #1E3A8A !important; border-radius: 10px; }
        textarea { background-color: #FFFFFF !important; color: #111827 !important; border: 2px solid #1E3A8A !important; font-weight: bold !important; }
        .header-box { background: linear-gradient(135deg, #1E3A8A 0%, #065F46 100%); padding: 35px; border-radius: 20px; text-align: center; box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.15); margin-bottom: 25px; }
        .header-box h1 { color: #FFFFFF !important; font-weight: 900 !important; font-size: 3.2rem; margin: 0; }
        .header-box p { color: #FBBF24 !important; font-weight: bold !important; font-size: 20px !important; }
        .stButton>button { background: linear-gradient(90deg, #F59E0B 0%, #D97706 100%) !important; color: #000000 !important; font-weight: 900 !important; font-size: 22px !important; padding: 15px 30px !important; border-radius: 50px !important; border: 3px solid #000000 !important; box-shadow: 0px 5px 15px rgba(245, 158, 11, 0.5) !important; }
        .card-free { background-color: #FFFFFF !important; padding: 22px; border-radius: 15px; border: 3px solid #2563EB !important; box-shadow: 0px 4px 10px rgba(0,0,0,0.08); margin-bottom: 15px; }
        .card-premium { background-color: #FFFFFF !important; padding: 25px; border-radius: 15px; border: 3px solid #7C3AED !important; box-shadow: 0px 6px 15px rgba(139, 92, 246, 0.2); margin-bottom: 20px; }
        .badge-coincidencia { background-color: #FEE2E2 !important; color: #991B1B !important; padding: 6px 14px; border-radius: 8px; font-weight: 900 !important; font-size: 16px; border: 2px solid #991B1B; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='header-box'>
        <h1>🦆 ¡HOLA, SOY PATU AI!</h1>
        <p>Tu asistente didáctico de Psicopatología clínica y DSM-5-TR</p>
    </div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🟢 MODO GRATUITO (Aprende y Diagnostica)", "👑 MODO PREMIUM (Análisis Avanzado Clínico)"])

with tab1:
    st.markdown("### 🧑‍🎓 Lecciones guiadas del DSM-5")
    opcion = st.selectbox("👉 Selecciona un trastorno para desplegar sus criterios oficiales:", [
        "1. Trastorno Depresivo Mayor",
        "2. Trastorno Depresivo Persistente (Distimia)",
        "3. Trastorno de Ansiedad Generalizada",
        "4. Trastorno por Déficit de Atención (TDAH)",
        "5. Trastorno del Espectro del Autismo (TEA)",
        "6. Trastorno Límite de la Personalidad (TLP)",
        "7. Esquizofrenia",
        "8. Trastorno Delirante",
        "9. Anorexia Nerviosa"
    ], key="free_select")
    
    id_seleccionado = int(opcion.split(".")[0])
    trastorno, criterios = consultar_guia_trastorno(id_seleccionado)
    
    if trastorno:
        st.markdown(f"<div style='background-color: #D1FAE5; padding: 15px; border-radius: 10px; border: 2px solid #065F46; color: #065F46 !important;'><strong>📘 Trastorno Activo:</strong> {trastorno[0]} | <strong>Código CIE-10:</strong> {trastorno[1]}</div>", unsafe_allow_html=True)
        st.markdown("#### 📌 Criterios Clínicos:")
        for codigo, desc in criterios:
            st.markdown(f"**• {codigo}:** {desc}")
            
    st.markdown("---")
    st.markdown("### 🔍 Inteligencia Diagnóstica Rápida (Free)")
    caso_free = st.text_area("✍ Escribe o pega la narrativa sintomática aquí:", placeholder="Describe detalladamente los síntomas observados...", key="txt_free")
    
    if st.button("🔮 ¡Preguntar a Patu AI!", key="btn_free"):
        if not caso_free.strip():
            st.error("⚠️ Error: Debes escribir los síntomas en el recuadro superior.")
        else:
            resultados = analizar_caso_patu(caso_free)
            if not resultados:
                st.info("🦆 Patu informa: No se detectan síntomas suficientes para las categorías vigentes.")
            else:
                st.success("✨ ¡Resultados obtenidos con éxito!")
                for r in resultados:
                    st.markdown(f"""
                        <div class='card-free'>
                            <span class='badge-coincidencia'>🎯 Nivel de Coincidencia: {r['compatibilidad']}%</span>
                            <h3 style='color: #1E3A8A; margin-top: 15px; font-weight: 900;'>Trastorno Identificado: {r['nombre']}</h3>
                            <p style='margin-bottom:0px;'><b>Categoría del Manual:</b> Pertenece al bloque de <u>{r['categoria']}</u>.</p>
                        </div>
                    """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 👑 Evaluación Experta Multiaxial")
    caso_premium = st.text_area("📋 Inserte el Historial Clínico para desglose profundo:", placeholder="Pegue la anamnesis completa...", key="txt_premium")
    
    if st.button("⚡ Ejecutar Diagnóstico Avanzado Completo", key="btn_premium"):
        if not caso_premium.strip():
            st.error("⚠️ Error: Ingrese la narrativa clínica para la evaluación experta.")
        else:
            resultados = analizar_caso_patu(caso_premium)
            if not resultados:
                st.info("🦆 Patu Premium: Sintomatología por debajo del rango crítico.")
            else:
                principal = resultados[0]
                
                st.markdown(f"""
                    <div class='card-premium'>
                        <span class='badge-coincidencia' style='background-color: #F3E8FF; color: #5B21B6 !important; border-color: #5B21B6;'>EVALUACIÓN CLÍNICA MULTIAXIAL EXPERTA</span>
                        <h2 style='color: #4C1D95; margin-top:15px; font-weight: 900;'>🎯 Diagnóstico Principal: {principal['nombre']} ({principal['cie10']})</h2>
                        <hr style='border: 1px solid #111827;'>
                        <p><b>• Eje I (Síndromes Clínicos):</b> {principal['categoria']} - {principal['nombre']}</p>
                        <p><b>• Eje II (Personalidad o Neurodesarrollo):</b> {principal['nombre'] if 'Personalidad' in principal['categoria'] or 'Neurodesarrollo' in principal['categoria'] else 'No reporta rasgos patológicos en este eje.'}</p>
                        <p><b>• Eje III (Condiciones Médicas):</b> Requiere interconsulta médica de descarte.</p>
                        <p><b>• Eje IV (Problemas Psicosociales):</b> Afectación académica, laboral o familiar asociada.</p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("### 🔄 Análisis de Comorbilidad Coexistente")
                if len(resultados) > 1:
                    st.markdown("<div style='background-color: #FEF3C7; padding: 12px; border-radius: 8px; border: 2px solid #D97706; color: #D97706 !important;'><strong>⚠️ Alerta de Coexistencia:</strong> El paciente manifiesta criterios paralelos estables con:</div>", unsafe_allow_html=True)
                    for sec in resultados[1:]:
                        st.markdown(f"**• {sec['nombre']}** (Compatibilidad: {sec['compatibilidad']}%).")
                else:
                    st.markdown("**✅ Diagnóstico Limpio:** No se registran otros solapamientos sintomáticos en este bloque.")
                
                st.markdown("### 🧠 Guía Exclusiva de Diagnóstico Diferencial")
                st.markdown(f"**Criterios de exclusión críticos antes de sentenciar el caso de {principal['nombre']}:**")
                st.markdown(f"<div style='background-color: #FEE2E2; padding: 15px; border-radius: 10px; border: 2px solid #991B1B; color: #991B1B !important;'><strong>🚨 Metodología Diferencial:</strong> {principal['guia']}</div>", unsafe_allow_html=True)
