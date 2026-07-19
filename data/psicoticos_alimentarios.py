# data/psicoticos_alimentarios.py

TRASTORNOS_PSIC_ALIM = [
    {
        "id": 20,
        "nombre": "Esquizofrenia",
        "cie10": "F20.9",
        "categoria": "Espectro de la Esquizofrenia y otros Trastornos Psicoticos",
        "guia_diferencial": "Diferenciar de: 1. Trastorno Esquizoafectivo (los sintomas afectivos duran la mayor parte del tiempo de la enfermedad; en la esquizofrenia son transitorios). 2. Trastorno Delirante (esta dominado por ideas delirantes no extravagantes, sin alucinaciones auditivas complejas ni desorganizacion del lenguaje).",
        "criterios": [
            ("A1", "Ideas delirantes fijas e inconmovibles frente a la realidad (persecucion, grandeza, referencia)."),
            ("A2", "Alucinaciones vividas y claras, habitualmente auditivas (escuchar voces que hablan entre si)."),
            ("A3", "Lenguaje desorganizado, descarrilamiento frecuente, incoherencia notable o habla incomprensible."),
            ("A4", "Comportamiento muy desorganizado o catatonico (agitacion sin sentido, posturas rigidas)."),
            ("A5", "Sintomas negativos como expresion emocional disminuida (aplanamiento afectivo) o abulia (falta de iniciativa).")
        ]
    },
    {
        "id": 21,
        "nombre": "Anorexia Nerviosa",
        "cie10": "F50.01",
        "categoria": "Trastornos de la Conducta Alimentaria",
        "guia_diferencial": "Diferenciar de: 1. Bulimia Nerviosa (los pacientes mantienen un peso corporal igual o por encima del limite minimo normal). 2. Trastorno de Ansiedad Social (el miedo se limita a la evaluacion social general, no exclusivamente al pavor a engordar y a la distorsion de la silueta).",
        "criterios": [
            ("A1", "Restriccion de la ingesta energetica en relacion con las necesidades, que conduce a un peso corporal significativamente bajo."),
            ("B1", "Miedo intenso a ganar peso o a engordar, o comportamiento persistente que interfiere en el aumento de peso."),
            ("C1", "Alteracion en la forma en que uno mismo percibe su propio peso o constitucion (distorsion de la autoimagen)."),
            ("C2", "Falta persistente de reconocimiento de la gravedad del bajo peso corporal actual.")
        ]
    },
    {
        "id": 22,
        "nombre": "Bulimia Nerviosa",
        "cie10": "F50.2",
        "categoria": "Trastornos de la Conducta Alimentaria",
        "guia_diferencial": "Diferenciar de: 1. Trastorno por Atracon (no se presentan conductas compensatorias inapropiadas como el vomito o uso de laxantes). 2. Anorexia de tipo purgativo (en la bulimia el peso se mantiene en rangos normales o sobrepeso).",
        "criterios": [
            ("A1", "Episodios recurrentes de atracones, caracterizados por ingestion de una cantidad de comida superior a la normal en un periodo corto."),
            ("A2", "Sensacion de falta de control sobre la comida durante el episodio de atracon."),
            ("B1", "Comportamientos compensatorios inapropiados recurrentes para evitar el aumento de peso como el vomito provocado, uso de laxantes o ayuno."),
            ("C1", "Los atracones y las conductas compensatorias inapropiadas se producen al menos una vez a la semana durante tres meses."),
            ("D1", "La autoevaluacion se ve influida indebidamente de manera casi exclusiva por la constitucion y el peso corporal.")
        ]
    }
]
