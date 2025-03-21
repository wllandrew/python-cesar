# Cifragem com algoritmo de César em Python.

### 📌 Apresentação e melhorias

  Este projeto foi elaborado na aula de tópicos especiais, ministrado pelo Professor Diogo Olsen, no curso técnico de informática integrado ao ensino médio no IFPR.
  Para o futuro deste projeto, proponho algumas melhorias:
  - Otimização do algoritmo de decifragem força bruta.
  - Tratar acentos.

### 📚 Arquivo importantes

  - O arquivo __config.json__ é onde estão as configurações da cifragem. "Key" é o chave para criptografar/descriptografar e "Mode" define o modo de operação do programa, que pode ser "encrypt"(Criptografa), "decrypt"(Descriptografa) e "bruteforce"(Realiza um algoritmo de força bruta).
  - O arquivo _texto.txt_ é onde será escrito o texto a ser criptografado ou descriptografado.
  - O arquivo _main.py_ define a classe *Cifra*, nas quais os textos, como instâncias desta classe, serão sujeitos ao método de criptografagem, escrita, leitura.

### 🚀 Como usar 

Primeiro, clone o repositório.
```bash
git clone https://github.com/wllandrew/python-cesar.git
```
Depois, acesse o repositório.
```bash
cd python-cesar
```
Após alterar os arquivos __config.json__ e __texto.json__ à sua escolha, rode o programa com o comando:
```bash
python main.py
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/75044d71-fe46-473a-981f-5a1292350753" alt="animated"/>
</p>

# Decifragem por força bruta.

  Dentro da classe *Cifra*, está declarado um método chamado força bruta, que percorre o arquivo _palavrasComuns.txt_, que contém mais de duzentas mil palavras comuns no português, e, para cada cifragem possível do texto, encontra as suas ocorrências neste arquivo. No final, a função retorna a chave com o maior número de ocorrências.

### 🚀 Como usar

  Configure o "Mode" em __config.json__ para "bruteforce" e roda o programa. Ele irá retornar a chave provável e irá perguntar se você quer descriptografar, assim aplicando a chave provável automaticamente.

<p align="center">
  <img src="https://github.com/user-attachments/assets/de722852-118d-4742-87d3-27d0ac1085ab" alt="animated"/>
</p>


