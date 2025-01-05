import json

class Cifra:

    # Construtor que define o texto a ser criptografado e configurações.
    def __init__(self, fileName : str):
        self.fileName = fileName

        with open(self.fileName, 'r') as File:
            self.Text = File.read()

        with open("config.json", 'r') as Config:
            Configurations = json.load(Config)

        self.Mode = Configurations['Mode']
        self.Key = Configurations['Key']

        # Métodos na inicialização
        if not self.Mode == "bruteforce":
            self.Encrypt()

        else:
            # Saber a diferença entre a chave provavel e atual permite a descriptografagem

            (likelyKey, actualKey) = self.BruteForce()
            print(f"Likely key: {likelyKey}")
            option = input("Want to decrypt? (y/n): ")

            if option == 'y':
                self.Mode = "encrypt"
                self.Key = abs(likelyKey - actualKey)
                self.Encrypt()

    # Método que encriptografa/descriptografa o texto
    def Encrypt(self):
        
        # Reduz os modos a uma só chave
        key = self.Key if self.Mode == "encrypt" else (26 - self.Key) % 26

        with open(self.fileName, 'w') as File:
            File.write(Cifra.CaesarAlgorithm(key, self.Text))
    
    # Método força bruta para achar uma key descriptografadora
    def BruteForce(self) -> int | list[int]:
    
        ''' 
        Primeiro, ler um pedaço do texto, 
        Segundo, separar apenas as pelavras completas desse trecho,
        Terceiro, iterar para cada chave possível em um dicionario e inserir as palavras em uma lista
        Quarto, a partir de cada chave, contabilizar o número de ocorrencias na lista de palavras
        Quinto, retornar a(s) chave(s) com maior número de ocorrências e a chave atual
        '''

        self.textChunk = self.Text[0:100:1]
        self.textChunk = self.textChunk.split(" ")

        # O(n)
        key_words = dict()
        for key in range(26):
            key_words[key] = []
            for n in self.textChunk:
                key_words[key].append(Cifra.CaesarAlgorithm(key, n))
                if key_words[key] == self.textChunk:
                    actualKey = key

        with open("palavrasComuns.txt", 'r', encoding="UTF-8") as PalavrasComuns:
            self.PalavrasComuns = PalavrasComuns.read()

        # O(nm)
        key_occurences = dict()
        for key, value in key_words.items():
            for word in value:
                if word in self.PalavrasComuns:
                    key_occurences[key] = 1 + key_occurences.get(key, 0)

        return (max(key_occurences, key=key_occurences.get), actualKey)

    # Método estático que implementa o algoritmo de criptografagem de césar
    @staticmethod
    def CaesarAlgorithm(key : int, text : str) -> str:
        encrypt = ''

        for character in text:
            
            # Problema: não inclui caracteres especiais, como acentos
            if not character.isalpha():
                encrypt += character
            else:
                if ord(character) >= 65 and ord(character) <= 90:
                    encrypt += chr((ord(character) - 65 + key) % 26 + 65)
                else:
                    encrypt += chr((ord(character) - 97 + key) % 26 + 97)

        return encrypt
            
def Main():
    cif = Cifra("texto.txt")

if __name__ == "__main__":
    Main()