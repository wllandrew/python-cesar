def forca_bruta(cifra, inicio = None):
    pc = open('pc.txt', 'r')
    palavrasComuns = pc.read()
    pc.close()

    rang = range(26) if inicio == None else range(inicio, 26)

    for palavra in palavrasComuns:
        for n in rang:
            if palavra in criptografar(cifra, n, 'c'):
                return int(n)
            else:
                pass

def criptografar(texto, chave, modo):
    if modo == 'fb':
        resposta = forca_bruta(texto)
        print(criptografar(texto, chave, 'c'))
        contador = resposta
        while contador <= 26:
            again = input("Denovo? (s/n): ")
            if again.lower() == 's':
                iteration = forca_bruta(texto, contador)
                contador += iteration - contador
            else: 
                break
    
