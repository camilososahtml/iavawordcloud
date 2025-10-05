import csv
import re

opiniones = """
Sobrevalorado, estuve 5to y 6to agronomía, y en cualquier turno los profesores exigen cosas que ni siquiera ellos saben, te hacen perder tiempo. Me fui al 26 y salve todo y con menos exigencias. Aclaremos si vas a hacer facultad te van a exigir mucho más de lo que está exigiendo el IAVA, Dámaso, Bauza, vas a ingresar con el cerebro en blanco.
Esta lleno de comunistas.
Como todos los liceos mas o menos.
Yo fuí al iava hace muchos años, me comí las ocupaciones... En 5o científico daban divisibilidad, se acababa de ir la paloma (no era que fuera exigente era que la vieja cagaba a todo el mundo), cosa al pedo si las hay, en el resto del Uruguay daba trigonometría en matemática A y nosotros comiendo del tupper al reverendo pedo con divisibilidad que es un huevo y buena parte de los profesores ni la entienden. La profesora de 5o de filosofía una cra, la de 6o un desastre. La gente de física sí exigentes pero no imposibles, buena gente aparte. Química todo bien, no se si tan exigentes la verdad, a mi no me pareció. El de dibujo era un HDP que sabía los kilos pero un sorete bárbaro. Era bastante mayor así que no debe estar más. El mayor HDP era de apellido Ponce de León o de león, un intento de ingeniero frustrado que se dedicaba a frustrar los estudiantes, daba matemática A y C en 6o de ingeniería y nunca dio clases en todo el año. Se sentaba en el escritorio y no hacía nada, no le importaba nada ni nadie y le resbalaba todo completamente. De mi grupo nadie terminó en el iava, yo entré a dar libres las de medicina, las de biología son unas HDP también pero por lo menos saben toda es información irrelevante e inútil que pretenden que sepas de memoria. El ambiente es más parecido a una facultad, eso no está para nada mal, te acostumbra a manejarte lo que está muy bueno, por otro lado es extremadamente politizado y conflictivo, te puedes encontrar perdiendo clases por cosas que no tienen nada que ver contigo y eso de que se votan las cosas no es del todo cierto, vienen de afuera a armar quilombo por boludeces, no se... Si tuviera que mandar a estudiar a mi hijo lo evitaría salvo que fuera a estudiar algo de humanístico capaz.
Todos los que conocí del iava en facultad se terminaron recibiendo.
Prefiero kotlin o c#.
Si claro, es el mejor liceo publico de Montevideo.
Ricas cosas.
si sos exigente contigo mismo, vas a estar bien en el IAVA, en el ibito o en el miranda.
Yo fui y en humanístico eran medio exigentes pero te exigían cosas que sí podías hacer realísticamente. Yo entré a la facultad sintiendome bastante segura con lo que había aprendido y al menos en el primer semestre me fue bien. Incluso llegué a estar brevemente en el gremio en 6to y no son tan comunistas radicales tupabolches como te los pinta reddit o los medios.
muchos profesores de ahi dan clases en otros liceo publicos tambien. y la verdad que al final lo que mas importa es si el profe es bueno o no... obvio tambien lo tiene que acompañar la clase para no quedar trancado, pero ahi hay mas margen, son unos cuantos liceos los que estan a ese nivel... lo mas alto posible en publico podríamos decir que sigue siendo una basura, pero bueno es lo que hay.
"""

archivo_csv = 'opiniones_iava22.csv'

muletillas = {
    "de", "la", "que", "el", "en", "y", "a", "los", "del", "se", "las", "por", "un", "para", "con", "no", "una", "su",
    "al", "lo", "como", "más", "pero", "sus", "le", "ya", "o", "este", "sí", "porque", "esta", "entre", "cuando",
    "muy", "sin", "sobre", "también", "me", "hasta", "hay", "donde", "quien", "desde", "todo", "nos", "durante",
    "todos", "uno", "les", "ni", "contra", "otros", "ese", "eso", "ante", "ellos", "e", "esto", "mí", "antes", "algunos",
    "qué", "unos", "yo", "otro", "otras", "otra", "él", "tanto", "esa", "estos", "mucho", "quienes", "nada", "muchos",
    "cual", "poco", "ella", "estar", "estas", "algunas", "algo", "nosotros", "mi", "mis", "tú", "te", "ti", "tu", "tus",
    "ellas", "nosotras", "vosotros", "vosotras", "os", "mío", "mía", "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas",
    "suyo", "suya", "suyos", "suyas", "nuestro", "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "vuestros",
    "vuestras", "esos", "esas", "estoy", "estás", "está", "estamos", "estáis", "están", "esté", "estés", "estemos",
    "estéis", "estén", "estaré", "estarás", "estará", "estaremos", "estaréis", "estarán", "estaría", "estarías",
    "estaríamos", "estaríais", "estarían", "estaba", "estabas", "estábamos", "estabais", "estaban", "estuve",
    "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron", "estuviera", "estuvieras", "estuviéramos",
    "estuvierais", "estuvieran", "estuviese", "estuvieses", "estuviésemos", "estuvieseis", "estuviesen", "estando",
    "estado", "estada", "estados", "estadas", "estad", "entonces", "pues"
}

def quitar_muletillas(texto):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    palabras_filtradas = [p for p in palabras if p not in muletillas]
    return ' '.join(palabras_filtradas)

with open(archivo_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Opinion'])
    for op in opiniones.splitlines():
        op_filtrada = quitar_muletillas(op)
        if op_filtrada.strip():
            writer.writerow([op_filtrada])

print(f'CSV "{archivo_csv}" creado sin palabras de stopwords.')