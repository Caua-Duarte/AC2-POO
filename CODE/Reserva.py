
class Reserva:
    
    def __init__(self, data_retirada, ck_list_entrega, ck_list_retirada):
        
        self.data_retirada = data_retirada
        self.ck_list_entrega = ck_list_entrega
        self.ck_list_retirada = ck_list_retirada 

    def ValorReserva(self, veiculo):
        if veiculo == "Carro_Esportivo":
            self.valor_reserva = float(250.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Carro_Crossover":
            self.valor_reserva = float(150.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Carro_Jipe":
            self.valor_reserva = float(200)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Carro_Sedan":
            self.valor_reserva = float(300.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Carro_Van":
            self.valor_reserva = float(400.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Motocicleta_Scooter":
            self.valor_reserva = float(50.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Motocicleta_Esportivo":
            self.valor_reserva = float(70.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Motocicleta_Trail":
            self.valor_reserva = float(60.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

        elif veiculo == "Motocicleta_OffRoad":
            self.valor_reserva = float(55.00)*self.valor_adicional
            print("O Valor Total Reserva: R$", self.valor_reserva)

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
