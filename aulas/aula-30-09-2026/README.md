# Aula 30/09/2026 - Continuação certificados digitais

## Componentes Básicos da ICP
- Chaves criptográficas
- Certificados digitais
- Autoridade Certificadora (AC)
- Autoridade Registradora (AR)
- Repositório de certificados (Diretório)

## Certificado Digital

É um documento de garantia da associação de chaves públicas e seus portadores (pessoas ou entidades)

Definido por ITU-T X.509

Composto por:
Dados do portador;
Chave pública do portador;
Dados da AC emissora;
Assinatura digital da AC emissora;
Período de validade do certificado;
Outros dados complementares;

## Autoridade Certificadora (AC)

"O aspecto principal de uma ICP é o da confiança!"

Autoridades Certificadoras são instituições em que as partes envolvidas na transação confiam;

Tem a função de garantir a associação de um portador (pessoa ou entidade) com seu par de chaves;

Emite os certificados digitais a partir de uma política estabelecida, que define como deve ser verificada a identidade do portador, e quais devem ser as regras e condições de segurança da própria AC.

## Autoridade Registradora (AR)

Autoridades Registradoras implementam a interface entre os usuários e a Autoridade Certificadora;

A Autoridade Registradora (AR) encarrega-se de receber as requisições de emissão ou de revogação de certificado do usuário, confirmar a identidade destes usuários e a validade de sua requisição, assim como do encaminhamento destes para a AC responsável, e entregar os certificados assinados pela AC aos seus respectivos solicitantes.

## Diretório

Armazena e disponibiliza os certificados, como um dos elementos pertencentes a um participante;

Padrão de acesso LDAP = Lightweight Directory Access Protocol (LDAP).

Controle de acesso e segurança embutidos;

Necessidade de escalabilidade e alta performance

## Fases de um certificado digital?

**Requerimento:** o usuário solicita a emissão do certificado digital.
**Validação do requerimento:** os dados e a identidade do solicitante são conferidos.
**Emissão do certificado:** o certificado é criado e disponibilizado pela autoridade certificadora.
**Aceitação:** o requerente confirma que os dados do certificado estão corretos.
**Uso:** o certificado pode ser utilizado para autenticação, assinaturas digitais e outras operações.
**Suspensão:** o certificado fica temporariamente impedido de ser utilizado, podendo ser reativado em determinadas situações.
**Revogação:** o certificado é cancelado definitivamente antes do fim de sua validade.
**Término da validade:** o certificado deixa de ser válido quando chega à data de expiração.
**Renovação:** um novo período de validade é obtido, seguindo os procedimentos exigidos pela autoridade certificadora.