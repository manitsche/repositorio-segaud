# 🔐 Criptografia Cascata com Tkinter

Aplicação simples de criptografia feita em Python usando Tkinter.

Permite: - Criptografar texto - Descriptografar texto - Validar
caracteres inválidos - Usar apenas letras (A‑Z, a‑z) e espaço

------------------------------------------------------------------------

# 📚 Ideia da criptografia

O algoritmo NÃO usa tabela fixa de substituição.

Em vez disso, cada letra: - depende da posição no texto - depende de uma
chave aleatória (seed) - depende da letra anterior já criptografada

Isso cria um **efeito cascata**.

Se você mudar apenas 1 letra no início, todo o resto do texto muda.

------------------------------------------------------------------------

# 🔤 Alfabeto permitido

Apenas: A--Z, a--z e espaço

Se o usuário digitar números, símbolos ou acentos, o programa mostra
erro.

------------------------------------------------------------------------

# 🧩 Explicação do código (parte por parte)

## Importações

tkinter → cria a interface gráfica\
messagebox → mostra alertas/erros\
random → gera chave aleatória\
string → fornece o alfabeto

------------------------------------------------------------------------

## Alfabeto

ALFABETO guarda todos os caracteres válidos.

Cada letra vira um índice numérico:

A = 0\
B = 1\
C = 2 ...

Assim podemos fazer contas matemáticas com letras.

TAM guarda o tamanho do alfabeto.

------------------------------------------------------------------------

## Chaves secretas

seed e shift_inicial são números aleatórios.

Eles mudam toda vez que o programa abre.

Funcionam como a "senha" da criptografia.

Sem eles o texto não pode ser recuperado.

------------------------------------------------------------------------

## Validação

A função validar_texto verifica se o texto contém apenas caracteres
permitidos.

Se encontrar algo inválido: mostra messagebox.showerror e cancela a
operação.

------------------------------------------------------------------------

## Função cifrar()

Percorre cada letra do texto.

Passos: 1. Converte a letra em índice 2. Aplica fórmula matemática 3.
Gera novo índice 4. Converte de volta para letra

Fórmula usada:

~~~
novo = (idx + desloc + ultimo + seed \* (pos + 1)) % TAM
~~~

Isso mistura: - letra atual - letra anterior - posição - chave secreta

Resultado: saída imprevisível.

------------------------------------------------------------------------

## Função decifrar()

Faz o processo inverso.

Subtrai os mesmos valores usados na cifra.

Assim recupera exatamente o texto original.

------------------------------------------------------------------------

# 🖥 Interface gráfica

Feita com Tkinter usando grid().

Componentes:

-   Campo de entrada de texto
-   Botão Criptografar
-   Botão Descriptografar
-   Campo somente leitura para texto criptografado
-   Campo somente leitura para texto descriptografado

------------------------------------------------------------------------

# 🔁 Como usar

Criptografar: Digite o texto → clique Criptografar → copie o resultado

Descriptografar: Cole o texto criptografado → clique Descriptografar

------------------------------------------------------------------------