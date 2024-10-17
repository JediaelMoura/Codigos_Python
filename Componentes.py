import os

# Define a quantidade de cada componente disponível em um dicionário
componentes = {
    'placas': 0,
    'caixinha': 0,
    'arduino_micro': 0,
    'botao_amarelo': 0,
    'botao_vermelho': 0,
    'resistor470R': 0,
    'resistor1k': 0,
    'encaixe_femea12pinos': 0,
    'encaixe_macho4pinos': 0,
    'leds': 0,
    'rele5V': 0,
    'capacitor10v': 0,
    'conectorRCA': 0,
    'caboUSB_3M': 0,
    'caboUSB_1M': 0
}

# Desejados
quantidade_desejada_bpulse = 10
quantidade_desejada_bplay = 10

def salvar_componentes(arquivo='componentes.txt'):
    with open(arquivo, 'w') as f:
        for nome, quantidade in componentes.items():
            f.write(f"{nome},{quantidade}\n")
        f.write(f"quantidade_desejada_BPulse,{quantidade_desejada_bpulse}\n")
        f.write(f"quantidade_desejada_BPlay,{quantidade_desejada_bplay}\n")

def carregar_componentes(arquivo='componentes.txt'):
    path = os.path.join(os.getcwd(), arquivo)
    if not os.path.exists(path):
        print(f"Arquivo {arquivo} não encontrado. Criando um novo arquivo.")
        salvar_componentes(arquivo)  # Salvar o estado inicial se o arquivo não existir
    else:
        with open(path, 'r') as f:
            for linha in f:
                partes = linha.strip().split(',')
                if len(partes) == 2:
                    nome, quantidade = partes
                    if nome in componentes:
                        componentes[nome] = int(quantidade)
                    elif 'quantidade_desejada' in nome:
                        globals()[nome] = int(quantidade)

def atualizar_componentes(nova_quantidade, componente):
    if componente in componentes:
        componentes[componente] = nova_quantidade
        salvar_componentes()  # Salvar automaticamente após atualização
    else:
        raise ValueError("Componente não encontrado")

# Carregar os dados ao iniciar o módulo
carregar_componentes()




# Quantidade original
# placas = 29
# caixinha = 16
# arduino_micro = 1
# botao_amarelo = 7
# botao_vermelho = 4
# resistor470R = 7
# resistor1k = 33
# encaixe_femea12pinos = 8
# encaixe_macho4pinos = 137
# leds = 13
# rele5V = 17
# capacitor10v = 27
# conectorRCA = 15
# caboUSB_3M = 0
# caboUSB_1M = 0