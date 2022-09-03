agenda = []

def askf_nome():
     return(input("Insira seu Nome: "))

def askf_tel():
     return(input("Insira seu Telefone: "))

def askf_email():
     return(input("Insira seu e-mail: "))

def askf_tt():
     return(input("Insira seu @ no Twitter: "))

def askf_face():
     return(input("Insira seu Facebook: "))



def show_data(nome, tel, email, tt, face):
     print("Nome: %s | Telefone: %s | Email: %s | Twitter: %s | Facebook: %s" % (nome, tel, email, tt, face))

def askf_archive_name():
     return(input("Nome do arquivo: "))

def busca(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None

def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None

def novo():
     global agenda
     nome = askf_nome()
     tel = askf_tel()
     email = askf_email()
     tt = askf_tt()
     face = askf_face()
     agenda.append([nome, tel, email, tt, face])

def apaga():
     global agenda
     nome = askf_nome()
     p = busca(nome)
     if p != None:
         del agenda[p]
     else:
         print("Nome não encontrado.")

def altera():
     p = busca(askf_nome())
     if p != None:
         nome = agenda[p][0]
         tel = agenda[p][1]
         email = agenda [p][2]
         tt = agenda [p][3]
         face = agenda [p][4]
         print("Encontrado:")
         show_data(nome, tel, email, tt, face)
         nome = askf_nome()
         tel = askf_tel()
         email = askf_email()
         tt = askf_tt()
         face = askf_face()
         agenda[p] = [nome, tel, email, tt, face]
     else:
         print("Nome não encontrado.")

def lista():
     print("=============\n\nAgenda\n\n=============")
     for e in agenda:
         show_data(e[0], e[1], e[2], e[3], e[4])
     print("=============\n\nAgenda\n\n=============")

def consulta():
     p = pesquisa(askf_nome())
     if p != None:
         nome = agenda[p][0]
         tel = agenda[p][1]
         email = agenda [p][2]
         tt = agenda [p][3]
         face = agenda [p][4]
         print("Encontrado:")
         show_data(nome, tel, email, tt, face)         
     else:
         print("Nome não encontrado.")

def validacao_choice(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""
|====================================|
|   1 - Cria um Novo Registro        |
|   2 - Alterar Registro existente   |
|   3 - Apaga Registro existente     |
|   4 - Listar Registros existentes  |
|   5 - Pesquisa Registro especifico |
|                                    |
|   0 - Sai                          |
|====================================|
""")
     return validacao_choice("Escolha uma opção: ",0,6)

while True:
     opcao = menu()
     if opcao == 0:
         break
     elif opcao == 1:
         novo()
     elif opcao == 2:
         altera()
     elif opcao == 3:
         apaga()
     elif opcao == 4:
         lista()
     elif opcao == 5:
         pesquisa()