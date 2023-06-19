#UMC - Universidade de Mogi das Cruzes
#Programador Mirim - Vinícius da Silva Santana
# ========================================================================================== #

import os
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# =============================== # Funções reservadas # =================================== #

def LPT():
    os.system("clear")  # Limpar Tela

def ExibiReserv():  # Exibir reservas
    print(f"{'ID':^5} {'Nome':^70} {'Apartamento':^20} {'Hóspedes':^8} {'Dias':^12} {'Valor Total':^15}")
    for reserva in ReservasL:
        print(f"{reserva['ID']:^5} {reserva['Nome']:<70} {reserva['Apartamento']:^20} {reserva['Hóspedes']:^8} "
              f"{reserva['Dias']:^12} {reserva['Valor Total']:^15}")

def SelecReserv(reserva_encontrada):  # Exibir a reserva selecionada
    print(f"{'ID':^5} {'Nome':^70} {'Apartamento':^20} {'Hóspedes':^8} {'Dias':^12} {'Valor Total':^15}")
    print(f"{reserva_encontrada['ID']:^5} {reserva_encontrada['Nome']:<70} {reserva_encontrada['Apartamento']:^20} "
          f"{reserva_encontrada['Hóspedes']:^8} {reserva_encontrada['Dias']:^12} {reserva_encontrada['Valor Total']:^15}")

# ========================================== # # ============================================ #

if os.path.exists("reservas.txt"):  # Verificar se existe txt, criar e ler
    ReservasL = []
    with open("reservas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            reserva = {
                "ID": dados[0],
                "Nome": dados[1],
                "Apartamento": int(dados[2]),
                "Hóspedes": int(dados[3]),
                "Dias": int(dados[4]),
                "Valor Total": float(dados[5])
            }
            ReservasL.append(reserva)
else:
    ReservasL = [] # Lista da reserva (l1)

TBDiaria = {
    1: [20.00, 28.00, 35.00, 42.00, 48.00, 53.00],
    2: [25.00, 34.00, 42.00, 50.00, 57.00, 63.00]
}

