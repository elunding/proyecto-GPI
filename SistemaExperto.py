
respuestas = []
preguntas = ["¿Cuando en la empresa hay una labor donde tienes experticia, escoges?\n a)Hacerlo solo b)Ser parte del equipo que haría esa labor c)Se lo dejas a alguien más d)Prefieres liderar el equipo",
             "¿Cómo te acomoda trabajar?\n a)Trabajar solo b)Trabajar en conjunto c)Me da lo mismo d)No me gusta trabajar",
             " Cuando ves que hay un error, ¿Qué haces?\n a)Lo comunicas a tu jefe de equipo b)Tomas la iniciativa c)Esperas a que lo solucione alguien de tu equipo d)Lo comunicas a tus compañeros para trabajarlo en conjunto",
             '¿Qué haces en tus tiempos libres?\n a)Hacer ejercicio b)Leer c)Ver televisión/ jugar videojuegos d)Tocar música ',
             'Cuando tienes dinero ¿ Qué es lo que haces ?\n a)Compartes con los demás b)Lo guardas o lo inviertes c)Lo gastas en ti, total para eso trabajas d)Te preocupa tu entorno y ayudas cuando hay que hacerlo',
             'Cuando conoces a un grupo nuevo de personas:\n a)Tratas de integrarte al grupo b)Esperas a que algunos de ellos tome la iniciativa para hablarte c)Te incomoda y molesta conocer a gente nueva d)Quieres pasar lo más desapercibido posible',
             'Ante una situación adversa:\n a)Buscas apoyo en los demás b)Ves la manera de solucionarlo por tus propios medios c)Necesitas de alguien que te contenga y anime constantemente d)Esperas paciente la mejor oportunidad para salir adelante',
             'Cuando has cometido errores, ¿como actúas ante ellos?\n a)Asumes la responsabilidad y tratas de arreglarlos/recompensarlos b)Ves la culpa en factores externos c)Te victimizas  d)Te culpas excesivamente',
             'Cuando se te presenta un gran desafío:\n a)Te sientes confiado b)Sientes inseguridad c)Te sientes entusiasmado d)Te causa indiferencia',
             'Si estás a cargo de un puesto importante en una organización, buscas:\n a)Plasmar tus ideas sin importar a los que tienes a cargo b)Establecer cercanía para que el grupo participe c)Lograr los objetivos para seguir escalando en la organización d)Estas conforme con tu puesto, y trabajas tranquilamente con los demás']
habilidades = []
necesidades = []
competencia = []


cadena = 'Elige una de las respuestas\n'

for pregunta in preguntas:
    print(pregunta)
    resp = input(cadena)
    if(resp != 'a' and resp!='b') and (resp != 'c' and resp!='d'):
        print('respuesta invalida')
        break
    else:
        respuestas.append(resp)
