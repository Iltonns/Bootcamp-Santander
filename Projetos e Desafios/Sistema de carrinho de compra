"""Crie um sistema de carrinho de compra que permita adicionar produtos e calcular o valor total da compra.

# CÓDIGO SUGERIDO PELA DIO

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# Exibe os itens do carrinho
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# Exibe o total da compra
print(f"Total: R${total:.2f}")"""


# CÓDIGO COM MELHORIAS IMPLEMENTADAS

# Melhorias sugeridas:
# 1. Validar a entrada do usuário para evitar erros em caso de dados inválidos.
# 2. Permitir remover itens do carrinho, se desejado.
# 3. Utilizar funções para modularizar o código.
# 4. Adicionar tratamento de exceções para conversão de preço.
# 5. Permitir adicionar quantidades para cada produto.
# 6. Exibir uma mensagem amigável caso o carrinho esteja vazio.


import os

def limpar_tela():
    """Limpa a tela do console de acordo com o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")

def imprimir_titulo(texto):
    """Imprime um título formatado com linhas de separação.
    
    Args:
        texto (str): O texto a ser exibido como título.
    """
    print("=" * 40)
    print(f"{texto:^40}")  # Centraliza o texto em 40 caracteres
    print("=" * 40)

def adicionar_item(carrinho):
    """Adiciona um item ao carrinho de compras.
    
    Solicita ao usuário os detalhes do produto (nome, preço e quantidade),
    valida os dados e adiciona ao carrinho se estiverem corretos.
    
    Args:
        carrinho (list): Lista de dicionários contendo os itens do carrinho.
    """
    while True:
        try:
            # Solicita os dados do produto em uma única linha
            linha = input("Digite o produto, preço e quantidade (ex: 'Arroz 10.50 2'): ").strip()
            if not linha:
                print("Entrada vazia. Tente novamente.")
                continue

            # Divide a entrada em partes (nome, preço, quantidade)
            partes = linha.rsplit(" ", 2)
            if len(partes) != 3:
                print("Formato inválido. Use: nome preço quantidade")
                continue

            nome, preco_str, qtd_str = partes
            
            # Converte preço para float (suportando tanto '.' quanto ',' como separador decimal)
            preco = float(preco_str.replace(",", "."))
            quantidade = int(qtd_str)

            # Valida preço e quantidade
            if preco < 0 or quantidade <= 0:
                print("Preço deve ser positivo e quantidade maior que zero.")
                continue

            # Adiciona o produto ao carrinho como um dicionário
            carrinho.append({"nome": nome, "preco": preco, "quantidade": quantidade})
            print(f"\n✅ Produto '{nome}' adicionado com sucesso!")
            break
        except ValueError:
            print("❌ Preço ou quantidade inválidos. Tente novamente.")

def remover_item(carrinho):
    """Remove um item do carrinho de compras.
    
    Solicita o nome do produto a ser removido e o remove do carrinho se encontrado.
    
    Args:
        carrinho (list): Lista de dicionários contendo os itens do carrinho.
    """
    if not carrinho:
        print("⚠️ Carrinho vazio. Nada para remover.")
        return
    
    nome = input("Digite o nome do produto a remover: ").strip()
    
    # Procura o produto no carrinho (comparação case-insensitive)
    for i, item in enumerate(carrinho):
        if item["nome"].lower() == nome.lower():
            carrinho.pop(i)  # Remove o item encontrado
            print(f"✅ Produto '{nome}' removido do carrinho.")
            return
    
    print(f"❌ Produto '{nome}' não encontrado no carrinho.")

def exibir_carrinho(carrinho):
    """Exibe o conteúdo atual do carrinho de compras com formatação.
    
    Mostra todos os itens, seus preços, quantidades e subtotais, além do total geral.
    
    Args:
        carrinho (list): Lista de dicionários contendo os itens do carrinho.
    """
    if not carrinho:
        print("🛒 Seu carrinho está vazio!")
        return

    imprimir_titulo("Itens no Carrinho")
    total = 0.0
    
    # Exibe cada item com alinhamento formatado
    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        print(f"{item['nome']:<20} R${item['preco']:>6.2f} x {item['quantidade']:<3} = R${subtotal:>7.2f}")
        total += subtotal
    
    # Exibe o total geral
    print("-" * 40)
    print(f"{'TOTAL':<30} R${total:>7.2f}")
    print("=" * 40)

def main():
    """Função principal que gerencia o fluxo do programa."""
    carrinho = []  # Inicializa o carrinho como uma lista vazia
    
    while True:
        imprimir_titulo("MENU PRINCIPAL")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Exibir carrinho")
        print("4 - Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        limpar_tela()

        if escolha == "1":
            imprimir_titulo("Adicionar Produto")
            adicionar_item(carrinho)
        elif escolha == "2":
            imprimir_titulo("Remover Produto")
            remover_item(carrinho)
        elif escolha == "3":
            exibir_carrinho(carrinho)
        elif escolha == "4":
            print("\n✅ Saindo do sistema. Obrigado por usar o carrinho!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
