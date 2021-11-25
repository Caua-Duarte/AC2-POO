from Veiculo import *
from Cliente import *
from Reserva import *


while True:
    try:
        print(" \n  Olá!!! Seja muito bem vindo à \n------------ALUGA.com------------\nPor favor escolha uma das opções:")

        option = int(input("\n1 - Cadastro de Cliente; \n2 - Cadastro de Veículo; \n3 - Estoque de veículo; \n4 - Veículos reservados; \n5 - Sair \nR: "))

        # Definindo funções
        def Client():

            cli1 = Cliente(
                nome=input("\nDigite o seu Nome: "),
                anonasc=input("\nDigite seu ano de nascimento: "),
                tel=input("\nDigite o seu telefone: "),
                docid=input("\nDigite o seu RG\CPF: "),
                cnh=input("\nDigite o seu CNH: "),
                end_rua=input("\nDigite o seu endereço de rua: "),
                end_num=input("\nDigite o numero da sua casa: "),
                end_bairro=input("\nDigite seu bairro: "),
                end_cidade=input("\nDigite sua cidade: "),
                end_uf=input("\nDigite seu estado: "),
                email=input("\nDigite seu email: "))

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
            est = Veiculo(nao_cadastrar=True)
            print(est.estoque_veiculo()) 
            #    newReservation.Reserva
            print("\nfunta4")      

        def Reservation():
            Reserva(
                nome_cliente=input("\nDigite o seu Nome: "),
                data_entrega=input("\nDigite a data de entrega: "),
                data_retirada=input("\nDigite a data de retirada: "),
                ck_list_entrega=bool(input("\nO check-list de entrega está ok? [True/False]: ")),
                ck_list_retirada=bool(input("\nO check-list de retirada está ok? [True/False]: "))
            ).ValorReserva(
                placa=input("Digite a placa: ")
            )

            print("\nfunta5")   

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