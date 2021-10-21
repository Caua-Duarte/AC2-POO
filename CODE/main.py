from Veiculo import Veiculo
from Cliente import Cliente


while True:
    try:
        print(" \n  Olá!!! Seja muito bem vindo à \n------------ALUGA.com------------\nPor favor escolha uma das opções:")

        option = int(input("\n1 - Cadastro de Cliente; \n2 - Cadastro de Veículo; \n3 - Estoque de veículo; \n4 - Veículos reservados; \n5 - Sair \nR: "))

        # Definindo funções
        def Client():

            cli1 = Cliente("Fran", 1998, 11972225869, "04423974899", '0', "Rua 1", 5, "Bairro velho", "MK", "BA", "frangmail.com")

            cli1.ValidEmail()
            cli1.ValidaCli()

            print("\nfunfa")

        def Vehicle():
            entrada = 0 

            while True :
            #Tente: Se executar e dar erro ele continua sem parar o sistema(If q acontece depois)
                try:
                    v1 = Veiculo(
                        tipo_veiculo=input('\nDigite se é carro ou moto (c/m): '),
                        modelo_veiculo=input('Digite o modelo da veiculo\nCarro - (e - Esportivo / c - Crossover / j - Jeep / s - Sedan / v - Van)\nMoto - (e - Esportivo / t - Trail / s - Scooter / or - Off-Road)\nR:'),
                        cor_veiculo=input('Digite a cor do carro (pt - Preto / br - Branco / vm - Vermelho / vd - Verde / az - Azul / am - Amarelo / cz - Cinza): '),
                        ano_veiculo=input('Digite o ano do veiculo: '),
                        placa_veiculo=input('Digite a placa do veículo (xxxx-xxxx) ou aperte r : '),
                        potencia_motor=input('Digite a potencia do motor: '),
                        tipo_combustivel = input('Digite o tipo de combustivel: gc - Gasolina Comum / ga - Gasolina aditivada / gp - Gasolina Premium / gf - Gasolina Formulada / ec - Etanol Comum / ea - Etanol Aditivado / dc - Diesel Comum / da - Diesel Aditivado / bd - Biodiesel'))
                    
                except:
                    print("\nOpsss! Algo deu errado!  desculpe o imprevisto. Tente novamente mais tarde!! =)")
                    break
                        
                else:
                    entrada = input("\nDeseja continar a operação? s/n ")
                    if entrada == "s":
                        continue
                    else:
                        break

        def Inventory():
            print(v1.estoque_veiculo())
            print("\nfunfa")

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
        
    except:
        resp = input("\nVocê deseja sair da aplicação? s/n ")
        if resp == 's':
            break
        else:
            continue