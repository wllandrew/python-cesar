import json

class Cifra:
    def __init__(self, name: str):
        self.name = name

        with open(name, 'r') as doc:
            self.texto = doc.read()

        with open('config.json', 'r') as js:
            config = json.load(js)

        with open('palavrasComuns.txt', 'r', encoding="UTF-8") as pc:
            self.pc = pc.read()
            self.pc = self.pc.split("\n")

        self.modo = config['modo']
        self.chave = config['chave']

    def ler(self):
        print(self.texto)

    def escrever(self):
        if self.modo == 'forcabruta':
            self.forcaBruta()
        else: 
            with open(self.name, 'w') as txt:
                txt.write(self.criptografar(self.texto, self.chave))

    @staticmethod
    def criptografar(texto, chave : int) -> str:
        stringDecript = []
        for n in texto:
            if ord(n) > 64 and ord(n) < 91:
                stringDecript.append(chr((ord(n) - 65 + chave) % 26 + 65))
            elif ord(n) > 96 and ord(n) < 123:
                stringDecript.append(chr((ord(n) - 97 + chave) % 26 + 97))
            else:
                stringDecript.append(n)
        return ''.join(stringDecript)

    @staticmethod
    def maisFrequente(lst : list) -> int | None:
        valor = 0

        for i in lst:
            atualmaior = lst.count(i)
            if atualmaior > contador:
                contador = atualmaior
                valor = i
        
        return valor

    def forcaBruta(self):
        resp = []
        for word in self.pc:
            for n in range(26):
                if word in self.criptografar(self.texto, n) and len(word) > 2:
                    resp.append(n)

        ch = self.maisFrequente(resp)

        print(f'Chave: {ch}\n Texto: {self.criptografar(self.texto, ch)}')

cif = Cifra("texto.txt")
cif.escrever()