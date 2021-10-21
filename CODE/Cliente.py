
class Cliente: 
    def __init__(self, nome, anonasc, tel, docid, cnh, end_rua, end_num, end_bairro, end_cidade, end_uf, email):
        self.nomecli = nome
        self.nasc = anonasc
        self.telcli = tel
        self.rgcpf = docid
        self.hab = cnh
        self.rua = end_rua
        self.numero = end_num
        self.bairro = end_bairro
        self.cidade = end_cidade
        self.uf = end_uf
        self.email = email

#Verifica se é um cliente válido
    def ValidaCli(self):
        if self.hab <="0" or self.hab == "":
            print("O cliente nao pode ser cadastrado, informe uma CNH")
            
#Verifica se o e-mail é válido
    def ValidEmail(self):
            if '@' not in self.email:
                print("Email invalido, digite novamente")
                

cli1 = Cliente("Fran", 1998, 11972225869, "04423974899", '0', "Rua 1", 5, "Bairro velho", "MK", "BA", "frangmail.com")

cli1.ValidEmail()
cli1.ValidaCli()
