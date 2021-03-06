def leer_frase():
    global txt
    txt = (input("Ingresa una texto: ")).lower()


dictSilabas = {
    'consonantes': [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'p',
        'q', 'r', 's', 't', 'v', 'w', 'x', 'z'
    ],
    'vocales_abiertas': ['a', 'e', 'o', 'á', 'é', 'ó', 'ú'],
    'vocales_cerradas': ['i', 'u', 'ü'],
    'semivocles': ['y']
}

#diptongos = [(dictSilabas.vocales_abiertas + dictSilabas.vocales_cerradas),
#             (dictSilabas.vocales_abiertas + dictSilabas.vocales_cerradas),
#             (dictSilabas.vocales_abiertas + dictSilabas.vocales_cerradas)]
#triptongos = dictSilabas.vocales_cerradas+dictSilabas.vocales_abiertas + dictSilabas.vocales_cerradas
pares_consonantes=[pares_consonantes=['bl', 'cl', 'fl', 'gl', 'kl', 'pl', 'tl', 'br', 'cr', 'dr', 'fr', 'gr', 'kr', 'pr', 'tr', 'ch', 'll', 'rr']
]


def separar_silabas():
    part = txt.split('-')
    for i in dictSilabas:
        for j in part:
            if i.isalpha():
                print('Estas son las silabas en la frase: ', part)


def contar_vocales():
    vocal = ['a', 'e', 'o', 'á', 'é', 'ó', 'ú', 'i', 'u', 'ü']
    contador = 0
    for i in vocal:
        for j in txt:
            if (i == j):
                contador += 1
    print('El numero de vocales es: ', contador)


def contar_consonantes():
    consonantes = [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'p',
        'q', 'r', 's', 't', 'v', 'w', 'x', 'z'
    ]
    contador = 0
    for i in consonantes:
        for j in txt:
            if (i == j):
                contador += 1
    print(' El numero de consonantes es: ', contador)


def pares_consonantes():
    pares = [
        'bl', 'cl', 'fl', 'gl', 'kl', 'pl', 'tl', 'br', 'cr', 'dr', 'fr', 'gr',
        'kr', 'pr', 'tr', 'ch', 'll', 'rr'
    ]
    contador = 0
    for i in pares:
        for j in txt:
            if (i == j):
                contador += 1
    print(' El numero de pares es: ', contador)


def contar_letra_en_frase():
    contador = 0
    for i in txt:
        if (i.isalpha()):
            contador += 1
    print(' La cantidad de letras es: ', contador)


leer_frase()
contar_letra_en_frase()
contar_consonantes()
pares_consonantes()
separar_silabas()
contar_vocales()
