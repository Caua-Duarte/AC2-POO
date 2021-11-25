cliente = []
class Cliente:
    def __init__(self, nome, anonasc, tel, docid, cnh, end_rua, end_num, end_bairro, end_cidade, end_uf, email):
        global cliente

        __valido = True

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

        if self.hab <="0" or self.hab == "":
            print("O cliente nao pode ser cadastrado, informe uma CNH")
            __valido = False

        if '@' not in self.email:
            print("Email invalido, digite novamente")
            __valido = False

        if __valido:
            cliente.append([self.nomecli,self.nasc,self.telcli,self.rgcpf,self.hab,self.rua,self.numero,self.bairro,self.cidade,self.uf,self.email])