def escrever_arquivo():
    print("Digite algo: ")
    while True:
        arq = open("dados.txt", 'a')
        inp = input("")
        if inp.lower() == 'sair': break
        if inp.lower() == 'limpar':
            arq.close()
            lmp = open("dados.txt", 'w')
            lmp.write('')
            lmp.close()
            break
        arq.write(inp + "\n")
        arq.close()

escrever_arquivo()