#User levels: 0-admin, 1-gerente, 2-conferente, 3-vendedor, 4-cliente(via_API)

class user():
    def __init__(self, nome,  lvl_user = 1, nickname, password, email, CPF):
        self.nome = nome 
        self.lvl_user = lvl_user
        self.nickname = nickname
        self.password = password
        self.email = email
        self.CPF = CPF
        print("Construtor finalizado!!!")

    def Cadastro(self, nome,  lvl_user, nickname, password, email, CPF):
        while(True):
            err = ["!@#$%*/+.-"]
            self.nome = input("Nome: ")
            if isdigit(self.nome) or (err in self.nome):
                print("Nome inválido. Caracteres especiais
                e/ou números não permitidos")
                self.nome = input("Nome: ")
            else:
                break
        self.nickname = input("Digite o login: ")
        self.password = input("Digite a senha: ")
        self.email = input("Digite o e-mail: ")
        self.CPF= input("Digite o CPF: ")

    def NIVEL_ACESSO(self, lvl_user)
        self.lvl_user = lvl_user
        permissoes(self.lvl_user)
        
