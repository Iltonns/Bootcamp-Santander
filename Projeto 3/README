# 🏦 Sistema Bancário em Python — Orientado a Objetos

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

Um sistema bancário completo via terminal, desenvolvido com foco em Programação Orientada a Objetos (POO). O projeto utiliza classes para representar clientes, contas e operações, promovendo organização, reuso e fácil manutenção do código.

## ✨ Principais Implementações em POO

### 🧩 Estrutura de Classes

- **Cliente**: Armazena dados pessoais (CPF, nome, data de nascimento, endereço) e gerencia suas contas.
- **ContaCorrente**: Representa uma conta bancária, com número sequencial, agência fixa, saldo, extrato e métodos para operações financeiras.
- **Operações**: Métodos encapsulados para depósito, saque, transferência e geração de extrato.
- **Banco**: Responsável pelo cadastro de clientes, criação de contas e validações.

### 👤 Gestão de Usuários
- Cadastro de clientes com CPF único, utilizando métodos de validação.
- Relacionamento 1:N entre clientes e contas, implementado via composição de objetos.

### 💳 Operações Bancárias
| Operação      | Limites e Validações (via métodos) | Registro (POO)         |
|---------------|------------------------------------|------------------------|
| Depósito      | Sem limites                        | Método da classe Conta |
| Saque         | Limite diário (3) e por operação   | Método da classe Conta |
| Transferência | Validação de saldo                 | Método da classe Conta |
| Extrato       | Histórico completo                 | Lista de operações     |

### 🏛️ Gestão de Contas
- Número de conta gerado automaticamente por atributo de classe.
- Agência fixa "0001".
- Saldo e extrato individual, encapsulados em cada instância de ContaCorrente.

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-bancario.git

# Execute o programa
python sistema_bancario.py
```

---

Este projeto demonstra os princípios da Programação Orientada a Objetos aplicados a um sistema bancário realista, facilitando futuras expansões e manutenções.
