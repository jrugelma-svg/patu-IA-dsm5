# data/neuro_personalidad.py

TRASTORNOS_NEURO_PERSONALIDAD = [
    {
        "id": 1,
        "nombre": "Trastorno del Espectro del Autismo (TEA)",
        "cie10": "F84.0",
        "categoria": "Trastornos del Neurodesarrollo",
        "guia_diferencial": "Diferenciar de: 1. Trastorno de la comunicacion social (no presenta patrones de conducta restrictivos ni repetitivos). 2. Discapacidad intelectual (sin un deficit global del desarrollo intelectual disociado). 3. TDAH (la falta de atencion social en el TEA es por desinteres o incomprension, no por distraccion ejecutiva).",
        "criterios": [
            ("A1", "Deficits en la reciprocidad socioemocional, aproximaciones sociales anormales y fracaso en la conversacion bidireccional."),
            ("A2", "Deficits en conductas comunicativas no verbales utilizadas en la interaccion social, contacto visual y lenguaje corporal."),
            ("A3", "Deficits en el desarrollo, mantenimiento y comprension de las relaciones sociales y ajuste del comportamiento."),
            ("B1", "Movimientos, utilizacion de objetos o habla estereotipados o repetitivos como alineacion de juguetes o ecolalia."),
            ("B2", "Insistencia en la monotonia, excesiva inflexibilidad de rutinas o patrones ritualizados de comportamiento."),
            ("B3", "Intereses muy restringidos y fijos que son anormales en cuanto a su intensidad o foco de interes."),
            ("B4", "Hiper o hiporreactividad a los estimulos sensoriales o interes inhabitual por aspectos sensoriales del entorno.")
        ]
    },
    {
        "id": 2,
        "nombre": "Trastorno por Deficit de Atencion con Hiperactividad (TDAH)",
        "cie10": "F90.2",
        "categoria": "Trastornos del Neurodesarrollo",
        "guia_diferencial": "Diferenciar de: 1. Trastorno negativista desafiante (la resistencia a tareas es por hostilidad, no por olvido). 2. Trastorno de Ansiedad Generalizada (la falta de concentracion se debe a la rumiacion de preocupaciones cotidianas). 3. Trastornos depresivos (la inatencion aparece unicamente durante el transcurso de un episodio afectivo).",
        "criterios": [
            ("A1", "Falla en prestar la debida atencion a los detalles o por descuido comete errores en las tareas escolares o laborales."),
            ("A2", "Dificultades para mantener la atencion en tareas largas, lecturas prolongadas o actividades recreativas."),
            ("A3", "Parece no escuchar cuando se le habla directamente de frente, como si tuviera la mente en otro lugar."),
            ("A4", "No sigue las instrucciones y falla en terminar las tareas escolares, quehaceres o deberes en el lugar de trabajo."),
            ("A5", "Dificultad para organizar tareas y actividades cotidianas, mala gestion del tiempo y desorganizacion."),
            ("A6", "Evita, le disgusta o es renuente a iniciar tareas que requieren un esfuerzo mental sostenido como informes."),
            ("A7", "Pierde cosas necesarias para tareas o actividades como materiales escolares, llaves, billetera o de oficina."),
            ("A8", "Se distrae con mucha facilidad por estimulos externos, ruidos cotidianos o pensamientos irrelevantes."),
            ("A9", "Olvida las actividades cotidianas, tareas, hacer mandados, pagar cuentas o asistir a citas programadas."),
            ("B1", "Juguetea con o golpea las manos o los pies o se retuerce en el asiento constantemente cuando debe estar quieto."),
            ("B2", "Se levanta en situaciones en que se espera que permanezca sentado en la clase o en la oficina."),
            ("B3", "Corretea o trepa en situaciones en las que no es apropiado o sensacion de inquietud motora en adultos."),
            ("B4", "Incapaz de jugar o de dedicarse a actividades recreativas de manera tranquila o pausada."),
            ("B5", "Esta continuamente en marcha, acelerado o actua como si lo impulsara un motor electrico."),
            ("B6", "Habla excesivamente sin parar, interrumpiendo el flujo normal de las interacciones."),
            ("B7", "Responde inesperadamente o antes de que se haya concluido una pregunta por completo."),
            ("B8", "Le cuesta sumamente esperar su turno en filas o en juegos grupales."),
            ("B9", "Interrumpe o se inmiscuye con otros en juegos, conversaciones ajenas o actividades de los demas.")
        ]
    },
    {
        "id": 3,
        "nombre": "Trastorno Limite de la Personalidad (TLP)",
        "cie10": "F60.3",
        "categoria": "Trastornos de la Personalidad",
        "guia_diferencial": "Diferenciar de: 1. Trastorno Bipolar (los cambios de humor en el TLP duran horas o dias y reaccionan a eventos interpersonales; en el bipolar duran semanas). 2. Trastorno de la Personalidad Histrionica (no suele presentar la autodestructividad ni el vacio cronico del TLP).",
        "criterios": [
            ("A1", "Esfuerzos desesperados para evitar el desamparo o abandono real o imaginado por parte de seres queridos."),
            ("A2", "Patron de relaciones interpersonales inestables e intensas que se caracteriza por la alternancia entre la idealizacion y la devaluacion."),
            ("A3", "Alteracion de la identidad: inestabilidad intensa y persistente de la autoimagen o del sentido del yo."),
            ("A4", "Impulsividad en dos o mas areas que son potencialmente dañinas para si mismo como gastos, sexo, drogas o atracones."),
            ("A5", "Comportamiento, actitud o amenazas recurrentes de suicidio, o comportamiento de autolesion o cortes."),
            ("A6", "Inestabilidad afectiva debida a una reactividad notable del estado de animo, episodios de disforia, irritabilidad o ansiedad."),
            ("A7", "Sensacion cronica de vacio emocional o aburrimiento existencial profundo."),
            ("A8", "Enfado inapropiado e intenso, o dificultad para controlar la ira con peleas fisicas recurrentes."),
            ("A9", "Ideas paranoides transitorias relacionadas con el estres o sintomas disociativos graves.")
        ]
    },
    {
        "id": 4,
        "nombre": "Trastorno de la Personalidad Antisocial",
        "cie10": "F60.2",
        "categoria": "Trastornos de la Personalidad",
        "guia_diferencial": "Diferenciar de: 1. Trastorno por consumo de sustancias (la conducta antisocial debe manifestarse tambien fuera de los periodos de intoxicacion). 2. Trastorno de la Personalidad Narcisista (no incluye el historial de trastornos de la conducta en la infancia ni la agresividad fisica del antisocial).",
        "criterios": [
            ("A1", "Incumplimiento de las normas sociales respecto a los comportamientos legales, actuaciones repetidas que son motivo de detencion."),
            ("A2", "Engaño que se manifiesta por mentiras repetidas, utilizacion de alias o estafa para provecho o placer personal."),
            ("A3", "Impulsividad o fracaso para planear con antelacion el futuro."),
            ("A4", "Irritabilidad y agresividad que se manifiesta por peleas o agresiones fisicas repetidas."),
            ("A5", "Desatencion imprudente de la seguridad propia o de los demas."),
            ("A6", "Irresponsabilidad constante que se manifiesta por la incapacidad repetida de mantener un comportamiento laboral estable."),
            ("A7", "Ausencia de remordimiento que se manifiesta con indiferencia o racionalizacion del hecho de haber herido, maltratado o robado.")
        ]
    },
    {
        "id": 5,
        "nombre": "Trastorno de la Personalidad Narcisista",
        "cie10": "F60.81",
        "categoria": "Trastornos de la Personalidad",
        "guia_diferencial": "Diferenciar de: 1. Trastorno de la Personalidad Antisocial (el narcisista no suele presentar historial de delincuencia ni agresion fisica severa). 2. Trastorno Limite de la Personalidad (el narcisista es mas estable y no presenta automutilaciones ni miedo desesperado al abandono).",
        "criterios": [
            ("A1", "Tiene sentimientos de grandeza y prepotencia, exagera sus logros y talentos inesperadamente."),
            ("A2", "Esta absorto en fantasias de exito ilimitado, poder, brillantez, belleza o amor ideal."),
            ("A3", "Cree que es especial y unico y que solo pueden comprenderle otras personas especiales o de alto estatus."),
            ("A4", "Tiene una necesidad excesiva de admiracion, atencion y aplausos de los demas."),
            ("A5", "Muestra un sentimiento de privilegio, expectativas irrazonables de recibir un trato de favor."),
            ("A6", "Explota las relaciones interpersonales, se aprovecha de los demas para sus propios fines."),
            ("A7", "Carece de empatia, es incapaz o renuente a reconocer o identificarse con los sentimientos de los demas."),
            ("A8", "Con frecuencia envidia a los demas o cree que los demas le envidian a el."),
            ("A9", "Muestra comportamientos o actitudes arrogantes, soberbias y altivas.")
        ]
    },
    {
        "id": 6,
        "nombre": "Trastorno de la Personalidad Histrionica",
        "cie10": "F60.4",
        "categoria": "Trastornos de la Personalidad",
        "guia_diferencial": "Diferenciar de: 1. Trastorno Limite de la Personalidad (en el histrionico los arranques afectivos son menos autodestructivos). 2. Trastorno de la Personalidad Narcisista (el histrionico esta dispuesto a parecer fragil o dependiente con tal de llamar la atencion, el narcisista no).",
        "criterios": [
            ("A1", "Se siente incomodo en situaciones en las que no es el centro de la atencion."),
            ("A2", "La interaccion con los demas se caracteriza con frecuencia por un comportamiento sexualmente seductor o provocativo."),
            ("A3", "Presenta cambios rapidos y expresion plana o superficial de las emociones."),
            ("A4", "Utiliza constantemente el aspecto fisico para atraer la atencion hacia si mismo."),
            ("A5", "Tiene un estilo de hablar que es excesivamente subjetivo y carente de detalles reales."),
            ("A6", "Muestra autodramatizacion, teatralidad y expresion exagerada de la emocion."),
            ("A7", "Es sugestionable, facilmente influenciable por los demas o por las circunstancias."),
            ("A8", "Considera que las relaciones son mas estrechas e intimas de lo que lo son en realidad.")
        ]
    }
]
