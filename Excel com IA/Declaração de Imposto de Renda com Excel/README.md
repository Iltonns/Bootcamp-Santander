# 📋 Declaração de Imposto de Renda com Excel

## 📌 Visão Geral

Planilha eletrônica desenvolvida em **Microsoft Excel** para facilitar a organização e compilação de dados necessários para a declaração do Imposto de Renda Pessoa Física (IRPF). Este projeto oferece uma solução integrada para centralizar informações pessoais, rendimentos bancários, movimentações financeiras e documentação de apoio.

---

## 🎯 Objetivos

- ✅ Centralizar dados pessoais do declarante
- ✅ Registrar informações de rendimentos bancários
- ✅ Documentar movimentações financeiras (entradas e saídas)
- ✅ Manter referência de documentos e anexos
- ✅ Facilitar a preparação para preenchimento da declaração de IR

---

## 📊 Estrutura do Projeto

A planilha é organizada em **4 abas** principais:

### 1️⃣ **ABA: TITULAR**
Seção dedicada ao registro de dados pessoais do contribuinte.

**Campos disponíveis:**
- Nome completo
- CPF
- Data de nascimento
- Título de eleitor
- Nome do cônjuge
- Endereço (rua/avenida e versão abreviada)
- CEP
- Telefone e celular
- E-mail
- Indicadores de situação fiscal:
  - Houve alteração da entrega anterior
  - Dependente cônjuge
  - Residente do exterior

**Dados preenchidos (exemplo):**
```
NOME: Eleilton Santos Gatinho
CPF: 123.456.789.11
NASCIMENTO: 09/12/1992
CÔNJUGE: Stephanie
ENDEREÇO: Rua Dez, Quadra 13, Nº 10
CEP: 65130-000
E-MAIL: ilton.sa@outlook.com
```

---

### 2️⃣ **ABA: INFORMES**
Registro de rendimentos bancários provenientes de diferentes instituições financeiras.

**Estrutura:**
- Campo de **TOTAL** com fórmula agregadora
- Espaço para registro de até **3 bancos**

**Informações por banco:**
- Código/Número do banco
- Valor atual em conta
- Referência de anexo (documentação PDF)

**Exemplos de bancos registrados:**
```
1º Banco: 260 - Nubank (R$ 500.000,00)
2º Banco: 380 - PicPay (R$ 1.000.000,00)
3º Banco: 77 - Banco Inter (R$ 800.000,00)

TOTAL: R$ 2.300.000,00
```

**Bancos disponíveis na tabela de referência:**
- Banco do Brasil, Bradesco, Itaú Unibanco, Santander
- Nubank, PicPay, Banco Inter, C6 Bank
- E mais de 40 instituições financeiras cadastradas

---

### 3️⃣ **ABA: NOTAS**
Registro de movimentações financeiras e extratos de holerites para comprovação de renda.

**Seções:**
- **ENTRADAS**: Registros de rendimentos

**Colunas:**
- Data da transação
- Categoria (ex: HOLERITE, transferência, etc.)
- Valor

**Capacidade:**
- Espaço para múltiplas entradas
- Permite rastreamento de diferentes fontes de renda

---

### 4️⃣ **ABA: TABELAS**
Base de dados de referência com lista padronizada de bancos brasileiros.

**Conteúdo:**
Lista com código e nome de mais de 50 instituições financeiras brasileiras:
- Banco de Brasil (código 1)
- Bradesco (código 237)
- Itaú Unibanco (código 341)
- Nubank (código 260)
- PicPay (código 380)
- E muitas outras...

**Utilidade:**
Fornece validação de dados e facilita seleção de bancos nas outras abas.

---

## 🚀 Como Utilizar

### Passo 1: Preenchimento de Dados Pessoais
1. Abra a aba **TITULAR**
2. Preencha os campos com seus dados pessoais
3. Confirme as informações de situação fiscal

### Passo 2: Registro de Rendimentos Bancários
1. Acesse a aba **INFORMES**
2. Para cada banco que possui conta:
   - Selecione o banco da tabela de referência
   - Informe o valor atual da conta
   - Anexe o comprovante em PDF (referência do arquivo)
3. O **TOTAL** será calculado automaticamente

### Passo 3: Documentar Movimentações Financeiras
1. Vá para a aba **NOTAS**
2. Registre todas as entradas (salários, prêmios, etc.)
3. Organize por data e categoria
4. Mantenha documentação de suporte (extratos, holerites)

### Passo 4: Verificação e Consolidação
1. Revise todos os dados nas 3 abas de entrada
2. Confirme os totalizadores
3. Reúna a documentação auxiliar referenciada
4. Use como base para preenchimento da declaração de IR

---

## 📄 Arquivos Anexados

A planilha referencia documentos em PDF como suporte:
- `Nubank_2025.pdf`
- `PicPay_2025.pdf`
- `Inter_2025.pdf`

*Nota: Recomenda-se manter estes arquivos no mesmo diretório ou em uma pasta de suporte organizada.*

---

## 🔧 Recursos Utilizados

- **Microsoft Excel** (formato .xlsx)
- **Fórmulas de soma e agregação**: Para cálculo automático de totais
- **Validação de dados**: Através da tabela de bancos
- **Formatação condicional**: Para melhor visualização

---

## 💡 Benefícios

✨ **Organização**: Centraliza todas as informações em um único arquivo
✨ **Rastreabilidade**: Mantém referência de documentos e valores
✨ **Automação**: Cálculos automáticos de totais
✨ **Facilidade**: Interface intuitiva e fácil de usar
✨ **Conformidade**: Estrutura alinhada com requisitos do IRPF

---

## 📋 Requisitos e Compatibilidade

- Microsoft Excel 2016 ou superior
- Compatibilidade com LibreOffice Calc
- Recomenda-se Windows ou macOS com Excel atualizado

---

## 👤 Informações do Contribuinte (Dados Atuais)

| Campo | Valor |
|-------|-------|
| **Nome** | Eleilton Santos Gatinho |
| **CPF** | 605.803.273-37 |
| **Data de Nascimento** | 09/12/1992 |
| **Telefone/Celular** | (48) 98874-4350 |
| **E-mail** | ilton.sa@outlook.com |
| **Patrimônio Bancário Total** | R$ 2.300.000,00 |

---

## 🔐 Dicas de Segurança

- 🔒 Mantenha este arquivo em local seguro
- 🔒 Faça backups regularmente
- 🔒 Proteja com senha se necessário (Excel oferece esta opção)
- 🔒 Guarde cópias dos documentos referenciados

---

## 📅 Versão

**v1.0** - Declaração de Imposto de Renda 2025

---

## 📝 Notas Importantes

- Esta planilha é um **instrumento de organização** para auxiliar na preparação da declaração
- Para informações oficiais sobre o IRPF, consulte o **Portal do e-CAC da Receita Federal**
- Recomenda-se validar todos os dados antes de utilizar na declaração oficial
- Mantenha documentação comprobatória de todas as informações registradas

---

**Última atualização:** 24 de janeiro de 2026

