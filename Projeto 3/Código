# Importações necessárias para o sistema bancário
import textwrap  # Para formatação de texto
from abc import ABC, abstractclassmethod, abstractproperty  # Para classes abstratas
from datetime import datetime  # Para manipulação de data e hora


class ContasIterador:
    """
    Classe iteradora personalizada para percorrer as contas bancárias
    e exibir informações formatadas de cada conta.
    """
    def __init__(self, contas):
        # Lista de contas a serem iteradas
        self.contas = contas
        # Índice atual para controle da iteração
        self._index = 0

    def __iter__(self):
        # Retorna o próprio objeto para permitir iteração
        return self

    def __next__(self):
        try:
            # Obtém a conta atual pelo índice
            conta = self.contas[self._index]
            # Retorna uma string formatada com informações da conta
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            # Quando não há mais contas, para a iteração
            raise StopIteration
        finally:
            # Sempre incrementa o índice para próxima iteração
            self._index += 1


class Cliente:
    """
    Classe base para representar um cliente do banco.
    Pode ser uma pessoa física ou jurídica.
    """
    def __init__(self, endereco):
        # Endereço do cliente
        self.endereco = endereco
        # Lista de contas associadas ao cliente
        self.contas = []
        # Contador para controle de contas
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        """
        Executa uma transação na conta do cliente.
        Verifica se não excedeu o limite diário de transações.
        """
        # Verifica se já foram feitas 2 ou mais transações hoje
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return

        # Registra a transação na conta
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Adiciona uma nova conta à lista de contas do cliente."""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Classe que representa um cliente pessoa física.
    Herda da classe Cliente e adiciona informações específicas.
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Chama o construtor da classe pai (Cliente)
        super().__init__(endereco)
        # Nome completo da pessoa
        self.nome = nome
        # Data de nascimento no formato dd-mm-aaaa
        self.data_nascimento = data_nascimento
        # CPF (Cadastro de Pessoa Física)
        self.cpf = cpf


class Conta:
    """
    Classe base para representar uma conta bancária.
    Define funcionalidades básicas como depósito e saque.
    """
    def __init__(self, numero, cliente):
        # Saldo inicial da conta (privado)
        self._saldo = 0
        # Número da conta (privado)
        self._numero = numero
        # Agência padrão (privado)
        self._agencia = "0001"
        # Cliente proprietário da conta (privado)
        self._cliente = cliente
        # Histórico de transações da conta (privado)
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Método de classe para criar uma nova conta."""
        return cls(numero, cliente)

    # Propriedades para acessar atributos privados
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
        Realiza um saque na conta.
        Retorna True se o saque foi bem-sucedido, False caso contrário.
        """
        saldo = self.saldo
        # Verifica se o valor do saque excede o saldo disponível
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            # Deduz o valor do saldo
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        """
        Realiza um depósito na conta.
        Retorna True se o depósito foi bem-sucedido, False caso contrário.
        """
        if valor > 0:
            # Adiciona o valor ao saldo
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente.
    Herda da classe Conta e adiciona funcionalidades específicas como limite de saque.
    """
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Chama o construtor da classe pai (Conta)
        super().__init__(numero, cliente)
        # Limite de valor para saque (privado)
        self._limite = limite
        # Limite de quantidade de saques (privado)
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        """Método de classe para criar uma nova conta corrente."""
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        """
        Sobrescreve o método sacar da classe pai.
        Adiciona validações específicas para conta corrente.
        """
        # Conta quantos saques já foram feitos
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        # Verifica se excedeu o limite de valor para saque
        excedeu_limite = valor > self._limite
        # Verifica se excedeu o limite de quantidade de saques
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            # Se passou nas validações, chama o método da classe pai
            return super().sacar(valor)

        return False

    def __str__(self):
        """Retorna uma representação em string da conta corrente."""
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    """
    Classe para gerenciar o histórico de transações de uma conta.
    Armazena e permite consultar todas as transações realizadas.
    """
    def __init__(self):
        # Lista de transações (privada)
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma nova transação ao histórico.
        Registra tipo, valor e data/hora da transação.
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Nome da classe da transação
                "valor": transacao.valor,  # Valor da transação
                "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"),  # Data/hora atual
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        """
        Gera um relatório das transações.
        Se tipo_transacao for especificado, filtra apenas transações desse tipo.
        """
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        """
        Retorna apenas as transações realizadas no dia atual.
        Útil para controle de limite diário de transações.
        """
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            # Converte a string de data para objeto datetime
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()
            # Se a data da transação for igual à data atual
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao(ABC):
    """
    Classe abstrata que define a interface para transações bancárias.
    Todas as transações devem implementar os métodos abstratos.
    """
    @property
    @abstractproperty
    def valor(self):
        """Propriedade abstrata que deve retornar o valor da transação."""
        pass

    @abstractclassmethod
    def registrar(self, conta):
        """Método abstrato que deve registrar a transação na conta."""
        pass


class Saque(Transacao):
    """
    Classe que representa uma transação de saque.
    Implementa a interface Transacao.
    """
    def __init__(self, valor):
        # Valor a ser sacado (privado)
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do saque."""
        return self._valor

    def registrar(self, conta):
        """
        Registra o saque na conta.
        Só adiciona ao histórico se o saque for bem-sucedido.
        """
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """
    Classe que representa uma transação de depósito.
    Implementa a interface Transacao.
    """
    def __init__(self, valor):
        # Valor a ser depositado (privado)
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do depósito."""
        return self._valor

    def registrar(self, conta):
        """
        Registra o depósito na conta.
        Só adiciona ao histórico se o depósito for bem-sucedido.
        """
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    """
    Decorador para registrar logs de transações.
    Registra a data/hora e nome da função executada.
    """
    def envelope(*args, **kwargs):
        # Executa a função original
        resultado = func(*args, **kwargs)
        # Registra o log com timestamp
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope


def menu():
    """
    Exibe o menu principal do sistema bancário.
    Retorna a opção escolhida pelo usuário.
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
    Busca um cliente na lista pelo CPF.
    Retorna o cliente encontrado ou None se não existir.
    """
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    """
    Recupera a primeira conta de um cliente.
    Retorna None se o cliente não tiver contas.
    """
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    """
    Função para realizar depósito.
    Solicita CPF do cliente e valor, então executa o depósito.
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
    Função para realizar saque.
    Solicita CPF do cliente e valor, então executa o saque.
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
    Função para exibir o extrato de uma conta.
    Mostra todas as transações e o saldo atual.
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
    # Itera sobre todas as transações do histórico
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
    Função para criar um novo cliente.
    Solicita dados pessoais e cria uma instância de PessoaFisica.
    """
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    """
    Função para criar uma nova conta.
    Associa a conta ao cliente e adiciona às listas de contas.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    # Cria uma nova conta corrente com limites padrão
    conta = ContaCorrente.nova_conta(
        cliente=cliente, numero=numero_conta, limite=500, limite_saques=50
    )
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    """
    Função para listar todas as contas cadastradas.
    Usa o iterador personalizado para exibir informações formatadas.
    """
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    """
    Função principal do sistema bancário.
    Inicializa as listas e executa o loop principal do menu.
    """
    # Listas para armazenar clientes e contas
    clientes = []
    contas = []

    # Loop principal do sistema
    while True:
        opcao = menu()

        # Processa a opção escolhida pelo usuário
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
            # Sai do loop e encerra o programa
            break

        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
            )


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
