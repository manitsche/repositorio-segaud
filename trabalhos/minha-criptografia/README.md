# Criptografia Híbrida Dinâmica (CHD)

## Descrição

Este projeto implementa um algoritmo de criptografia próprio, inspirado em métodos clássicos como:

- Cifra de César  
- Vigenère  
- Rail Fence  
- Transposição por blocos  

A proposta é combinar diferentes técnicas para criar um sistema mais complexo e menos suscetível a ataques simples.

---

## Funcionamento

O algoritmo é composto pelas seguintes etapas:

### 1. Conversão da chave
A chave fornecida é transformada em uma sequência numérica com base na posição de cada caractere no alfabeto.

---

### 2. Substituição (Vigenère Dinâmico)
Cada caractere do texto é deslocado no alfabeto de acordo com:
- o valor correspondente da chave  
- a posição do caractere no texto  

Isso gera um deslocamento variável ao longo da mensagem.

---

### 3. Inversão por blocos
O texto é dividido em blocos com tamanho igual ao comprimento da chave. Cada bloco é invertido.

---

### 4. Transposição (Rail Fence)
Os caracteres são reorganizados em um padrão de zigue-zague e depois recombinados, aumentando a dispersão.

---

### 5. Permutação baseada na chave
Dentro de cada bloco, os caracteres são reorganizados com base na ordenação dos valores da chave.

---

### 6. Padding
Caso o tamanho do texto não seja múltiplo do tamanho da chave, são adicionados caracteres de preenchimento (`X`) ao final para manter a consistência dos blocos.

---

## Decifragem

O processo de decifragem aplica as etapas na ordem inversa:

1. Desfaz a permutação  
2. Desfaz a transposição (Rail Fence)  
3. Desfaz a inversão dos blocos  
4. Aplica o deslocamento inverso  

A recuperação do texto original depende do uso da mesma chave.

---

## Interface

O programa possui uma interface gráfica desenvolvida com Tkinter, contendo:

- Campo para entrada de texto  
- Campo para chave  
- Botão para cifrar  
- Botão para decifrar  
- Área de saída para o resultado  

---

## Exemplo de uso

### Texto
~~~
The quick brown fox jumps over the lazy dog
~~~

### Chave
~~~
MarcoNitsche
~~~

### Procedimento

1. Inserir o texto e a chave  
2. Executar a cifragem  
3. Copiar o resultado  
4. Inserir o resultado e executar a decifragem  

### Resultado esperado
The quick brown fox jumps over the lazy dog


---

## Regras importantes

- A mesma chave deve ser utilizada para cifrar e decifrar  
- Qualquer alteração no texto cifrado impede a recuperação correta  
- O algoritmo diferencia letras maiúsculas e minúsculas  
- Espaços são suportados  

---

## Objetivo

O projeto tem como objetivo demonstrar:

- conceitos de criptografia clássica  
- combinação de técnicas de substituição e transposição  
- construção de um algoritmo reversível  
- tratamento de blocos com padding  

---

## Possíveis melhorias

- Suporte a caracteres especiais  
- Aplicação de múltiplas rodadas de criptografia  
- Implementação de análise de frequência  
- Exportação e importação de arquivos  
