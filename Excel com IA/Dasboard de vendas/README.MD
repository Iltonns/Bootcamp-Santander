# Dashboard de Vendas XBOX Game Pass 📊

## 📋 Visão Geral

Um dashboard interativo e profissional desenvolvido em **Excel com Copilot**, que apresenta análises detalhadas sobre as vendas de assinaturas do **Xbox Game Pass**. O projeto combina dados de transações reais com visualizações gráficas intuitivas para facilitar a tomada de decisões estratégicas.

## 🎯 Objetivo

Analisar e visualizar dados de vendas de planos de assinatura Xbox Game Pass, incluindo diferentes tipos de planos, add-ons como EA Play e Minecraft Season Pass, informações de renovação automática e cálculo de receita total.

## 📁 Estrutura do Arquivo

O arquivo `Dashboard de Vendas XBOX.xlsx` é composto por **4 abas**:

### 1. **Assets** 🎨
- **Função**: Paleta de cores e elementos visuais do dashboard
- **Conteúdo**:
  - Definição da paleta de cores Xbox
  - Cores principais: Verde Xbox (#9BC848), Verde (#22C55E), Verde água (#2AE6B1), Verde claro (#5BF6A8)
  - Cores secundárias para indicadores negativos (#E8E6E9)
  - Estilos para menus e elementos visuais

### 2. **Bases** 📊
- **Função**: Base de dados bruta com informações de assinantes
- **Dimensões**: 296 linhas × 13 colunas
- **Colunas**:
  - `Subscriber ID`: Identificador único do assinante
  - `Name`: Nome do assinante
  - `Plan`: Tipo de plano (Core, Standard, Ultimate)
  - `Start Date`: Data de início da assinatura
  - `Auto Renewal`: Renovação automática (Yes/No)
  - `Subscription Price`: Preço da assinatura base
  - `Subscription Type`: Tipo de assinatura (Monthly, Quarterly, Annual)
  - `EA Play Season Pass`: Disponibilidade do serviço EA Play
  - `EA Play Season Pass Price`: Valor do EA Play
  - `Minecraft Season Pass`: Disponibilidade do Minecraft Pass
  - `Minecraft Season Pass Price`: Valor do Minecraft Pass
  - `Coupon Value`: Valor de desconto aplicado
  - `Total Value`: Valor total (receita bruta)

**Dados de Amostra**:
- 296 assinantes cadastrados
- Datas variando de janeiro a março de 2024
- Múltiplas combinações de planos e add-ons

### 3. **Cálculos** 📈
- **Função**: Análises e perguntas de negócio respondidas
- **Conteúdo**:
  - Respostas para perguntas estratégicas como:
    - "Qual o faturamento total de vendas de planos anuais?"
    - "Qual o faturamento separado por auto renovação?"
  - Tabelas dinâmicas com análises cruzadas
  - Agregações por tipo de assinatura
  - Cálculos de receita por segmento

**Exemplo de Análise**:
- Faturamento de planos anuais sem renovação automática: **R$ 3.847**

### 4. **Dashboard** 🎯
- **Função**: Visualização executiva e interativa
- **Conteúdo**:
  - Título: "XBOX GAME PASS SUBSCRIPTIONS SALES"
  - Gráficos e visualizações
  - KPIs principais
  - Análises visuais de vendas
  - Indicadores de desempenho

## 📊 Tipos de Dados Analisados

| Plano | Descrição | Preço Base |
|-------|-----------|-----------|
| **Core** | Plano básico | R$ 5 |
| **Standard** | Plano intermediário | R$ 10 |
| **Ultimate** | Plano premium com extras | R$ 15 |

## 💰 Add-ons Disponíveis

- **EA Play Season Pass**: Acesso a jogos EA (R$ 30)
- **Minecraft Season Pass**: Conteúdo exclusivo Minecraft (R$ 20)
- **Cupons de Desconto**: Redução adicional de valor

## 🔧 Tecnologias e Recursos

- **Microsoft Excel** com poder visual avançado
- **Copilot para Excel** para análises inteligentes
- **Tabelas Dinâmicas** para agregações de dados
- **Paleta de cores** profissional e coerente
- **Gráficos interativos** para exploração de dados

## 📊 Principais Métricas

- **Total de Assinantes**: 296 registros
- **Receita Total**: Agregação de todos os valores
- **Taxa de Renovação Automática**: Percentual de assinantes com renovação automática ativa
- **Receita por Tipo de Plano**: Breakdown entre Core, Standard e Ultimate
- **Faturamento por Add-on**: Impacto de EA Play e Minecraft Pass na receita

## 🎨 Design e Usabilidade

- Cores corporativas Xbox consistentes
- Layout limpo e profissional
- Fácil navegação entre abas
- Indicadores visuais claros
- Design responsivo para diferentes tamanhos de tela

## 👥 Público-Alvo

- **Analistas de Vendas**: Análise de performance de vendas
- **Gerentes de Produto**: Compreensão de adoção de planos
- **CFO/Finance**: Relatório de receita e faturamento
- **Executivos**: Dashboard executivo com KPIs principais

## 📝 Como Usar

1. **Navegar pelas abas**: Use as 4 abas para explorar dados brutos, cálculos e visualizações
2. **Interagir com o Dashboard**: Clique e explore os gráficos na aba Dashboard
3. **Analisar Cálculos**: Verifique as respostas para perguntas de negócio na aba Cálculos
4. **Referência de Cores**: Use a aba Assets como referência visual para manter consistência

## 🚀 Possíveis Melhorias

- Adicionar filtros interativos (Slicers)
- Criar gráficos comparativos por período
- Implementar previsões de receita
- Análise de churn (cancelamentos)
- Comparativo entre tipos de assinatura
- Análise de propensão a compra de add-ons

## 📅 Data do Projeto

Desenvolvido durante o **Bootcamp Santander - Excel com IA**

---

**Nota**: Este é um dashboard baseado em dados fictícios para fins educacionais e de análise de vendas de serviços de assinatura.
