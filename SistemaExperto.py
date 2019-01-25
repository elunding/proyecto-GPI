
respuestas = []
preguntas = ["¿Cuando en la empresa hay una labor donde tienes experticia, escoges?\n a)Hacerlo solo b)Ser parte del equipo que haría esa labor c)Se lo dejas a alguien más d)Prefieres liderar el equipo",
             "¿Cómo te acomoda trabajar?\n a)Trabajar solo b)Trabajar en conjunto c)Me da lo mismo d)No me gusta trabajar",
             " Cuando ves que hay un error, ¿Qué haces?\n a)Lo comunicas a tu jefe de equipo b)Tomas la iniciativa c)Esperas a que lo solucione alguien de tu equipo d)Lo comunicas a tus compañeros para trabajarlo en conjunto",
             'Cuando tienes dinero ¿ Qué es lo que haces ?\n a)Compartes con los demás b)Lo guardas o lo inviertes c)Lo gastas en ti, total para eso trabajas d)Te preocupa tu entorno y ayudas cuando hay que hacerlo',
             'Cuando conoces a un grupo nuevo de personas:\n a)Tratas de integrarte al grupo b)Esperas a que algunos de ellos tome la iniciativa para hablarte c)Te incomoda y molesta conocer a gente nueva d)Quieres pasar lo más desapercibido posible',
             'Ante una situación adversa:\n a)Buscas apoyo en los demás b)Ves la manera de solucionarlo por tus propios medios c)Necesitas de alguien que te contenga y anime constantemente d)Esperas paciente la mejor oportunidad para salir adelante',
             'Cuando has cometido errores, ¿como actúas ante ellos?\n a)Asumes la responsabilidad y tratas de arreglarlos/recompensarlos b)Ves la culpa en factores externos c)Te victimizas  d)Te culpas excesivamente',
             'Cuando se te presenta un gran desafío:\n a)Te sientes confiado b)Sientes inseguridad c)Te sientes entusiasmado d)Te causa indiferencia',
             'Si estás a cargo de un puesto importante en una organización, buscas:\n a)Plasmar tus ideas sin importar a los que tienes a cargo b)Establecer cercanía para que el grupo participe c)Lograr los objetivos para seguir escalando en la organización d)Estas conforme con tu puesto, y trabajas tranquilamente con los demás']
'''
habilidades = []
necesidades = []
competencia = []
'''
promedios = []

cadena = 'Elige una de las respuestas\n'

#


for pregunta in preguntas:
    print(pregunta)
    resp = input(cadena)
    if(resp != 'a' and resp!='b') and (resp != 'c' and resp!='d'):
        print('respuesta invalida')
        break
    else:
        respuestas.append(resp)




def prom_respuestas(a, b, c, d):

    cant_preguntas = 10

    prom_a = a/cant_preguntas
    prom_b = b/cant_preguntas
    prom_c = c/cant_preguntas
    prom_d = d/cant_preguntas

    if (prom_a > prom_b and prom_a > prom_c and prom_a > prom_d):
        print("el trabajador es estrategico")
    elif (prom_b > prom_a and prom_b > prom_c and prom_b > prom_d):
        print("el trabajador es tactico")

    elif (prom_c > prom_a and prom_c> prom_b and prom_c > prom_d ):
        print("el trabajador es operacional")

    elif (prom_d > prom_a and prom_d > prom_b and prom_d > prom_c):
        print("el trabajador es operacional")

    promedios.append(prom_a)
    promedios.append(prom_b)
    promedios.append(prom_c)
    promedios.append(prom_d)
    print(promedios)
    #print(prom_a, prom_b, prom_c, prom_d)
    #mayor = max(promedios)
    #print(mayor)


    '''
    for prom in range(len(promedios)):
        if(prom[i] > prom[i+1]):
            mayor = prom[i]
        elif(prom[i+1] > prom[i]):
            mayor = prom[i+1]
    print(mayor)
    '''

cont_a = 0
cont_b = 0
cont_c = 0
cont_d = 0


for i in range(len(respuestas)):
    if(respuestas[i] == 'a'):
        cont_a = cont_a + 1
    elif(respuestas[i]  == 'b'):
        cont_b = cont_b + 1
    elif(respuestas[i]  == 'c'):
        cont_c = cont_c + 1
    elif(respuestas[i]  == 'd'):
        cont_d = cont_d + 1

prom_respuestas(cont_a, cont_b, cont_c, cont_d)
