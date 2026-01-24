# 🎓 Bootcamp Santander - Projetos e Desafios

Este repositório contém os projetos desenvolvidos durante o **Bootcamp Santander**, demonstrando a evolução técnica ao longo do programa. Aqui você encontrará exemplos práticos, desafios resolvidos e implementações de conceitos de desenvolvimento de software, ciência de dados e análise com ferramentas modernas.

---

## 📑 Sumário

1. [Back-End com Python](#back-end-com-python)
2. [Ciência de Dados](#ciência-de-dados)
3. [Excel com IA](#excel-com-ia)
4. [Como Usar](#como-usar)
5. [Ferramentas Utilizadas](#ferramentas-utilizadas)

---

## 🔧 Back-End com Python

Projetos focados em desenvolvimento de sistemas completos com Python, aplicando conceitos de programação procedural e orientada a objetos.

### 🏦 Sistema Bancário em Python
**Pasta**: `Back-End com Python/Sistema Bancario Simples em Python/`

Um sistema bancário completo via terminal com:
- 👤 **Gestão de Usuários**: Cadastro com validação de CPF único
- 💳 **Operações Bancárias**: Depósito, saque (limite de 3/dia e R$500 por operação), transferência e extrato
- 📋 **Relatórios**: Histórico completo de transações
- 🏛️ **Gestão de Contas**: Número de conta sequencial automático e agência fixa

**Tecnologias**: Python 3.x

---

### 🏦 Sistema Bancário em Python — Orientado a Objetos
**Pasta**: `Back-End com Python/Sistema Bancario Orientado a Objetos/`

Versão avançada do sistema bancário desenvolvida com foco em **Programação Orientada a Objetos (POO)**:

#### 🧩 Estrutura de Classes
- **Cliente**: Dados pessoais e gerenciamento de contas
- **ContaCorrente**: Representação de contas bancárias com operações encapsuladas
- **Banco**: Cadastro de clientes e validações centralizadas

#### ✨ Recursos Avançados
- **Decoradores**: Validação de operações e autenticação
- **Iteradores**: Navegação eficiente em listas de contas e operações
- **Geradores**: Criação de extratos e relatórios sob demanda

**Tecnologias**: Python 3.x, POO, Decoradores, Iteradores, Geradores

---

### 🛍️ Sistema de Carrinho de Compras em Python
**Pasta**: `Back-End com Python/Sistema de Carrinho de compra em Python/`

Sistema interativo de carrinho de compras com:
- ➕ **Adição de itens**: Cadastro de produtos com nome, preço e quantidade
- ✖️ **Remoção de itens**: Remoção case insensitive
- 📋 **Visualização**: Lista formatada com subtotais e total geral
- ✅ **Validação**: Verificação de preços e quantidades
- 🖥️ **Interface**: Menu interativo com limpeza de tela

**Tecnologias**: Python 3.x

---

## 📊 Ciência de Dados

Projetos focados em análise de dados, pipelines ETL, machine learning e cloud computing.

### 📊 Análise de Dados com Excel
**Pasta**: `Ciência de dados/Análise de dados com excel/`

**Dashboard de Vendas XBOX** — Dashboard interativo para análise de vendas:
- 📈 **Visualizações**: Gráficos de desempenho e tendências
- 🔄 **Funcionalidades**: Tabelas dinâmicas, segmentações (Slicers) e filtros interativos
- 💡 **Análise**: KPIs, comparação entre períodos e identificação de produtos mais vendidos
- 📋 **Formatação**: Formatação condicional e design intuitivo

**Ferramentas**: Microsoft Excel 2016+, Tabelas Dinâmicas, Fórmulas Avançadas, Formatação Condicional

---

### 🔄 Pipeline ETL com Python
**Pasta**: `Ciência de dados/Pipeline ETL com Python/`

Projeto implementando um pipeline completo de **Extração, Transformação e Carregamento**:

#### 📥 EXTRACT
- Leitura de dados do arquivo JSON (`clientes.json`)
- Extração de IDs de usuários para processamento

#### 🔄 TRANSFORM
- Utilização de **IA Generativa (OpenAI GPT-4)** para gerar mensagens de marketing personalizadas
- Processamento e enriquecimento de dados com base em perfil de usuário
- Alternativa sem API para fins educacionais

#### 📤 LOAD
- Carregamento dos dados transformados no sistema
- Estruturação para posterior utilização em APIs

**Tecnologias**: Python, Pandas, OpenAI API, JSON, Jupyter Notebook

---

### ☁️ Implementação de Serviços AWS
**Pasta**: `Ciência de dados/Projeto AWS/`

Projeto de implementação de serviços AWS para otimização de infraestrutura na empresa Abstergo Industries:

#### 🚀 Serviços Implementados

1. **Amazon EC2 Auto Scaling**
   - 📉 Redução de custos em 60% nos horários de baixo tráfego
   - ⚙️ Métricas de CPU e memória para otimização automática

2. **Amazon S3 Intelligent-Tiering**
   - 💾 Movimentação automática entre camadas de armazenamento
   - 📊 Redução de 45% nos custos de armazenamento

3. **AWS Lambda com API Gateway**
   - ⚡ Arquitetura serverless para eliminação de ociosidade
   - 🔗 Migração de microsserviços com redução de 55% em custos

**Resultado**: Redução de aproximadamente 53% nos custos operacionais

**Tecnologias**: AWS EC2, S3, Lambda, API Gateway, Cloud Computing

---

### 🧠 Deep Learning do Zero em Python
**Pasta**: `Ciência de dados/Deep Learning do Zero em Python/`

Implementação de conceitos de **Deep Learning** do zero em Python, demonstrando a compreensão teórica e prática de redes neurais artificiais.

**Tecnologias**: Python, NumPy, TensorFlow/PyTorch (conforme implementação)

---

## 📈 Excel com IA

Projetos integrando IA e análise avançada em planilhas Excel.

### 💰 Ferramenta de Controle de Investimentos
**Pasta**: `Excel com IA/Ferramenta de Controle de Investimentos/`

Planilha Excel interativa para análise de investimentos em **Fundos Imobiliários (FII)**:

#### 🎯 Funcionalidades Principais
- 💵 **Cálculo de Investimento**: Baseado em porcentagem do salário (padrão 30%)
- 📊 **Simulação de Cenários**: Patrimônio acumulado em 2, 5, 10, 20 e 30 anos
- 💎 **Estimativa de Dividendos**: Cálculo de renda passiva mensal
- 🎲 **Perfis de Risco**: Conservador, Moderado e Agressivo
- 📍 **Alocação de Ativos**: Recomendação automática entre tipos de FII (PAPEL, TIJOLO, HÍBRIDOS, FOFs, DESENVOLVIMENTO, HOTELARIAS)

#### 📋 Seções da Planilha
1. **Configurações Iniciais**: Salário, rendimento esperado, sugestão de investimento
2. **Cálculos**: Aporte mensal, patrimônio acumulado, dividendos
3. **Análise de Cenários**: Simulações para diferentes períodos
4. **Recomendação de Alocação**: Distribuição por tipo de FII conforme perfil

**Fórmulas Utilizadas**: FV (Future Value), VLOOKUP, IF, Nomes (Named Ranges)

**Ferramentas**: Microsoft Excel, Funções Financeiras Avançadas

---

### 📊 Outros Projetos Excel
**Pasta**: `Excel com IA/`

Diversos projetos com Excel avançado:
- 📈 **Análise de Dados com Excel e Copilot**: Integração com IA do Copilot
- 🎯 **Criando um Dashboard de Vendas**: Dashboard de análise de vendas
- 🎮 **Dashboard de Vendas XBOX**: Análise específica de produtos XBOX
- 📋 **Declaração de Imposto de Renda**: Ferramenta fiscal
- 📊 **Trabalhando com Tabelas Dinâmicas**: Análise avançada de dados
- ⚙️ **Formatações Condicionais**: Técnicas visuais avançadas

---

## 🚀 Como Usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/Projetos-e-Desafios-Bootcamp-Santander.git
cd Projetos-e-Desafios-Bootcamp-Santander
```

### 2. Navegue até o projeto desejado
```bash
cd "Back-End com Python/Sistema Bancario Simples em Python/Codigo"
# ou
cd "Excel com IA/Ferramenta de Controle de Investimentos"
```

### 3. Siga as instruções específicas do README do projeto

---

## 🛠️ Ferramentas Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e sugestões.

## 👤 Autor

Desenvolvido como parte dos projetos e desafios do **Bootcamp Santander**

---

**Última atualização**: 24 de janeiro de 2026
