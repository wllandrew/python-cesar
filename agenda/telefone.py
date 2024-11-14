import json

class Agenda:
    def __init__(self, local):
        self.local = local
        with open(local, 'r') as loc:
            self.content = json.load(loc)
    def adicionar(self, nome, numero):
        add = {nome : numero}
        self.content.update(add)
        with open(self.local, 'w') as loc:
            json.dump(self.content, loc)
    # Limitação: função buscar acha apenas o valor por meio da chave e não a chave por meio do valor.
    def buscar(self, parametro):
        for n in self.content:
            if n == parametro:
                return True
            else:
                return False
    def excluir(self, nome):
        if self.buscar(nome):
            self.content.pop(nome)
        with open(self.local, 'w') as loc:
            json.dump(self.content, loc)
    def atualizar(self, nome, numNovo):
        self.content[nome] = numNovo
        with open(self.local, 'w') as loc:
            json.dump(self.content, loc)
    def imprimir(self):
        print(self.content)

ag = Agenda('agenda.json')
# Loop interface de funções do objeto agenda
while True:
    print("Atividade: adicionar(d), buscar(b), excluir(e), atualizar(a), imprimir(i)")
    resp = input("?: ")
    if resp.lower() == 'd':
        nomeAdd = input('Nome: ')
        telefoneAdd = input('Telefone: ')
        ag.adicionar(nomeAdd, telefoneAdd)
    elif resp.lower() == 'b':
        dadoBusca = input('Dado a ser buscado: ')
        if ag.buscar(dadoBusca):
            print('Está na lista')
        else:
            print('Não está na lista')
    elif resp.lower() == 'e':
        nomeExc = input("Nome a ser excluido: ")
        ag.excluir(nomeExc)
    elif resp.lower() == 'a':
        nomeAtt = input("Nome a ser atualizado: ")
        numeroAtt = (input("Numero novo: "))
        ag.atualizar(nomeAtt, numeroAtt)
    elif resp.lower() == 'i':
        ag.imprimir()
    elif resp.lower() == 'quit':
        break
