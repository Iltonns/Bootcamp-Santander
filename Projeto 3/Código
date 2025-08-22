"""
SISTEMA BANCÁRIO EM PYTHON COM ORIENTAÇÃO A OBJETOS

Este sistema implementa um banco digital completo com as seguintes funcionalidades:
- Cadastro de clientes (pessoas físicas)
- Criação de contas correntes
- Operações de depósito e saque
- Histórico de transações
- Extrato bancário
- Sistema de logs para auditoria
- Validações de negócio (limites, número de transações, etc.)

Arquitetura:
- Cliente: Gerencia clientes e suas contas
- Conta: Classe base para contas bancárias
- ContaCorrente: Implementação específica de conta corrente
- Transacao: Sistema de transações (depósito e saque)
- Historico: Rastreamento de todas as operações
- ContasIterador: Padrão Iterator para listar contas
"""

import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
from pathlib import Path

# Define o caminho raiz para salvar arquivos de log
ROOT_PATH = Path(__file__).parent


class ContasIterador:
    """
    Implementa o padrão Iterator para percorrer a lista de contas
    Permite iterar sobre as contas de forma elegante
    """
    def __init__(self, contas):
        self.contas = contas
        self._index = 0  # Índice interno para controle da iteração

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            # Retorna uma string formatada com informações da conta
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            # Quando não há mais contas para iterar
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    """
    Classe base para representar um cliente do banco
    Gerencia informações pessoais e contas associadas
    """
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # Lista de contas do cliente
        self.indice_conta = 0  # Contador para controle de contas

    def realizar_transacao(self, conta, transacao):
        """
        Executa uma transação na conta do cliente
        Valida se não excedeu o limite diário de transações
        """
        # Limite de 2 transações por dia por conta
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Adiciona uma nova conta à lista de contas do cliente"""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Cliente pessoa física - herda de Cliente
    Representa clientes individuais com CPF
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Chama construtor da classe pai
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        """Representação string da pessoa física para debug"""
        return f"<{self.__class__.__name__}: ('{self.nome}', '{self.cpf}')>"


class Conta:
    """
    Classe base para contas bancárias
    Implementa funcionalidades básicas como saldo, depósito e saque
    """
    def __init__(self, numero, cliente):
        self._saldo = 0  # Saldo inicial zero (atributo privado)
        self._numero = numero
        self._agencia = "0001"  # Agência padrão
        self._cliente = cliente
        self._historico = Historico()  # Histórico de transações

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Método de classe para criar uma nova conta"""
        return cls(numero, cliente)

    # PROPRIEDADES (getters) para acessar atributos privados
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        """
        Realiza saque da conta
        Valida se há saldo suficiente e se o valor é positivo
        """
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        """
        Realiza depósito na conta
        Valida se o valor é positivo
        """
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    """
    Conta corrente - herda de Conta
    Implementa funcionalidades específicas como limite de saque e número máximo de saques
    """
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama construtor da classe pai
        self._limite = limite  # Limite de saque por operação
        self._limite_saques = limite_saques  # Número máximo de saques por dia

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        """Método de classe para criar uma nova conta corrente"""
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        """
        Sobrescreve o método sacar da classe pai
        Adiciona validações específicas da conta corrente
        """
        # Conta quantos saques já foram feitos hoje
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            # Chama o método sacar da classe pai se todas as validações passarem
            return super().sacar(valor)

        return False

    def __repr__(self):
        """Representação string da conta para debug"""
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

    def __str__(self):
        """Representação string amigável da conta para o usuário"""
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    """
    Gerencia o histórico de transações de uma conta
    Armazena todas as operações com data, hora e tipo
    """
    def __init__(self):
        self._transacoes = []  # Lista de transações

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma nova transação ao histórico
        Registra tipo, valor e data/hora da operação
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Nome da classe da transação
                "valor": transacao.valor,
                "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        """
        Gera relatório das transações
        Pode filtrar por tipo específico (depósito, saque)
        """
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        """
        Retorna apenas as transações realizadas hoje
        Usado para validar limite diário de operações
        """
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao(ABC):
    """
    Classe abstrata para transações bancárias
    Define interface que deve ser implementada por todas as transações
    """
    @property
    @abstractproperty
    def valor(self):
        """Propriedade abstrata para o valor da transação"""
        pass

    @abstractclassmethod
    def registrar(self, conta):
        """Método abstrato para registrar a transação na conta"""
        pass


class Saque(Transacao):
    """
    Transação de saque - herda de Transacao
    Implementa a lógica específica para saques
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """
        Registra o saque na conta
        Só adiciona ao histórico se a operação for bem-sucedida
        """
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """
    Transação de depósito - herda de Transacao
    Implementa a lógica específica para depósitos
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """
        Registra o depósito na conta
        Só adiciona ao histórico se a operação for bem-sucedida
        """
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    """
    Decorator para registrar logs de todas as operações
    Salva informações sobre execução de funções em arquivo de log
    """
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        
        # Escreve no arquivo de log
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(
                f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. "
                f"Retornou {resultado}\n"
            )
        return resultado

    return envelope


def menu():
    """
    Exibe o menu principal do sistema
    Retorna a opção escolhida pelo usuário
    """
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    """
    Busca um cliente pelo CPF na lista de clientes
    Retorna o cliente encontrado ou None se não existir
    """
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    """
    Recupera a primeira conta do cliente
    TODO: Implementar seleção de conta quando cliente tiver múltiplas contas
    """
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    """
    Função para realizar depósito
    Decorada com @log_transacao para registrar logs
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    """
    Função para realizar saque
    Decorada com @log_transacao para registrar logs
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes):
    """
    Função para exibir extrato bancário
    Mostra histórico de transações e saldo atual
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    
    # Itera sobre o histórico de transações
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


@log_transacao
def criar_cliente(clientes):
    """
    Função para criar novo cliente
    Coleta dados pessoais e cria instância de PessoaFisica
    """
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    """
    Função para criar nova conta
    Associa conta ao cliente e adiciona às listas de contas
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    # Cria conta corrente com limite de R$ 500 e 50 saques por dia
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    """
    Lista todas as contas usando o iterador personalizado
    Exibe informações formatadas de cada conta
    """
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    """
    Função principal do sistema
    Loop infinito que processa as opções do menu
    """
    clientes = []  # Lista para armazenar todos os clientes
    contas = []    # Lista para armazenar todas as contas

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
