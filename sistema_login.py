import os
import json
import getpass

class SistemaLogin:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        try:
            with open("usuarios.json", "r") as arquivo:
                usuarios = json.load(arquivo)
        except FileNotFoundError:
            usuarios = []
            with open("usuarios.json", "x") as arquivo:
                json.dump(usuarios, arquivo)
            print("\nAinda não temos usuários registrados.")
        return usuarios

    def bem_vindo(self):
        print("Sistema de Registo / Login")
        print("*" * 27)
        print("1. Listar\n2. Registrar\n3. Logar\n4. Deletar Usuário\n5. Sair\n")

    def listar_usuarios(self):
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"Usuário: {i} - {usuario['id']}")

    def cadastrar(self):
        usuarios_existente = False
        senha_ok = False

        novo_usuario = {
            "id": input("Registre um Usuário: ").lower(),
            "senha": getpass.getpass("Registre uma Senha: ")
        }
        confirmar_senha = getpass.getpass("Confirme a Senha: ")

        if novo_usuario["id"] == "":
            print("\nUsuário em branco, necessário preencher.")
        elif len(novo_usuario["id"]) <= 4:
            print("\nUsuário muito curto.")
        elif novo_usuario["id"] and novo_usuario["id"][0].isdigit():
            print("\nO usuário precisa começar com uma letra.")
        else:
            for usuario in self.usuarios:
                if usuario["id"] == novo_usuario["id"]:
                    usuarios_existente = True
                    break

        if novo_usuario["senha"] != confirmar_senha:
            print("\nAs senhas não coincidem.")
        elif novo_usuario["senha"] == "":
            print("\nSenha em branco, necessário preencher.")
        elif len(novo_usuario["senha"]) <= 4:
            print("\nSenha muito curta.")
        else:
            senha_ok = True

            if usuarios_existente:
                print("\nUsuário já registrado.")
            elif usuarios_existente == False and senha_ok == True:
                self.usuarios.append(novo_usuario)
                print("\nUsuário registrado com sucesso!")

            with open("usuarios.json", "w") as arquivo:
                json.dump(self.usuarios, arquivo)

    def logar(self):
        logar_usuario = input("\nDigite seu usuário: ").lower()
        logar_senha = getpass.getpass("Digite sua Senha: ")

        for usuario in self.usuarios:
            if logar_usuario == "" or logar_senha == "":
                print("\nUsuário em branco, necessário preencher.")
                break
            elif logar_usuario == usuario["id"] and logar_senha != usuario["senha"]:
                print("\nFalha no Login.")
                break
            elif logar_usuario != usuario["id"] and logar_senha == usuario["senha"]:
                print("\nFalha no Login.")
                break
            else:
                logar_usuario == usuario["id"] and logar_senha == usuario["senha"]
                print("\nLogin realizado com Sucesso.")
                print(f"\nOlá novamente, '{logar_usuario}'.")
                break

    def excluir(self):
        deletar_usuario = input("\nDigite o Usuário que deseja Deletar: ").lower()

        usuario_deletar = None

        for i, usuario in enumerate(self.usuarios):
            if usuario["id"] == deletar_usuario:
                usuario_deletar = i
                break

        if usuario_deletar is not None:
            senha = getpass.getpass("\nDigite sua Senha: ")
            confirmar_senha = getpass.getpass("Confirme sua Senha: ")

            if senha != confirmar_senha:
                print("\nAs Senhas não Conferem.")
            else:
                if usuario["senha"] == senha:
                    del self.usuarios[usuario_deletar]
                    print("\nUsuário deletado com Sucesso!")
                else:
                    print("\nUsuário ou Senha não conferem.")
        else:
            print("\nUsuário não encontrado.")

        with open("usuarios.json", "w") as arquivo:
            json.dump(self.usuarios, arquivo)

    def finalizar(self):
        enter = input("\nPressione 'ENTER' para continuar.")
        os.system("cls")

    def executar(self):
        while True:
            self.bem_vindo()
            resposta = input("Qual ação deseja realizar? [1], [2], [3], [4] or [5]\nResposta: ")

            if resposta == "1":
                self.listar_usuarios()
            elif resposta == "2":
                self.cadastrar()
            elif resposta == "3":
                self.logar()
            elif resposta == "4":
                self.excluir()
            elif resposta == "5":
                print("\nTe vejo em breve")
                break
            else:
                print("\nDigite apenas: 1, 2, 3, 4 or 5")

            self.finalizar()

sistema = SistemaLogin()
sistema.executar()
