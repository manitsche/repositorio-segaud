# Certificados Digitais

## Assinatura Digital

* Usa criptografia.
* Garante autenticidade.
* Garante integridade.
* Permite verificar quem assinou.

## Envelope Digital

Combina criptografia simétrica e assimétrica.

* Chave simétrica: criptografa a mensagem.
* Chave pública: criptografa a chave de sessão.
* Chave privada: recupera a chave de sessão.

## Problema da Chave Pública

Como saber se uma chave pública realmente pertence à pessoa?

Um invasor pode substituir uma chave pública por outra.

## Certificado Digital

Associa uma identidade a uma chave pública.

Exemplo:

```text
Nome + Chave Pública = Certificado Digital
```

## Autoridade Certificadora (CA)

A CA:

* Verifica a identidade.
* Emite o certificado.
* Assina o certificado com sua chave privada.

A chave pública da CA é usada para verificar o certificado.

## Certificado Digital x Certificação Digital

Certificado Digital: Arquivo eletrônico que associa uma identidade a uma chave pública.

Certificação Digital: Processo usado para garantir a identificação e a confiança.

## X.509

Padrão utilizado para certificados digitais.

Principais informações:

1. Versão
2. Número serial
3. Algoritmo de assinatura
4. Emissor
5. Validade
6. Sujeito
7. Chave pública
8. Extensões

## Extensões

**Key Usage:** Define o que a chave pode fazer.

**Extended Key Usage:** Define usos específicos da chave, como:
* Autenticação de servidor
* Autenticação de cliente
* TLS/SSL

## CRL

CRL significa Certificate Revocation List.

É uma lista de certificados que foram revogados.

## Resumo

```text
Certificado Digital
        ↓
Identidade + Chave Pública
        ↓
Assinado pela CA
        ↓
Verificado pela chave pública da CA
```

Frase para memorizar:

Certificado Digital = identidade + chave pública, assinadas por uma CA.

### Infraestrutura de chaves públicas

- PKI Brasil: Infraestrutura de chaves públicas = ICP Brasil