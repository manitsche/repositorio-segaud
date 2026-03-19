# Criptografia classica - Segurança e Auditoria de Sistemas - Aula 11/03/2026

## O que é Criptografia

Técnica de transformar informações em formato ilegível (cifrado).

Objetivo: garantir privacidade e segurança dos dados.

Apenas quem possui a chave consegue decifrar.

---

## Criptologia

Ciência que engloba:

- **Criptografia:** cria métodos de proteção.

- **Criptoanálise:** tenta quebrar a proteção (ataques).

---

## Conceitos Básicos

- **Cifrar:** transformar texto legível em ilegível.
- **Decifrar:** voltar ao formato original.
- **Plaintext:** texto original.
- **Ciphertext:** texto criptografado.
- **Cifra:** algoritmo de criptografia.
- **Chave:** informação secreta usada no processo

---

## Esteganografia

Técnica de esconder mensagens dentro de outras mídias (imagem, áudio, etc.).

A mensagem fica oculta, não apenas cifrada.

Exemplo: esconder texto em pixels de uma imagem (LSB).

---

## História

Muito antiga (Egito, Roma).

Evolução significativa com computadores.

Muito usada na Segunda Guerra Mundial.

---

## Princípio de Kerckhoffs

A segurança deve depender da chave, não do algoritmo.

O algoritmo pode ser público.

Evita “segurança por obscuridade”.

---

## Sistemas Criptográficos

### Tipos de chave:
 - Simétrica (mesma chave)
 - Assimétrica (chaves diferentes)

### Processamento:
 - Bloco
 - Fluxo (stream)

### Operações:
 - Substituição
 - Transposição

---

## Criptoanálise (Ataques)

Objetivo: descobrir a chave.

Tipos:
- Ataque analítico (baseado no algoritmo)
- Força bruta (testar todas as chaves)

---

## Formas de Criptografia

**Por código:** substitui palavras/frases inteiras.
**Por cifra:** altera letras ou posição (mais comum).

---

## Tipos de Cifras

### Substituição

 Troca letras por outras.
 Exemplos:
 Cifra de César (simples, fraca)
 Vigenère (mais complexa) 
 Monoalfabética (usa permutação)
 Playfair (usa pares de letras)

### Transposição

 Reorganiza a ordem das letras.
 Mantém as mesmas letras.
 Exemplos:
 Rail Fence
 Cítala (espartana)

### Cifra de Produto

 Combina substituição + transposição.
 Mais segura (base da criptografia moderna).
 One-Time Pad
 Usa chave aleatória do tamanho da mensagem.
 Teoricamente inquebrável.
 Difícil de usar na prática.

---

## Segurança das Cifras

Nem sempre muitas chaves = segurança.

Linguagem possui padrões (frequência de letras).

Isso permite quebrar cifras.

---

## Ideias principais

Criptografia protege dados.

Criptoanálise tenta quebrar.

Segurança moderna depende da chave, não do segredo do método.

Combinação de técnicas aumenta a segurança.