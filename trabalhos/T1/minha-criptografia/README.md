# Minha Criptografia

## Descrição

Este projeto implementa um sistema simples de criptografia e descriptografia baseado em deslocamentos dinâmicos. O algoritmo transforma um texto composto apenas por letras (A-Z, a-z) e espaços em uma versão criptografada, que pode ser revertida ao texto original.

A lógica utiliza valores aleatórios gerados no início da execução, tornando a criptografia diferente a cada vez que o programa é executado.

---

## Como funciona

### Alfabeto

O sistema trabalha com um conjunto fixo de caracteres:

- Letras maiúsculas (A-Z)
- Letras minúsculas (a-z)
- Espaço

Cada caractere é tratado como um índice dentro desse alfabeto.

---

### Parâmetros principais

- `seed`: número aleatório entre 5 e 50 que influencia o deslocamento progressivo
- `shift_inicial`: deslocamento inicial aleatório baseado no tamanho do alfabeto

Esses valores são essenciais para o funcionamento correto da criptografia e descriptografia.

---

### Validação

Antes de processar o texto, o sistema verifica se todos os caracteres pertencem ao alfabeto permitido. Caso contrário, a operação é interrompida.

---

## Criptografia

A função `cifrar` transforma o texto original em texto criptografado.

### Processo

Para cada caractere:

1. Obtém o índice do caractere no alfabeto
2. Aplica a fórmula:
~~~
novo = (idx + desloc + ultimo + seed * (pos + 1)) % TAM
~~~

Onde:
- `idx`: índice do caractere atual
- `desloc`: valor de deslocamento atual
- `ultimo`: índice do último caractere criptografado
- `pos`: posição do caractere no texto
- `seed`: valor aleatório definido no início
- `TAM`: tamanho do alfabeto

3. Atualiza os valores:
~~~
ultimo = novo
desloc = novo
~~~

4. Converte o novo índice de volta para caractere

### Observação

Cada caractere depende do anterior, criando um efeito acumulativo.

---

## Descriptografia

A função `decifrar` reverte o texto criptografado ao original.

### Processo

Para cada caractere:

1. Obtém o índice do caractere criptografado
2. Aplica a fórmula inversa:

~~~
original = (idx - desloc - ultimo - seed * (pos + 1)) % TAM
~~~

3. Atualiza os valores:
~~~
ultimo = idx
desloc = idx
~~~


4. Converte o índice obtido para o caractere original

---

## Características

- Cada execução gera uma criptografia diferente
- O algoritmo possui dependência entre caracteres (efeito cascata)
- Textos iguais podem gerar saídas diferentes dependendo da posição

---

## Limitações

- Não suporta números, acentos ou símbolos
- Não é adequado para segurança real
- A descriptografia depende dos mesmos valores de `seed` e `shift_inicial`
- Esses valores não são salvos automaticamente

---

## Exemplo conceitual

Entrada:

~~~
OLA
~~~

Cada caractere é transformado considerando:
- sua posição
- o caractere anterior
- os valores aleatórios

O resultado final parece aleatório, mas pode ser revertido com os mesmos parâmetros.

---

## Conclusão

O algoritmo é uma variação de cifra de substituição com deslocamento dinâmico e estado interno. Ele combina:

- deslocamento progressivo
- dependência entre caracteres
- fator aleatório