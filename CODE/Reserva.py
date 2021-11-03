from Veiculo import *

class Reserva(Veiculo):
    
    def __init__(self, data_retirada, ck_list_entrega, ck_list_retirada):
        
        tipo = super().__init__(tipo_veiculo)
        modelo = super().__init__(modelo_veiculo)
        self.v1 = veiculo.t_v
        self.v2 = veiculo.m_v
        self.data_retirada = data_retirada
        self.ck_list_entrega = ck_list_entrega
        self.ck_list_retirada = ck_list_retirada 

    def ValorReserva(self, tipo, ):

        if tipo == "c":

            if modelo == "e":
                self.valor_reserva = float(250.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            elif modelo == "c":
                self.valor_reserva = float(150.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            elif modelo == "j":
                self.valor_reserva = float(200)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            elif modelo == "s":
                self.valor_reserva = float(300.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            elif modelo == "v":
                self.valor_reserva = float(400.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            else:
                print("Não existe isso seu cabeçudo!")

        elif tipo == "m":

            if modelo == "e":
                self.valor_reserva = float(50.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            elif modelo == "t":
                self.valor_reserva = float(70.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            elif modelo == "s":
                self.valor_reserva = float(60.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)

            elif modelo == "or":
                self.valor_reserva = float(55.00)*self.valor_adicional
                print("O Valor Total Reserva: R$", self.valor_reserva)
            
            else:
                print("O mula já deu por hoje neh não aguento mais erro")

        else:
            print("Categoria não localizada")
       
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
            

'''
    def CKlistRetirada(self):
        if self.ck_list_retirada == True:
            print("Carro esta liberado")
        else:
            print("Carro nao esta conforme")
         
V = Reserva(2021-4-4, True, False)
V.ValorAdicional(2021-4-4)
V.ValorReserva(veiculo="Carro_Jipe")
V.CKlistEntrega()
V.CKlistRetirada()
'''