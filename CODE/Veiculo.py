class Veiculo:

    veiculo_lv = {}

    #Cadastro do veiculo
    def __init__(self,tipo_veiculo,modelo_veiculo,cor_veiculo,placa_veiculo,tipo_combustivel,potencia_motor,ano_veiculo,nao_cadastrar=False):

        '''
        ***nao_cadastrar -> Informe "True" caso queria chamar o construtor mas não queira cadastrar nenhum veiculo***\n\n
        tipo_veiculo -> Carro: "c" / Motocicleta: "m"\n
        modelo_veiculo -> Carro: Esportiva: "e", Crossover: "c", Jipe: "j", Sedan: "s", Van: "v" / Motocicleta: Esportiva: "e", Trail: "t", Scooter: "s", Off-Road: "or"\n
        cor_veiculo -> Preto: "pt", Branco: "br", Vermelho: "vm", Verde: "vd", Azul: "az", Amarelo: "am", Cinza: "cz"\n
        placa_veiculo -> Ex: 1234-ABCD \ "r" para randomizar uma placa\n
        tipo_combustivel -> Gasolina Comum: "gc", Gasolina aditivada: "ga", Gasolina Premium: "gp", Gasolina Formulada: "gf", Etanol Comum: "ec", Etanol Aditivado: "ea", Diesel Comum: "dc", Diesel Aditivado: "da", Biodiesel: "bd"\n
        ano_veiculo -> Informar o ano do veiculo como int()\n
        potencia_motor -> Potência medida em cavalos int()
        '''
        if nao_cadastrar == False:

            import random as rd
            import datetime as dt

            _erro = False

            __tipo_veiculo = {'c':'Carro','m':'Motocicleta'}
            __mod_veic_carro = {'e':'Esportivo','c':'Crossover','j':'Jeep','s':'Sedan','v':'Van'}
            __mod_veic_moto = {'e':'Esportivo','t':'Trail','s':'Scooter','or':'Off-Road'}
            __cor_veiculo = {'pt':'Preto','br':'Branco','vm':'Vermelho','vd':'Verde','az':'Azul','am':'Amarelo','cz':'Cinza'}
            __tipo_combustivel = {'gc':'Gasolina Comum','ga':'Gasolina aditivada','gp':'Gasolina Premium','gf':'Gasolina Formulada','ec':'Etanol Comum','ea':'Etanol Aditivado','dc':'Diesel Comum','da':'Diesel Aditivado','bd':'Biodiesel'}

            self.t_v = tipo_veiculo.lower()
            self.m_v = modelo_veiculo
            self.c_v = cor_veiculo
            self.p_v = placa_veiculo.upper()
            self.t_c = tipo_combustivel
            self.a_v = ano_veiculo
            self.p_m = potencia_motor

            #Verifica se o tipo de veiculo está correto
            if self.t_v != '':
                if self.t_v not in __tipo_veiculo.keys():
                    print('\033[1;31mTipo de veiculo não encontrado\033[m')
                    _erro = True
                else:
                    self.t_v = __tipo_veiculo[self.t_v]
            else:
                self.t_v = __tipo_veiculo['c']

            #Verifica se o modelo do veiculo está correto
            if self.t_v == 'Carro':
                if self.m_v != '':
                    if self.m_v not in __mod_veic_carro:
                        print('\033[1;31mModelo de carro não encontrado\033[m')
                        _erro = True
                    else:
                        self.m_v = __mod_veic_carro[self.m_v]
                else:
                    self.m_v = __mod_veic_carro['s']
            else:
                if self.m_v != '':
                    if self.m_v not in __mod_veic_moto:
                        print('\033[1;31mModelo de moto não encontrado\033[m')
                        _erro = True
                    else:
                        self.m_v = __mod_veic_moto[self.m_v]
                else:
                    self.m_v = __mod_veic_moto['t']

            #Verifica se a cor do veiculo está correta
            if self.c_v != '':
                if self.c_v not in __cor_veiculo.keys():
                    print('\033[1;31mCor inválida\033[m')
                    _erro = True
                else:
                    self.c_v = __cor_veiculo[self.c_v]
            else:
                self.c_v = __cor_veiculo['pt']

            #Randomiza uma placa no formato "####-####" com caracteres numéricos e alfabéticos
            if self.p_v == 'R' or self.p_v == '':
                rand_placa = []
                while len(rand_placa) < 9:
                    nxt_v = rd.randint(0,1)
                    if nxt_v == 0:
                        rand_char = rd.randint(0,9)
                    else:
                        rand_char = rd.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
                    if len(rand_placa) == 3:
                        rand_placa.append(str(rand_char))
                        rand_placa.append('-')
                    else:
                        rand_placa.append(str(rand_char))
                self.p_v = ''.join(rand_placa)
            #Verifica se a placa informada está correta
            else:
                if len(self.p_v) == 9:
                    if '-' in self.p_v and self.p_v.count('-') == 1:
                        for c in self.p_v:
                            if c.isalnum() == False and c != '-':
                                print('\033[1;31mPlaca inválida\033[m')
                                _erro = True
                    else:
                        print('\033[1;31mPlaca inválida\033[m')
                        _erro = True
                else:
                    print('\033[1;31mPlaca inválida\033[m')
                    _erro = True

            #Verifica se o tipo de combustível é válido
            if self.t_c != '':
                if self.t_c not in __tipo_combustivel.keys():
                    print('\033[1;31mTipo de gasolina inválida\033[m')
                    _erro = True
                else:
                    self.t_c = __tipo_combustivel[self.t_c]
            else:
                self.t_c = __tipo_combustivel['gc']

            #Verifica se o ano do veiculo é válido
            if self.a_v != '':
                if self.a_v.isnumeric() != True:
                    print('\033[1;31mAno do veiculo inválido\033[m')
                    _erro = True
                else:
                    self.a_v = int(self.a_v)
                    if dt.date.today().year < self.a_v:
                        print('\033[1;31mAno do veiculo inválido\033[m')
                        _erro = True
            else:
                self.a_v = 2015

            #Verifica se a potência do veiculo é válida
            if self.p_m != '':
                if self.p_m.isnumeric() != True:
                    print('\033[1;31mPotência do motor inválida\033[m')
                    _erro = True
                else:
                    self.p_m = int(self.p_m)
                    if self.p_m <= 0:
                        print('\033[1;31mPotência do motor inválida\033[m')
                        _erro = True
            else:
                self.p_m = 110

            #Insere o veiculo em um array de veiculos livres caso ele ainda não esteja cadastrado
            if _erro == False:
                if self.p_v not in self.veiculo_lv:
                    self.veiculo_lv[self.p_v] = (self.t_v,self.m_v,self.c_v,self.p_m,self.t_c,self.a_v)
                else:
                    print('\033[1;31mVeiculo já cadastrado\033[m')
            else:
                print('\033[1;31mInformações inválidas, veiculo não cadastrado\033[m')
        
        else:
            ...

    def estoque_veiculo(self):
        '''
        Mostra as informações de todos os veiculos\n
        Informa quais carros estão disponíveis
        '''
        return self.veiculo_lv

#Run
if __name__ == '__main__':
    v1 = Veiculo(tipo_veiculo='m',modelo_veiculo='e',cor_veiculo='br',ano_veiculo=2018,placa_veiculo='r',potencia_motor=90)
    print(v1.estoque_veiculo())
