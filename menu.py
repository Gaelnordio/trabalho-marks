import pywhatkit

pacientes = []
consultas = []

def cadastrar_paciente():

    id_paciente = len(pacientes) + 1

    nome = input("Nome: ")
    idade = input("Idade: ")
    telefone = input("WhatsApp (+5511999999999): ")
    endereco = input("Endereço: ")

    paciente = {
        "id": id_paciente,
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "endereco": endereco
    }

    pacientes.append(paciente)

    print("\nPaciente cadastrado com sucesso!")
    print("ID:", id_paciente)


def area_paciente():

    telefone = input("Digite seu WhatsApp: ")

    for p in pacientes:

        if p["telefone"] == telefone:

            print("\n===== DADOS DO PACIENTE =====")
            print("ID:", p["id"])
            print("Nome:", p["nome"])
            print("Idade:", p["idade"])
            print("Telefone:", p["telefone"])
            print("Endereço:", p["endereco"])

            print("\n===== CONSULTAS =====")

            encontrou = False

            for c in consultas:

                if c["id_paciente"] == p["id"]:

                    print("\nData:", c["data"])
                    print("Horário:", c["horario"])
                    print("Motivo:", c["motivo"])

                    encontrou = True

            if not encontrou:
                print("Nenhuma consulta agendada.")

            return

    print("Telefone não encontrado.")


def listar_pacientes():

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    print("\n===== PACIENTES =====")

    for p in pacientes:

        print("\nID:", p["id"])
        print("Nome:", p["nome"])
        print("Telefone:", p["telefone"])


def agendar_consulta():

    try:
        id_paciente = int(input("ID do paciente: "))
    except:
        print("ID inválido.")
        return

    paciente = None

    for p in pacientes:

        if p["id"] == id_paciente:
            paciente = p
            break

    if paciente is None:
        print("Paciente não encontrado.")
        return

    data = input("Data (dd/mm/aaaa): ")
    horario = input("Horário (hh:mm): ")
    motivo = input("Motivo da consulta: ")

    consultas.append({
        "id_paciente": paciente["id"],
        "nome": paciente["nome"],
        "telefone": paciente["telefone"],
        "data": data,
        "horario": horario,
        "motivo": motivo
    })

    print("Consulta agendada com sucesso!")


def listar_consultas():

    if len(consultas) == 0:
        print("Nenhuma consulta cadastrada.")
        return

    print("\n===== CONSULTAS =====")

    for c in consultas:

        print("\nPaciente:", c["nome"])
        print("Data:", c["data"])
        print("Horário:", c["horario"])
        print("Motivo:", c["motivo"])


def enviar_lembrete():

    try:
        id_paciente = int(input("ID do paciente: "))
    except:
        print("ID inválido.")
        return

    for c in consultas:

        if c["id_paciente"] == id_paciente:

            mensagem = (
                f"Olá {c['nome']}!\n\n"
                f"Lembramos que sua consulta está marcada para:\n"
                f"Data: {c['data']}\n"
                f"Horário: {c['horario']}\n"
                f"Motivo da consulta: {c['motivo']}\n\n"
                f"Posto de Saúde do Bairro."
            )

            try:

                pywhatkit.sendwhatmsg_instantly(
                    c["telefone"],
                    mensagem,
                    wait_time=15,
                    tab_close=True
                    
                )

                print("Mensagem enviada com sucesso!")

            except Exception as erro:

                print("Erro ao enviar mensagem:")
                print(erro)

            return

    print("Consulta não encontrada.")


def relatorio():

    print("\n===== RELATÓRIO =====")
    print("Pacientes cadastrados:", len(pacientes))
    print("Consultas agendadas:", len(consultas))


while True:

    print("\n================================")
    print(" SISTEMA POSTO DE SAÚDE")
    print("================================")
    print("1 - Cadastrar paciente")
    print("2 - Área do paciente")
    print("3 - Listar pacientes")
    print("4 - Agendar consulta")
    print("5 - Listar consultas")
    print("6 - Enviar lembrete WhatsApp")
    print("7 - Relatório")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_paciente()

    elif opcao == "2":
        area_paciente()

    elif opcao == "3":
        listar_pacientes()

    elif opcao == "4":
        agendar_consulta()

    elif opcao == "5":
        listar_consultas()

    elif opcao == "6":
        enviar_lembrete()

    elif opcao == "7":
        relatorio()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")