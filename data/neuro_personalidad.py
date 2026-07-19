# data/neuro_personalidad.py

TRASTORNOS_NEURO_PERSONALIDAD = [
    {
        "id": 4,
        "nombre": "Trastorno por Déficit de Atención e Hiperactividad (TDAH)",
        "cie10": "F90.2",
        "categoria": "Trastornos del Neurodesarrollo",
        "guia_diferencial": "Diferenciar de comportamientos propios de la edad, Trastorno Negativista Desafiante o ansiedad, donde la falta de concentración es secundaria al malestar emocional.",
        "criterios": [
            ("A1a", "Con frecuencia falla en prestar la debida atención a los detalles o por descuido comete errores."),
            ("A1b", "Con frecuencia tiene dificultades para mantener la atención en tareas o actividades recreativas."),
            ("A1c", "Con frecuencia parece no escuchar cuando se le habla directamente."),
            ("A2a", "Con frecuencia juguetea con o golpea las manos o los pies o se retuerce en el asiento."),
            ("A2b", "Con frecuencia se levanta en situaciones en que se espera que permanezca sentado."),
            ("A2c", "Con frecuencia corretea o trepa en situaciones en las que no resulta apropiado.")
        ]
    },
    {
        "id": 5,
        "nombre": "Trastorno del Espectro del Autismo (TEA)",
        "cie10": "F84.0",
        "categoria": "Trastornos del Neurodesarrollo",
        "guia_diferencial": "Diferenciar del Trastorno de la Comunicación Social, Discapacidad Intelectual sin TEA o Trastorno de Movimientos Estereotipados.",
        "criterios": [
            ("A1", "Deficiencias en la reciprocidad socioemocional (conversaciones bilaterales, compartir intereses)."),
            ("A2", "Deficiencias en las conductas comunicativas no verbales utilizadas en la interacción social."),
            ("A3", "Deficiencias en el desarrollo, mantenimiento y comprensión de las relaciones."),
            ("B1", "Movimientos, utilización de objetos o habla estereotipados o repetitivos."),
            ("B2", "Insistencia en la monotonía, excesiva inflexibilidad de rutinas o patrones ritualizados."),
            ("B3", "Intereses muy restringidos y fijos que son anormales en cuanto a su intensidad o foco.")
        ]
    },
    {
        "id": 6,
        "nombre": "Trastorno Límite de la Personalidad (TLP)",
        "cie10": "F60.3",
        "categoria": "Trastornos de la Personalidad",
        "guia_diferencial": "Diferenciar del Trastorno Bipolar (donde los cambios de humor duran semanas), o de otros trastornos de la personalidad como el Histriónico o Narcisista.",
        "criterios": [
            ("A1", "Esfuerzos desesperados para evitar el desamparo o abandono real o imaginado."),
            ("A2", "Patrón de relaciones interpersonales inestables e intensas (idealización y devaluación)."),
            ("A3", "Alteración de la identidad: inestabilidad intensa y persistente de la autoimagen."),
            ("A4", "Impulsividad en dos o más áreas que son potencialmente dañinas para sí mismo."),
            ("A5", "Comportamiento, actitud o amenazas recurrentes de suicidio, o comportamiento de automutilación."),
            ("A6", "Inestabilidad afectiva debida a una reactividad notable del estado de ánimo.")
        ]
    }
]
