# data/afectivos_ansiedad.py

TRASTORNOS_AFEC_ANSI = [
    {
        "id": 10,
        "nombre": "Trastorno Depresivo Mayor",
        "cie10": "F32.9",
        "categoria": "Trastornos Afectivos y del Estado de Animo",
        "guia_diferencial": "Diferenciar de: 1. Duelo normal (el afecto predominante es el sentimiento de vacio y perdida, no la incapacidad cronica de sentir placer ni la autodevaluacion severa). 2. Trastorno de Ansiedad Generalizada (la rumiacion es sobre eventos futuros, no sobre culpa pasada o ruina inminente). 3. Trastorno Bipolar (requiere ausencia estricta de episodios maniacos o hipomaniacos previos).",
        "criterios": [
            ("A1", "Estado de animo deprimido la mayor parte del dia, casi todos los dias, indicado por el sujeto o por otros."),
            ("A2", "Disminucion acusada del interes o de la capacidad para el placer (anhedonia) en todas o casi todas las actividades."),
            ("A3", "Perdida importante de peso sin hacer dieta o aumento de peso, o disminucion o aumento del apetito casi todos los dias."),
            ("A4", "Insomnio o hipersomnia casi todos los dias de la semana."),
            ("A5", "Agitacion o retraso psicomotor casi todos los dias observable por parte de los demas."),
            ("A6", "Fatiga o perdida de la energia casi todos los dias de manera constante."),
            ("A7", "Sentimiento de inutilidad o de culpa excesiva o inapropiada que puede ser delirante."),
            ("A8", "Disminucion de la capacidad para pensar o concentrarse, o para tomar decisiones, casi todos los dias."),
            ("A9", "Pensamientos de muerte recurrentes, ideas suicidas recurrentes sin un plan determinado o intento de suicidio.")
        ]
    },
    {
        "id": 11,
        "nombre": "Trastorno Bipolar I",
        "cie10": "F31.9",
        "categoria": "Trastornos Afectivos y del Estado de Animo",
        "guia_diferencial": "Diferenciar de: 1. Trastorno Limite de la Personalidad (la inestabilidad emocional cambia en horas; en el Bipolar I el episodio maniaco dura al menos una semana entera). 2. Esquizofrenia (los delirios y alucinaciones ocurren solo dentro de los episodios afectivos en el trastorno bipolar).",
        "criterios": [
            ("A1", "Un periodo bien definido de estado de animo anormal y persistentemente elevado, expansivo o irritable."),
            ("A2", "Aumento anormal y persistente de la actividad dirigida a objetivos o de la energia que dura minimo una semana."),
            ("B1", "Aumento de la autoestima o sentimiento de grandeza o prepotencia excesiva."),
            ("B2", "Disminucion de la necesidad de dormir, sintiendose descansado con solo tres horas de sueño."),
            ("B3", "Mas hablador de lo habitual o presion para mantener la conversacion sin interrupciones."),
            ("B4", "Fuga de ideas o experiencia subjetiva de que los pensamientos van a gran velocidad."),
            ("B5", "Facilidad de distraccion ante estimulos externos irrelevantes."),
            ("B6", "Participacion excesiva en actividades que tienen muchas posibilidades de producir consecuencias dolorosas.")
        ]
    },
    {
        "id": 12,
        "nombre": "Trastorno de Ansiedad Generalizada (TAG)",
        "cie10": "F41.1",
        "categoria": "Trastornos de Ansiedad y Estres",
        "guia_diferencial": "Diferenciar de: 1. Trastorno de Ansiedad Social (la ansiedad se limita a situaciones de evaluacion social). 2. Trastorno Obsesivo-Compulsivo (las preocupaciones en el TAG son sobre problemas de la vida real, no obsesiones extrañas o egodistonicas acompañadas de rituales).",
        "criterios": [
            ("A1", "Ansiedad y preocupacion excesiva (anticipacion aprensiva) que se produce durante mas dias de los que ha estado ausente durante un minimo de seis meses."),
            ("A2", "Al al sujeto le resulta dificil controlar la preocupacion o frenar los pensamientos rumiativos."),
            ("B1", "Inquietud o sensacion de estar atrapado o con los nervios de punta constantemente."),
            ("B2", "Facilidad para fatigarse o sentirse exhausto sin un esfuerzo fisico aparente."),
            ("B3", "Dificultad para concentrarse o quedarse con la mente en blanco ante situaciones de estres."),
            ("B4", "Irritabilidad constante o hipersensibilidad ante estimulos del entorno."),
            ("B5", "Tension muscular notable, dolores de cuello, espalda o rigidez corporal."),
            ("B6", "Problemas de sueño como dificultad para dormirse, continuar durmiendo o sueño inquieto e insatisfactorio.")
        ]
    },
    {
        "id": 13,
        "nombre": "Trastorno de Panico",
        "cie10": "F41.0",
        "categoria": "Trastornos de Ansiedad y Estres",
        "guia_diferencial": "Diferenciar de: 1. Trastorno de Ansiedad por Enfermedad (el paciente interpreta los sintomas como una enfermedad cronica, no como una crisis inminente de muerte). 2. Efectos fisiologicos de sustancias (intoxicacion por cafeina, cocaína o abstinencia).",
        "criterios": [
            ("A1", "Ataques de panico imprevistos y recurrentes caracterizados por una oleada abrupta de miedo intenso o malestar intenso."),
            ("A2", "Palpitaciones, golpeteo del corazon o aceleracion de la frecuencia cardiaca."),
            ("A3", "Sudoracion copiosa o escalofrios repentinos."),
            ("A4", "Temblores o sacudidas musculares involuntarias."),
            ("A5", "Sensacion de dificultad para respirar, asfixia o ahogo inminente."),
            ("A6", "Dolor, opresion o malestar en el torax o zona del pecho."),
            ("A7", "Nauseas o malestar abdominal persistente."),
            ("A8", "Sensacion de mareo, inestabilidad, aturdimiento o desmayo."),
            ("A9", "Parestesias o sensacion de entumecimiento u hormigueo en las extremidades."),
            ("A10", "Desrealizacion (sensacion de irrealidad) o despersonalizacion (separarse de uno mismo)."),
            ("A11", "Miedo absoluto a perder el control o a volverse loco."),
            ("A12", "Miedo inminente a morir durante el episodio agudo.")
        ]
    }
]
