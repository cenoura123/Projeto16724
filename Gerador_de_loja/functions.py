import requests
import json
import pygame
from datetime import *
import os

# BD


def Verificar_se_nome_existe(nome_procurado):
    encontrar = False
    # Faz a requisição à URL especificada
    requisicao = requests.get('https://loja-c4a27-default-rtdb.firebaseio.com/Banco/Conta/.json')
    # Converte a resposta JSON para um dicionário Python
    consulta = requisicao.json()

    # Itera sobre os itens do dicionário
    for Conta, Vs in consulta.items():
        # Exibe o conteúdo da conta
        #print(Vs)
        
        # Verifica se o nome procurado está em algum dos valores
        if 'Name' in Vs and Vs['Name'] == nome_procurado:
            encontrar = True
            break

    if encontrar:
        return False
    else:
        return True

# Exemplo de uso
    
def Criar_Conta(nome, senha):
    dados_conta = {
        'Name': f"{nome}",
        'Password': f"{senha}"
    }
    requisicao = requests.post('https://loja-c4a27-default-rtdb.firebaseio.com/Banco/Conta/.json', data=json.dumps(dados_conta))

def Enter_Cont(nomex):
    dados = 'https://loja-c4a27-default-rtdb.firebaseio.com/Banco/Conta/.json'
    
    # Faz a requisição à URL especificada
    requisicao = requests.get(dados)
    
    # Converte a resposta JSON para um dicionário Python
    consulta = requisicao.json()
    
    # Inicializa uma variável para verificar se o nome foi encontrado
    encontrado = False
    
    # Itera sobre os itens do dicionário
    for nome, info in consulta.items():
        # Verifica se o nome procurado está presente e exibe a senha
        if info['Name'] == nomex:
            senha = info['Password']
            encontrado = True
            break
    
    # Se o nome não foi encontrado, exibe "NAO TEM SENHA"
    if encontrado:
        return senha
    else:
        return False


def Verificar_Version():
    dados = requests.get('https://loja-c4a27-default-rtdb.firebaseio.com/Banco/Vs.json')
    consulta = dados.json()
    encontrar = False
    for vs in consulta:
        versao = consulta[vs]
        encontrar = True
        break
    if encontrar:
        return versao
    else:
        return False
    
# Funções de Criamento , Consulta e Exclusao
def Criar_Arquivo_Base_Shop():

    caminho = "_internal/dados.json"

    if os.path.exists(caminho):
        return True
    else:

        dados = {
           
        }
        # Caminho da pasta onde os dados JSON serão salvos
        caminho_da_pasta = "_internal/"  # Substitua pelo caminho desejado

        # Nome do arquivo onde os dados JSON serão salvos
        nome_do_arquivo = "dados.json"

        # Cria a pasta se ela não existir
        os.makedirs(caminho_da_pasta, exist_ok=True)

        # Caminho completo do arquivo
        caminho_completo_do_arquivo = os.path.join(caminho_da_pasta, nome_do_arquivo)

        # Abrir o arquivo em modo de escrita e salvar os dados JSON
        with open(caminho_completo_do_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)


# Função de Add Lojas(shops)

def Criar_lojas(Nome):
    data_atual = datetime.now()
    data_atual_formatada = data_atual.date()
    novo_dicionario = {
        Nome: {
            "Nome": Nome,
            "Data_Criada": f"{data_atual_formatada}",
            "Produtos" : {

            },
            "Desing" : {

            }
        }
    }

    # Caminho da pasta e nome do arquivo JSON
    caminho_da_pasta = "_internal/"  # Substitua pelo caminho desejado
    nome_do_arquivo = "dados.json"
    caminho_completo_do_arquivo = os.path.join(caminho_da_pasta, nome_do_arquivo)

    # Ler os dados atuais do arquivo JSON
    if os.path.exists(caminho_completo_do_arquivo):
        with open(caminho_completo_do_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
    else:
        dados = {}  # Se o arquivo não existir, iniciamos com um dicionário vazio

    # Adicionar o novo dicionário aos dados existentes
    dados.update(novo_dicionario)

    # Salvar os dados de volta no arquivo JSON
    with open(caminho_completo_do_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"O novo dicionário foi adicionado ao arquivo {caminho_completo_do_arquivo}")

# pega nomes das lojas 

def Nomes_lojas():
    # Caminho da pasta onde o arquivo JSON está salvo
    caminho_da_pasta = "_internal/"  # Substitua pelo caminho desejado

    # Nome do arquivo JSON
    nome_do_arquivo = "dados.json"

    # Caminho completo do arquivo
    caminho_completo_do_arquivo = os.path.join(caminho_da_pasta, nome_do_arquivo)

    # Ler os dados do arquivo JSON
    with open(caminho_completo_do_arquivo, 'r') as arquivo:
        dados_carregados = json.load(arquivo)
        return dados_carregados

# funçao decorativas

def Som(caminho):
    try:
        pygame.init()
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
        return("Tocando")
    except Exception as e:
        print("Arquivo não encontrado")