while True:
    LPT()            # Limpar Tela
    print("""             Boas Vindas a Pousada
    Digite [0] para verificar a tabela de preços por apartamento e pessoas
    Digite [1] para reservar um apartamento
    Digite [2] para cancelar uma reserva
    Digite [3] para alterar uma reserva
    Digite [4] para verificar existe uma reserva
    Digite [5] para SALVAR e SAIR do programa
    """)

    OPC = input("Digite a opção desejada: ")

    if OPC == "1":    #reservar ap
        LPT()         # Limpar Tela
        print("""   \033[4;47;46m   RESERVA DE APARTAMENTOS SELECIONADO   \033[0m """)
        ID = input("ID da reserva: ")

        if any(reserva["ID"] == ID for reserva in ReservasL):
            print("Erro: ID já existe. Insira um ID único.")
            input("Pressione ENTER para voltar ao menu")
            continue

        reserva = {
            "ID": ID,
            "Nome": input("Nome dos hóspedes: ")
        }

        while True:
            try:
                reserva["Apartamento"] = int(input("Tipo de apartamento (1 ou 2): "))
                if reserva["Apartamento"] not in [1, 2]:
                    raise ValueError("Erro: Insira um valor válido (1 ou 2).")
                break
            except ValueError as err:
                print(err)

        while True:
            try:
                reserva["Hóspedes"] = int(input("Quantidade de hóspedes no apartamento(Máx 6): "))
                if reserva["Hóspedes"] < 1 or reserva["Hóspedes"] > 6:
                    raise ValueError("Erro: Insira um valor válido (entre 1 e 6).")
                break
            except ValueError as err:
                print(err)

        while True:
            try:
                reserva["Dias"] = int(input("Quantidade de diárias: "))
                if reserva["Dias"] < 1:
                    raise ValueError("Erro: Insira um valor válido (maior que 0).")
                break
            except ValueError as err:
                print(err)

        diarias = TBDiaria.get(reserva["Apartamento"])
        dia = diarias[reserva["Hóspedes"] - 1]
        reserva["Valor Total"] = dia * reserva["Dias"]
        ReservasL.append(reserva)
        LPT()          # Limpar Tela
        print("Reserva adicionada com sucesso.")
        input("Pressione ENTER para voltar ao menu")
        
    elif OPC == "0":   #tabela de preço
        LPT()          # Limpar Tela
        print("""             \033[4;47;46m   TABELA DE APARTAMENTOS SELECIONADO   \033[0m 
        Quantidade de Pessoas no apartamento      Diária tipo 1 (R$)      Diaria tipo 2(R$)
 1                                                     20,00                   25,00
 2                                                     28,00                   34,00
 3                                                     35,00                   42,00
 4                                                     42,00                   50,00
 5                                                     48,00                   57,00
 6                                                     53,00                   63,00
 """)
        input("Pressione ENTER para voltar ao menu")
    
    elif OPC == "2":   #Cancelar reserva
        LPT()
        print("""   \033[4;47;46m   CANCELAMENTO DE RESERVA SELECIONADO   \033[0m """)
        ExibiReserv()  # Exibir reservas
        ID = input("Insira o ID da reserva a ser excluída: ")
        reserva_encontrada = None
        for reserva in ReservasL:
            if reserva["ID"] == ID:
                reserva_encontrada = reserva
                break

        if reserva_encontrada:
            LPT()
            print("""               A RESERVA A SEGUIR SERÁ EXCLUÍDA:""")
            SelecReserv(reserva_encontrada)  # Exibir a reserva selecionada
            confirmacao = input("Tem certeza de que deseja excluir esta reserva? (S/N): ")
            if confirmacao.upper() == "S":
                ReservasL.remove(reserva_encontrada)
                LPT()
                print("Reserva excluída com sucesso.")
            else:
                LPT()
                print("Operação cancelada. A reserva não foi excluída.")

        else:
            LPT()
            print("Reserva não encontrada. Verifique o ID informado.")

        input("Pressione ENTER para voltar ao menu")

    elif OPC == "3":   #alterar reserva
        LPT()
        print("""   \033[4;47;46m   ALTERAÇÃO DE RESERVA SELECIONADO   \033[0m """)
        ExibiReserv() # Exibir reservas
        ID = input("Insira o ID da reserva a ser alterada: ")

        reserva_encontrada = None
        for reserva in ReservasL:
            if reserva["ID"] == ID:
                reserva_encontrada = reserva
                break

        if reserva_encontrada:
            LPT()
            print("""   \033[4;47;46m   RESERVA ENCONTRADA, INSIRA OS NOVOS DADOS   \033[0m """)
            SelecReserv(reserva_encontrada) # Exibir a reserva selecionada
            while True:
             try:
                reserva_encontrada["Nome"] = input("Nome dos hóspedes atualizados: ")
                    
                reserva_encontrada["Apartamento"] = int(input("Novo tipo de apartamento (1 ou 2): "))
                if reserva_encontrada["Apartamento"] not in [1, 2]:
                    raise ValueError("Erro: Insira um valor válido de apartamento (1 ou 2).")

                reserva_encontrada["Hóspedes"] = int(input("Nova quantidade de hóspedes no apartamento (Máx 6): "))
                if reserva_encontrada["Hóspedes"] < 1 or reserva_encontrada["Hóspedes"] > 6:
                    raise ValueError("Erro: Insira um valor válido de apartamento (entre 1 e 6).")

                reserva_encontrada["Dias"] = int(input("Nova quantidade de diárias: "))
                if reserva_encontrada["Dias"] < 1:
                    raise ValueError("Erro: Insira um valor válido de diárias (maior que 0).")

                break
             except ValueError as err:
                print(err)

            diarias = TBDiaria.get(reserva_encontrada["Apartamento"])
            dia = diarias[reserva_encontrada["Hóspedes"] - 1]
            reserva_encontrada["Valor Total"] = dia * reserva_encontrada["Dias"]

            LPT()
            print("Reserva alterada com sucesso.")
        else:
            LPT()
            print("Reserva não encontrada. Verifique o ID informado.")

        input("Pressione ENTER para voltar ao menu")

    elif OPC == "4":    #ver reservas realizadas
        LPT()
        print("""   \033[4;47;46m   VERIFICAÇÃO DE RESERVAS SELECIONADO   \033[0m """)
        ExibiReserv() # Exibir reservas
        ID = input("Insira o ID da reserva a visualizar: ")
        reserva_encontrada = None
        for reserva in ReservasL:
            if reserva["ID"] == ID:
                reserva_encontrada = reserva
                break

        if reserva_encontrada:
            LPT()
            print("""   \033[4;47;46m   RESERVA ENCONTRADA   \033[0m """)

            SelecReserv(reserva_encontrada) # Exibir a reserva selecionada
        else:
            print("Reserva não encontrada. Verifique o ID informado.")

        input("Pressione ENTER para voltar ao menu")
    
    elif OPC == "5":   #sair e salvar
        LPT()
        print("Salvando as reservas e saindo do programa...")
        with open("reservas.txt", "w") as arquivo:
            for reserva in ReservasL:
                linha = f"{reserva['ID']},{reserva['Nome']},{reserva['Apartamento']},{reserva['Hóspedes']},{reserva['Dias']},{reserva['Valor Total']}\n"
                arquivo.write(linha)
        break
    
    else:
        LPT()
        print("Opção inválida. Tente novamente.")
        input("Pressione ENTER para voltar ao menu")


