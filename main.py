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

        if self.Mode == "bruteforce":
            self.BruteForce()
        else:
            self.Encrypt()

    # Método que encriptografa/descriptografa o texto
    def Encrypt(self):
        
        # Reduz os modos a uma só chave
        key = self.Key if self.Key == "encrypt" else (26 - self.Key) % 26

        with open(self.fileName, 'w') as File:
            File.write(Cifra.CaesarAlgorithm(key, self.Text))

    
    # Método força bruta para achar uma key descriptografadora
    def BruteForce(self) -> int | list[int]:
        pass

    # Método estático que implementa o algoritmo de criptografagem de césar
    @staticmethod
    def CaesarAlgorithm(key : int, text : str) -> str:
        encrypt = ''

        for character in text:
            
            # Problema: não inclui caracteres especiais, como acentos
            if character.isalpha():
                if ord(character) >= 65 and ord(character) <= 90:
                    encrypt += chr((ord(character) - 65 + key) % 26 + 65)
                else:
                    encrypt += chr((ord(character) - 97 + key) % 26 + 97)
            else:
                encrypt += character

        return encrypt
            

def Main():
    cif = Cifra("texto.txt")

if __name__ == "__main__":
    Main()


