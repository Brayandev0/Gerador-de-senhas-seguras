# Criador         : Brayan vieira 
# função          : Gerador de senhas seguro  
# versão          : 1.2
# data da criação : 15/2/2024
# Notas versão 1.1: melhor nitidez e tratamento de erros
# Notas versão 1.2: Melhor nitidez no menu
#---------------------------------------------------------------------------------------
#                                   configurando bibliotecas 
import random
import string
#---------------------------------------------------------------------------------------
#                               Função para gerar senha 
#
def gerar_senha(tamanho_da_senha, tipo_da_senha):
    senha = ""
    for _ in range(tamanho_da_senha):
        senha += random.choice(tipo_da_senha)
        continue
    return print(f" \n Sua senha gerada e : {senha} \n ")
#---------------------------------------------------------------------------------------
#                       Variaveis padrões e menu 
#
ERRO_PADRAO = "você inseriu um caracter invalido"
MENU = '''

Bem-vindo ao Gerador de Senhas Seguras

Escolha uma opção:

[A] Criar uma senha com números
[B] Criar uma senha com caracteres Maiúsculos
[C] Criar uma senha com caracteres minúsculos
[D] Criar uma senha com combinações de caracteres especiais
[All] Uma senha com todas essas opções

Digite a letra correspondente à opção desejada ou 'S' para sair: '''
#---------------------------------------------------------------------------------------
#                           Configurando o menu
#
print(" \n Bem vindo ao gerador de senhas seguras \n ")

decisao_do_menu = input(MENU).lower()
match decisao_do_menu:
    case "a":
        tipo_senha = string.digits
    case "b":
        tipo_senha = string.ascii_uppercase
    case "c":
        tipo_senha = string.ascii_lowercase
    case "d":
        tipo_senha = string.punctuation
    case "all":
        tipo_senha = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    case _:
        print(f"\n {ERRO_PADRAO}\n ")
        exit()

#---------------------------------------------------------------------------------------
#                               Configurando o comprimento e tratando erros
#
print("\n \n Insira o comprimento da senha abaixo \n Ex : 10 \n \n uma senha de 10 caracteres ")
try:
    comprimento = int(input("\n insira : "))
except ValueError:
    print(f" \n \n {ERRO_PADRAO} \n ")
#    exit()
except NameError:
    print(ERRO_PADRAO)
#---------------------------------------------------------------------------------------
#                           
gerar_senha(comprimento, tipo_senha)
