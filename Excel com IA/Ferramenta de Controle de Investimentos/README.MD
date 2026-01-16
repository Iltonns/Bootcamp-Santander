# Ferramenta de Controle de Investimentos

## 📋 Descrição do Projeto

A **Ferramenta de Controle de Investimentos** é uma planilha Excel interativa desenvolvida para ajudar na tomada de decisões sobre investimentos em Fundos Imobiliários (FII). A ferramenta permite simular diferentes cenários de investimento a longo prazo e gera recomendações de alocação de capital com base no perfil de risco do investidor.

## 🎯 Objetivo

O principal objetivo é fornecer uma forma simples e visual para:
- Calcular quanto investir mensalmente com base no salário
- Simular o patrimônio acumulado em diferentes períodos (2, 5, 10, 20 e 30 anos)
- Estimar os dividendos mensais gerados pelos investimentos
- Sugerir uma alocação de investimentos em diferentes tipos de FII conforme o perfil de risco

## 📊 Funcionalidades

### 1. **Configurações Iniciais**
   - **Salário**: Valor mensal do salário (padrão: R$ 2.000)
   - **Rendimento da Carteira**: Taxa de rendimento mensal esperada (padrão: 0,6%)
   - **Sugestão de Investimento**: Calcula automaticamente 30% do salário como valor sugerido para investir

### 2. **Cálculo de Investimento Mensal**
   - **Aporte Mensal**: Valor a ser investido mensalmente (baseado na sugestão de 30%)
   - **Período de Investimento**: Número de anos para investir (padrão: 5 anos)
   - **Taxa de Rendimento**: Rendimento mensal esperado (padrão: 1,079%)
   - **Patrimônio Acumulado**: Calcula o valor total acumulado usando a função FV do Excel
   - **Dividendos Mensais**: Estima os dividendos mensais gerados pelo patrimônio

### 3. **Análise de Cenários**
   Simula quanto você teria investido em diferentes períodos:
   - **2 Anos**: Patrimônio acumulado + Dividendos mensais estimados
   - **5 Anos**: Patrimônio acumulado + Dividendos mensais estimados
   - **10 Anos**: Patrimônio acumulado + Dividendos mensais estimados
   - **20 Anos**: Patrimônio acumulado + Dividendos mensais estimados
   - **30 Anos**: Patrimônio acumulado + Dividendos mensais estimados

### 4. **Recomendação de Alocação por Perfil**
   A ferramenta se ajusta automaticamente conforme o perfil de risco selecionado (atualmente: Moderado) e recomenda como distribuir o aporte mensal entre os seguintes tipos de FII:
   
   - **PAPEL**: Fundos imobiliários focados em papéis (malls, lojas)
   - **TIJOLO**: Fundos imobiliários focados em imóveis (salas comerciais, prédios)
   - **HÍBRIDOS**: Fundos que combinam diferentes tipos de ativos
   - **FOFs**: Fundos de Fundos (investem em outros fundos)
   - **DESENVOLVIMENTO**: Fundos focados em imóveis em desenvolvimento
   - **HOTELARIAS**: Fundos focados em propriedades hoteleiras

### 5. **Perfis de Risco Disponíveis**
   A tabela de apoio contém três perfis predefinidos com alocações diferentes:
   - **Conservador**: Maior foco em TIJOLO (50%) e PAPEL (30%)
   - **Moderado**: Distribuição equilibrada com TIJOLO (40%) e PAPEL (32%)
   - **Agressivo**: Maior diversificação com PAPEL (50%) e DESENVOLVIMENTO (20%)

## 📑 Estrutura da Planilha

### Aba 1: Controle de Investimento
- Contém todas as configurações, cálculos e simulações
- Layout intuitivo com seções bem definidas
- Uso de nomes (named ranges) para melhor organização

### Aba 2: Tabela de Apoio
- Tabela de referência com os perfis de risco
- Chaves compostas (PERFIL-TIPO_FII) para lookup automático
- Percentuais de alocação para cada combinação de perfil e tipo de FII

## 🔧 Como Usar

1. **Configurar os Parâmetros Iniciais**:
   - Altere o "Salário" em D10
   - Ajuste o "Rendimento Carteira" em D11 (taxa mensal esperada)
   - Modifique a "Taxa de rendimento mensal" em D17 conforme projeções

2. **Definir o Perfil de Risco**:
   - Selecione o perfil desejado em C28 (Conservador, Moderado ou Agressivo)

3. **Visualizar Resultados**:
   - Veja o patrimônio acumulado em D18
   - Acompanhe os dividendos mensais em D19
   - Analise os cenários de 2 a 30 anos nas linhas 22-26

4. **Consultar a Alocação Recomendada**:
   - Veja a distribuição do aporte mensal entre os tipos de FII nas linhas 32-37
   - A coluna C mostra o percentual recomendado
   - A coluna D mostra o valor em reais para cada tipo

## 💡 Exemplo de Uso

Com os valores padrão:
- Salário: R$ 2.000
- Aporte mensal sugerido (30%): R$ 600
- Período de investimento: 5 anos
- Taxa mensal: 1,079%

**Resultado esperado**:
- Patrimônio em 5 anos: ~R$ 39.900 (aproximadamente)
- Dividendos mensais: ~R$ 239
- Em 30 anos, você teria um patrimônio significativo com renda passiva considerável

## 📈 Fórmulas Utilizadas

- **FV (Future Value)**: Calcula o valor futuro de uma série de pagamentos regulares
- **VLOOKUP**: Busca os percentuais de alocação conforme perfil e tipo de FII
- **SUM**: Soma os totais dos percentuais e valores de alocação

## 🎓 Conceitos Financeiros

- **Aporte**: Investimento mensal realizado
- **Patrimônio Acumulado**: Soma de todos os aportes mais os rendimentos
- **Dividendos**: Renda passiva gerada pelo patrimônio
- **FII**: Fundo Imobiliário que permite investir em imóveis sem necessidade de capital elevado
- **Taxa de Rendimento**: Retorno mensal esperado do investimento

## 🚀 Potenciais Melhorias Futuras

- Adicionar mais perfis de risco personalizados
- Incluir histórico de aportes e retorno real vs. projetado
- Gráficos visuais do crescimento patrimonial
- Integração com dados de rendimento real de FIIs
- Cálculo de impostos e taxas

## 📝 Observações Importantes

- Esta ferramenta é para **fins educacionais e de planejamento pessoal**
- Os resultados são baseados em **projeções** e podem não refletir a realidade do mercado
- Taxa de rendimento utilizada é uma **estimativa** e pode variar significativamente
- Recomenda-se consultar um **assessor financeiro** antes de tomar decisões de investimento

---

**Última atualização**: Janeiro de 2026
