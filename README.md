# Cifragem com algoritmo de César em Python.

### Configurações

  O arquivo __config.json__ é onde estão as configurações da cifragem.

### Mensagem

  O arquivo _texto.txt_ é onde será escrito o texto a ser criptografado ou descriptografado.

### Código

  O arquivo _main.py_ define a classe *Cifra*, nas quais os textos, como instâncias desta classe, serão sujeitos ao método de criptografagem, escrita, leitura.

# Decifragem por força bruta.

  Dentro da classe *Cifra*, está declarado um método chamado força bruta, que percorre o arquivo _palavrasComuns.txt_, que contém mais de duzentas mil palavras comuns no português, e, para cada cifragem possível do texto, encontra as suas ocorrências neste arquivo. No final, a função retorna a chave com o maior número de ocorrências.
