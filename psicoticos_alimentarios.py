# data/psicoticos_alimentarios.py

TRASTORNOS_PSICOTICOS_ALIMENTARIOS = [
    {
        "id": 7,
        "nombre": "Esquizofrenia",
        "cie10": "F20.9",
        "categoria": "Espectro de la Esquizofrenia y otros Trastornos Psicóticos",
        "guia_diferencial": "Diferenciar del Trastorno Esquizoafectivo (requiere un episodio mayor del estado de ánimo simultáneo) y de trastornos debidos a efectos fisiológicos de una sustancia.",
        "criterios": [
            ("A1", "Delirios (creencias fijas no susceptibles de cambio a la luz de pruebas en contra)."),
            ("A2", "Alucinaciones (percepciones que tienen lugar sin la presencia de un estímulo externo)."),
            ("A3", "Discurso desorganizado (ej. descarrilamiento frecuente o incoherencia)."),
            ("A4", "Comportamiento muy desorganizado o catatónico."),
            ("A5", "Síntomas negativos (expresión emotiva disminuida o abulia)."),
            ("B", "El funcionamiento en uno o más campos principales (trabajo, relaciones, cuidado propio) está muy por debajo del nivel alcanzado antes del inicio.")
        ]
    },
    {
        "id": 8,
        "nombre": "Trastorno Delirante",
        "cie10": "F22",
        "categoria": "Espectro de la Esquizofrenia y otros Trastornos Psicóticos",
        "guia_diferencial": "A diferencia de la esquizofrenia, nunca se ha cumplido el Criterio A de la esquizofrenia; las alucinaciones, si existen, no son prominentes y guardan relación con el tema delirante.",
        "criterios": [
            ("A", "Presencia de uno o más delirios de un mes o más de duración."),
            ("B", "Nunca se ha cumplido el Criterio A de la Esquizofrenia."),
            ("C", "Aparte del impacto de los delirios, el funcionamiento no está muy alterado y el comportamiento no es manifiestamente extravagante.")
        ]
    },
    {
        "id": 9,
        "nombre": "Anorexia Nerviosa",
        "cie10": "F50.01",
        "categoria": "Trastornos de la Conducta Alimentaria y de la Ingesta de Alimentos",
        "guia_diferencial": "Diferenciar de afecciones médicas (ej. enfermedad de Crohn), Trastorno Depresivo Mayor (donde la pérdida de peso no se asocia a distorsión de la imagen corporal) o fobia social.",
        "criterios": [
            ("A", "Restricción de la ingesta energética en relación con las necesidades, que conduce a un peso corporal significativamente bajo."),
            ("B", "Miedo intenso a ganar peso o a engordar, o comportamiento persistente que interfiere en el aumento de peso."),
            ("C", "Alteración en la forma en que uno mismo percibe su propio peso o constitución (distorsión de la imagen corporal).")
        ]
    }
]
