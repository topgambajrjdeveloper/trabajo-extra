def romano_a_arabigo(romano):
    romanos = {'M': 1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    entero=0
    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i-1]]:
            entero += romano[romano[i]]-2 * romanos[romano[i-1]]
        else:
            entero += romanos[romano[i]]   

    print('Este es el número en romano:', entero)


def arabigo_a_romano(entero):
    numeros = [1000, 500, 100, 50, 10, 5, 1]
    numerales = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    numeral = ''
    i = 0

    while entero > 0:
        for _ in range(entero // numeros[i]):
            numeral += numerales[i]
            entero -= numeros[i]
        i += 1
    print('Este es el número en romano:', numeral)


arabigo_a_romano(1098) #Introduce aqui el entero
romano_a_arabigo('CXXIII') #Introduce aqui el romano