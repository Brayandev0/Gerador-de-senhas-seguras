# Criador         : Brayan vieira 
# função          : Gerador de senhas seguro  
# versão          : 1.1
# data da criação : 15/2/2024
# Notas versão 1.1: melhor nitidez e tratamento de erros
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
Opcao_a_b =   "[A] Criar uma senha com números                    [B] criar uma senha com caracteres Maiúsculos \n "
Opcao_c_d =   "[C] Criar uma senha com caracteres minusculos       [D] criar uma senha com combinçacões de caracteres especiais  \n  "
Opcao_all =   "[All] uma senha com todas essas opções"
#---------------------------------------------------------------------------------------
#                           Configurando o menu
#
print(" \n Bem vindo ao gerador de senhas seguras \n ")

decisao_do_menu = input(f" {Opcao_a_b} \n {Opcao_c_d} \n {Opcao_all}  \n \n insira :  ").lower()
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
