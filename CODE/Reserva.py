from Cliente import *
from Veiculo import *
from datetime import date

class Reserva:
    
    def __init__(self,nome_cliente,data_entrega,data_retirada, ck_list_entrega, ck_list_retirada):

        data_entrega = data_entrega.split('-')
        data_retirada = data_retirada.split('-')

        self.data_entrega = date(int(data_entrega[0]),int(data_entrega[1]),int(data_entrega[2]))
        self.data_retirada = date(int(data_retirada[0]),int(data_retirada[1]),int(data_retirada[2]))
        self.ck_list_entrega = ck_list_entrega
        self.ck_list_retirada = ck_list_retirada
        self.n_cliente = nome_cliente
        
    def ValorReserva(self,placa):

        self.valor_adicional = self.data_entrega - self.data_retirada

        placa = placa.upper()

        for plc in veiculo_lv.keys():
            if plc == placa:
                if veiculo_lv[plc][0] == 'Carro':

                    if veiculo_lv[plc][1] == "Esportivo":
                        self.valor_reserva = float(250.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "Crossover":
                        self.valor_reserva = float(150.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "Jeep":
                        self.valor_reserva = float(200)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "Sedan":
                        self.valor_reserva = float(300.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "Van":
                        self.valor_reserva = float(400.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    else:
                        print("Não existe isso seu cabeçudo!")
                else:
                    if veiculo_lv[plc][1] == "Esportivo":
                        self.valor_reserva = float(50.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "Trail":
                        self.valor_reserva = float(70.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "Scooter":
                        self.valor_reserva = float(60.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "Off-Road":
                        self.valor_reserva = float(55.00)*self.valor_adicional.days
                        print("O Valor Total Reserva: R$", self.valor_reserva)
                    
                    else:
                        print("O mula já deu por hoje neh não aguento mais erro")

                return

        print("Placa não encontrada")
    
    def CKlistEntrega(self):
        if self.ck_list_entrega == True:
            print("Carro esta liberado")
        else:
            print("Carro não esta conforme")

    def CKlistRetirada(self):
        if self.ck_list_retirada == True:
            print("Carro esta liberado")
        else:
            print("Carro nao esta conforme")
         