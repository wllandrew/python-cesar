import json

class Cifra:
    def __init__(self, name: str):
        self.name = name
        with open(name, 'r') as doc:
            self.text = doc.read()
        with open('config.json', 'r') as js:
            config = json.load(js)
        self.chave = config['chave']
        self.modo = config['modo']
        with open('palavrasComuns.txt', 'r') as pc:
            self.pc = [line.rstrip("\n") for line in pc]

    def ler(self):
        print(self.texto)

    def escrever(self):
        with open(self.name, 'w') as txt:
            txt.write(self.texto)

    def criptografar(self):
        stringDecript = []
        chaveReal = self.chave if self.modo == 'c' else (0 - self.chave)
        for n in self.text:
            if ord(n) > 64 and ord(n) < 91:
                stringDecript.append(chr((ord(n) - 65 + chaveReal) % 26 + 65))
            elif ord(n) > 96 and ord(n) < 123:
                stringDecript.append(chr((ord(n) - 97 + chaveReal) % 26 + 97))
            else:
                stringDecript.append(n)
        self.texto = ''.join(stringDecript)
        self.escrever()

    def forcaBruta(self):
        inicio = self.chave + 26
        resp = []
        while self.chave != inicio:
            self.criptografar()
            sd = self.texto.split('\n')
            for word in self.pc:
                if word in self.texto.split('\n'):
                    resp.append(self.chave)
            # print(f"{self.chave % 26} : {sd}")
            self.chave += 1
            '''
            for n in self.pc:
                if n in self.texto.split('\n'):
                    resp.append(self.chave)
            self.chave += 1
            '''

        for n in resp:
            self.chave = n
            self.criptografar()
            print(f'Chave:{self.chave} \nTexto: {self.texto}')


cif = Cifra("texto.txt")
#cif.criptografar()
cif.forcaBruta()