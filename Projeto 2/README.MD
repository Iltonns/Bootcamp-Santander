# 🏦 Sistema Bancário em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

Um sistema bancário completo via terminal com cadastro de clientes, contas correntes e operações financeiras básicas.

## ✨ Funcionalidades Principais

### 👤 Gestão de Usuários
- Cadastro com CPF, nome completo, data de nascimento e endereço
- Validação de CPF único
- Relacionamento 1:N entre usuários e contas

### 💳 Operações Bancárias
| Operação | Limites | Registro |
|----------|---------|----------|
| Depósito | Sem limites | Registrado no extrato |
| Saque | Limite diário (3) e por operação (R$500) | Registrado no extrato |
| Transferência | Validação de saldo | Registrada em ambas as contas |
| Extrato | Histórico completo | Com data e valor | Listagem de contas |

### 🏛️ Gestão de Contas
- Número de conta sequencial automático
- Agência fixa "0001"
- Saldo e extrato individual por conta

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-bancario.git

# Execute o programa
python sistema_bancario.py
