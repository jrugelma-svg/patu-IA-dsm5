# data/afectivos_ansiedad.py

TRASTORNOS_AFECTIVOS_ANSIEDAD = [
    {
        "id": 1,
        "nombre": "Trastorno Depresivo Mayor",
        "cie10": "F32.9",
        "categoria": "Trastornos Depresivos",
        "guia_diferencial": "Diferenciar de la tristeza normal, el duelo por pérdida o el Trastorno Depresivo Persistente (Distimia) debido a la cronicidad y severidad de los episodios.",
        "criterios": [
            ("A1", "Estado de ánimo deprimido la mayor parte del día, casi todos los días."),
            ("A2", "Disminución importante del interés o el placer por todas o casi todas las actividades (anhedonia)."),
            ("A3", "Pérdida o aumento importante de peso, o disminución o aumento del apetito casi todos los días."),
            ("A4", "Insomnio o hipersomnia casi todos los días."),
            ("A5", "Agitación o retraso psicomotor casi todos los días (observable por parte de otros)."),
            ("A6", "Fatiga o pérdida de energía casi todos los días."),
            ("A7", "Sentimiento de inutilidad o culpabilidad excesiva o inapropiada casi todos los días."),
            ("A8", "Disminución de la capacidad para pensar o concentrarse, o para tomar decisiones."),
            ("A9", "Pensamientos de muerte recurrentes, ideas suicidas recurrentes sin plan determinado o intento de suicidio.")
        ]
    },
    {
        "id": 2,
        "nombre": "Trastorno Depresivo Persistente (Distimia)",
        "cie10": "F34.1",
        "categoria": "Trastornos Depresivos",
        "guia_diferencial": "Requiere un estado de ánimo deprimido durante al menos dos años. Si los síntomas cumplen el criterio de un episodio depresivo mayor continuo, se codifica como tal.",
        "criterios": [
            ("B1", "Estado de ánimo deprimido durante la mayor parte del día, durante un mínimo de dos años."),
            ("B2", "Poco apetito o sobrealimentación."),
            ("B3", "Insomnio o hipersomnia."),
            ("B4", "Poca energía o fatiga."),
            ("B5", "Baja autoestima."),
            ("B6", "Falta de concentración o dificultad para tomar decisiones."),
            ("B7", "Sentimientos de desesperanza.")
        ]
    },
    {
        "id": 3,
        "nombre": "Trastorno de Ansiedad Generalizada",
        "cie10": "F41.1",
        "categoria": "Trastornos de Ansiedad",
        "guia_diferencial": "Diferenciar del trastorno de ansiedad por enfermedad, trastorno obsesivo-compulsivo o el estrés postraumático.",
        "criterios": [
            ("A", "Ansiedad y preocupación excesiva (anticipación aprensiva) que se produce durante más días de los que ha estado ausente durante un mínimo de seis meses, en relación con diversos sucesos."),
            ("B", "Al individuo le resulta difícil controlar la preocupación."),
            ("C1", "Inquietud o sensación de estar atrapado o con los nervios de punta."),
            ("C2", "Facilidad para fatigarse."),
            ("C3", "Dificultad para concentrarse o quedarse con la mente en blanco."),
            ("C4", "Irritabilidad."),
            ("C5", "Tensión muscular."),
            ("C6", "Problemas de sueño (dificultad para dormirse o continuar durmiendo, o sueño inquieto e insatisfactorio).")
        ]
    }
]
