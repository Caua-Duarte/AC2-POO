from Veiculo import Veiculo

print(" \n  Olá!!! Seja muito bem vindo à \n------------ALUGA.com------------\nPor favor escolha uma das opções:")
option = int(input("\n1 - Cadastro de Cliente; \n2 - Cadastro de Veículo; \n3 - Estoque de veículo; \n4 - Veículos reservados; \nR: "))

# Definindo funções
def Client():
#    newClient = Function()
#    newClient.Cliente
    print("\nfunta1")

def Vehicle():
    entrada = 0 

    while True :
    #Tente: Se executar e dar erro ele continua sem parar o sistema(If q acontece depois)
        try:
            v1 = Veiculo(tipo_veiculo=input('\nDigite se é carro ou moto (c/m): '),modelo_veiculo=input('Digite o modelo do veiculo (e - Esportivo / c - Crossover / j - Jeep / s - Sedan / v - Van): ' ),cor_veiculo=input('Digite a cor do carro (pt - Preto / br - Branco / vm - Vermelho / vd - Verde / az - Azul / am - Amarelo / cz - Cinza): '),ano_veiculo=int(input('Digite o ano do veiculo: ')),placa_veiculo=input('Digite a placa do veículo (xxxx-xxxx) ou aperte r : '),potencia_motor=int(input('Digite a potencia do motor: ')))

        except:
            print("Opsss! Algo deu errado!  desculpe o imprevisto. Tente nnovamente mais tarde!! =)")
            break
                
        else:
            entrada = input("Deseja continar? Se sim digite 's' Se não digite 'n' ")
            if entrada == "s":
                continue
            else:
                print(v1.estoque_veiculo())
                break


def Inventory():
#   newInventory = Function()
#   newInventory.Cliente
    print("\nfunta3")

def Reservation():
#   newReservation = Function()
#    newReservation.Reserva
    print("\nfunta4")


escolha = { 1 : Client,
            2 : Vehicle,
            3 : Inventory,
            4 : Reservation,
}

escolha.get(option) ()