from Cliente import *
from Veiculo import *

class Reserva(Veiculo):
    
    def __init__(self,nome_cliente,data_retirada, ck_list_entrega, ck_list_retirada):

        self.data_retirada = data_retirada
        self.ck_list_entrega = ck_list_entrega
        self.ck_list_retirada = ck_list_retirada
        self.n_cliente = nome_cliente
        
    def ValorReserva(self,placa):

        # super().__init__(tipo_veiculo, modelo_veiculo)

        for plc in veiculo_lv.keys():
            if plc == placa:
                if veiculo_lv[plc][0] == 'c':

                    if veiculo_lv[plc][1] == "e":
                        self.valor_reserva = float(250.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "c":
                        self.valor_reserva = float(150.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "j":
                        self.valor_reserva = float(200)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "s":
                        self.valor_reserva = float(300.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "v":
                        self.valor_reserva = float(400.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    else:
                        print("Não existe isso seu cabeçudo!")
                else:
                    if veiculo_lv[plc][1] == "e":
                        self.valor_reserva = float(50.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "t":
                        self.valor_reserva = float(70.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "s":
                        self.valor_reserva = float(60.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)

                    elif veiculo_lv[plc][1] == "or":
                        self.valor_reserva = float(55.00)*self.valor_adicional
                        print("O Valor Total Reserva: R$", self.valor_reserva)
                    
                    else:
                        print("O mula já deu por hoje neh não aguento mais erro")

                return

        print("Placa não encontrada")
       
    def ValorAdicional(self, data_entrega):
        if  data_entrega == self.data_retirada:
            self.valor_adicional = 1
        else:
            self.valor_adicional = 1 + (self.data_retirada - data_entrega)  
            print("QTD. Dias Adicionais: ", self.valor_adicional)
    
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
         
V = Reserva(2021-4-4, True, True) 
V.ValorAdicional(2021-4-4)
V.ValorReserva( tipo_veiculo="c", modelo_veiculo="e")
V.CKlistEntrega()
V.CKlistRetirada()
