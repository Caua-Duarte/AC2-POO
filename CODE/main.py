

print(" \n  Olá!!! Seja muito bem vindo à \n------------ALUGA.com------------\nPor favor escolha uma das opções:")
option = int(input("\n1 - Cadastro de Cliente; \n2 - Cadastro de Veículo; \n3 - Estoque de veículo; \n4 - Veículos reservados; \nR: "))

# Definindo funções
def Client():
#    newClient = Function()
#    newClient.Cliente
    print("\nfunta1")

def Vehicle():
#   newVehicle = Function()
#   newVehicle.Cliente
    print("\nfunta2")

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