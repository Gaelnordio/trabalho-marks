import pywhatkit


# =========================
# CLASSE PESSOA
# =========================

class Pessoa:

    def __init__(self, nome, idade, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def telefone(self):
        return self.__telefone

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Telefone:", self.telefone)


# =========================
# PACIENTE
# (HERANÇA + POLIMORFISMO)
# =========================

class Paciente(Pessoa):

    def __init__(self, id, nome, idade, telefone, endereco):
        super().__init__(nome, idade, telefone)

        self.__id = id
        self.__endereco = endereco

    @property
    def id(self):
        return self.__id

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, valor):
        self.__endereco = valor

    # POLIMORFISMO (OVERRIDING)

    def exibir_dados(self):

        print("\n===== PACIENTE =====")
        print("ID:", self.id)

        super().exibir_dados()

        print("Endereço:", self.endereco)


# =========================
# CONSULTA
# =========================

class Consulta:

    def __init__(self, paciente, data, horario, motivo):

        self.__paciente = paciente
        self.__data = data
        self.__horario = horario
        self.__motivo = motivo
        self.__status = "A confirmar"

    @property
    def paciente(self):
        return self.__paciente

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def motivo(self):
        return self.__motivo

    @property
    def status(self):
        return self.__status

    def confirmar(self):
        self.__status = "Confirmada"

    def cancelar(self):
        self.__status = "Cancelada"

    def exibir(self):

        print("\nPaciente:", self.paciente.nome)
        print("Data:", self.data)
        print("Horário:", self.horario)
        print("Motivo:", self.motivo)
        print("Status:", self.status)


# =========================
# SISTEMA
# =========================

class SistemaPosto:

    def __init__(self):

        self.__pacientes = []
        self.__consultas = []

    # ---------------------

    def cadastrar_paciente(self):

        nome = input("Nome: ")
        idade = input("Idade: ")
        telefone = input("WhatsApp (+5511999999999): ")
        endereco = input("Endereço: ")

        paciente = Paciente(

            len(self.__pacientes) + 1,

            nome,

            idade,

            telefone,

            endereco

        )

        self.__pacientes.append(paciente)

        print("\nPaciente cadastrado com sucesso!")

    # ---------------------

    def procurar_paciente(self, id):

        for paciente in self.__pacientes:

            if paciente.id == id:
                return paciente

        return None

    # ---------------------

    def listar_pacientes(self):

        if len(self.__pacientes) == 0:

            print("Nenhum paciente cadastrado.")
            return

        print("\n===== PACIENTES =====")

        for paciente in self.__pacientes:

            paciente.exibir_dados()

    # ---------------------

    def area_paciente(self):

        telefone = input("Digite seu WhatsApp: ")

        for paciente in self.__pacientes:

            if paciente.telefone == telefone:

                paciente.exibir_dados()

                print("\n===== CONSULTAS =====")

                encontrou = False

                for consulta in self.__consultas:

                    if consulta.paciente.id == paciente.id:

                        consulta.exibir()

                        encontrou = True

                if not encontrou:

                    print("Nenhuma consulta encontrada.")

                return

        print("Telefone não encontrado.")

    # ---------------------

    def agendar_consulta(self):

        try:

            id_paciente = int(input("ID do paciente: "))

        except:

            print("ID inválido.")

            return

        paciente = self.procurar_paciente(id_paciente)

        if paciente is None:

            print("Paciente não encontrado.")

            return

        data = input("Data(dd/mm/aaaa): ")
        horario = input("Horário(hh:mm): ")
        motivo = input("Motivo: ")

        consulta = Consulta(

            paciente,

            data,

            horario,

            motivo

        )

        self.__consultas.append(consulta)

        print("Consulta cadastrada.")

    # ---------------------

    def listar_consultas(self):

        if len(self.__consultas) == 0:

            print("Nenhuma consulta cadastrada.")
            return

        print("\n===== CONSULTAS =====")

        for consulta in self.__consultas:

            consulta.exibir()

    # ---------------------

    def confirmar_consulta(self):

        try:
            id_paciente = int(input("ID do paciente: "))
        except:
            print("ID inválido.")
            return

        for consulta in self.__consultas:

            if consulta.paciente.id == id_paciente:

                consulta.confirmar()

                print("Consulta confirmada!")

                return

        print("Consulta não encontrada.")

    # ---------------------

    def cancelar_consulta(self):

        try:
            id_paciente = int(input("ID do paciente: "))
        except:
            print("ID inválido.")
            return

        for consulta in self.__consultas:

            if consulta.paciente.id == id_paciente:

                consulta.cancelar()

                print("Consulta cancelada!")

                return

        print("Consulta não encontrada.")

    # ---------------------

    def enviar_lembrete(self):

        try:
            id_paciente = int(input("ID do paciente: "))
        except:
            print("ID inválido.")
            return

        for consulta in self.__consultas:

            if consulta.paciente.id == id_paciente:

                mensagem = (
                    f"Olá {consulta.paciente.nome}!\n\n"
                    f"Lembramos que sua consulta está marcada para:\n"
                    f"Data: {consulta.data}\n"
                    f"Horário: {consulta.horario}\n"
                    f"Motivo: {consulta.motivo}\n\n"
                    f"Posto de Saúde do Bairro."
                )

                try:

                    pywhatkit.sendwhatmsg_instantly(

                        consulta.paciente.telefone,

                        mensagem,

                        wait_time=30,

                        tab_close=True

                    )

                    print("Mensagem enviada com sucesso!")

                except Exception as erro:

                    print("Erro ao enviar mensagem.")

                    print(erro)

                return

        print("Consulta não encontrada.")

    # ---------------------

    def relatorio(self):

        print("\n===== RELATÓRIO =====")

        print("Pacientes cadastrados:", len(self.__pacientes))

        print("Consultas agendadas:", len(self.__consultas))


# =====================================
# PROGRAMA PRINCIPAL
# =====================================

sistema = SistemaPosto()

while True:

    print("\n================================")
    print(" SISTEMA POSTO DE SAÚDE")
    print("================================")
    print("1 - Cadastrar paciente")
    print("2 - Consultas do paciente")
    print("3 - Listar pacientes")
    print("4 - Agendar consulta")
    print("5 - Listar consultas")
    print("6 - Confirmar consulta")
    print("7 - Cancelar consulta")
    print("8 - Enviar lembrete WhatsApp")
    print("9 - Relatório")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        sistema.cadastrar_paciente()

    elif opcao == "2":

        sistema.area_paciente()

    elif opcao == "3":

        sistema.listar_pacientes()

    elif opcao == "4":

        sistema.agendar_consulta()

    elif opcao == "5":

        sistema.listar_consultas()

    elif opcao == "6":

        sistema.confirmar_consulta()

    elif opcao == "7":

        sistema.cancelar_consulta()

    elif opcao == "8":

        sistema.enviar_lembrete()

    elif opcao == "9":

        sistema.relatorio()

    elif opcao == "0":

        print("Sistema encerrado.")

        break

    else:

        print("Opção inválida.")
