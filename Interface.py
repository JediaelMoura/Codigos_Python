import tkinter as tk
from tkinter import messagebox
import Componentes

# quantidade_desejada_bpulse = 10
# quantidade_desejada_bplay = 10


def calcular_bepulse():
    placas_por_bepulse = 1
    caixinha_por_bepulse = 1
    arduino_micro_por_bepulse = 1
    resistor470r_por_bepulse = 1
    resistor1k_por_bepulse = 1
    capacitor10v_por_bepulse = 1
    encaixe_femea12pinos_por_bepulse = 2
    rele5v_por_bepulse = 1
    conectorrca_por_bepulse = 1
    cabousb_3m_por_bepulse = 1

    # Acessando os valores pelo dicionário componentes
    bepulse = min(Componentes.componentes['placas'] // placas_por_bepulse,
                  Componentes.componentes['caixinha'] // caixinha_por_bepulse,
                  Componentes.componentes['arduino_micro'] // arduino_micro_por_bepulse,
                  Componentes.componentes['resistor470R'] // resistor470r_por_bepulse,
                  Componentes.componentes['resistor1k'] // resistor1k_por_bepulse,
                  Componentes.componentes['capacitor10v'] // capacitor10v_por_bepulse,
                  Componentes.componentes['encaixe_femea12pinos'] // encaixe_femea12pinos_por_bepulse,
                  Componentes.componentes['rele5V'] // rele5v_por_bepulse,
                  Componentes.componentes['conectorRCA'] // conectorrca_por_bepulse,
                  Componentes.componentes['caboUSB_3M'] // cabousb_3m_por_bepulse)

    maisdeum = 's' if bepulse != 1 else ''
    complemento = 'os' if bepulse == Componentes.quantidade_desejada_bpulse else ''
    resultado_bepulse_label.config(text=f"Com o que temos disponível, é possível montar {complemento} {bepulse} bePulse{maisdeum}.")

    calcular_faltantes_bepulse()

def calcular_faltantes_bepulse():
    # Usando o dicionário 'componentes' para acessar os valores
    componentes_bepulse = {
        'Placas': Componentes.componentes['placas'],
        'Caixinhas': Componentes.componentes['caixinha'],
        'Arduino Pro Micro USB-C': Componentes.componentes['arduino_micro'],
        'Resistor 470r': Componentes.componentes['resistor470R'],
        'Resistor 1k': Componentes.componentes['resistor1k'],
        'Capacitor 10v': Componentes.componentes['capacitor10v'],
        'Encaixes fêmeas 12 pinos': Componentes.componentes['encaixe_femea12pinos'],
        'Rele 5v': Componentes.componentes['rele5V'],
        'Conector RCA': Componentes.componentes['conectorRCA'],
        'Cabo USB 3m': Componentes.componentes['caboUSB_3M']
    }
    maisdeum = 's' if Componentes.quantidade_desejada_bpulse != 1 else ''

    contagem_faltantes_bepulse = {}

    for componente, quantidade_disponivel in componentes_bepulse.items():
        # Define a quantidade necessária
        quantidade_necessaria = 2 if componente == 'Encaixes fêmeas de 12 pinos' else 1
        quantidade_necessaria *= Componentes.quantidade_desejada_bpulse

        if quantidade_disponivel < quantidade_necessaria:
            contagem_faltantes_bepulse[componente] = quantidade_necessaria - quantidade_disponivel

    if contagem_faltantes_bepulse:
        resultado_faltantes_label.config(
            text=f"Para ter {Componentes.quantidade_desejada_bpulse} unidades de bePulse em estoque, compre:")
        resultado_faltantes_text.delete(1.0, tk.END)
        for componente, contagem in contagem_faltantes_bepulse.items():
            resultado_faltantes_text.insert(tk.END, f"{contagem} unidade{maisdeum} de {componente}.\n")
    else:
        resultado_faltantes_label.config(text="Todos os componentes necessários estão disponíveis em estoque.")

def calcular_beplay():
    placas_por_beplay = 1
    caixinha_por_beplay = 1
    arduino_micro_por_beplay = 1
    resistor470r_por_beplay = 5
    encaixe_femea12pinos_por_beplay = 2
    encaixe_macho4pinos_por_beplay = 5
    botao_amarelo_por_beplay = 4
    botao_vermelho_por_beplay = 1
    cabousb_3m_por_beplay = 1

    beplay = min(Componentes.componentes['placas'] // placas_por_beplay,
                 Componentes.componentes['caixinha'] // caixinha_por_beplay,
                 Componentes.componentes['arduino_micro'] // arduino_micro_por_beplay,
                 Componentes.componentes['resistor470R'] // resistor470r_por_beplay,
                 Componentes.componentes['encaixe_femea12pinos'] // encaixe_femea12pinos_por_beplay,
                 Componentes.componentes['encaixe_macho4pinos'] // encaixe_macho4pinos_por_beplay,
                 Componentes.componentes['botao_amarelo'] // botao_amarelo_por_beplay,
                 Componentes.componentes['botao_vermelho'] // botao_vermelho_por_beplay,
                 Componentes.componentes['caboUSB_3M'] // cabousb_3m_por_beplay)

    maisdeum = 's' if beplay != 1 else ''

    complemento = 'os' if beplay == Componentes.quantidade_desejada_bplay else ''
    resultado_beplay_label.config(
        text=f"Com o que temos disponível, é possível montar {complemento} {beplay} bePlay{maisdeum}.")

    calcular_faltantes_beplay()

def calcular_faltantes_beplay():
    # Usa o dicionário 'componentes' para acessar os valores
    componentes_beplay = {
        'Placas': Componentes.componentes['placas'],
        'Caixinha': Componentes.componentes['caixinha'],
        'Arduínos': Componentes.componentes['arduino_micro'],
        'Resistor de 470R': Componentes.componentes['resistor470R'],
        'Encaixes fêmeas de 12 pinos': Componentes.componentes['encaixe_femea12pinos'],
        'Encaixes machos de 4 pinos': Componentes.componentes['encaixe_macho4pinos'],
        'Botões Amarelos': Componentes.componentes['botao_amarelo'],
        'Botões Vermelhos': Componentes.componentes['botao_vermelho'],
        'Cabo USB 3M': Componentes.componentes['caboUSB_3M']
    }

    maisdeum = 's' if Componentes.quantidade_desejada_bplay != 1 else ''

    contagem_faltantes_beplay = {}
    for componente, quantidade_disponivel in componentes_beplay.items():
        # Calcula a quantidade necessária para 10 unidades
        quantidade_necessaria = {
            'Resistor de 470R': 5,
            'Encaixes machos de 4 pinos': 5,
            'Botões Amarelos': 4,
            'Encaixes fêmeas de 12 pinos': 2
        }.get(componente, 1) * Componentes.quantidade_desejada_bplay

        if quantidade_disponivel < quantidade_necessaria:
            contagem_faltantes_beplay[componente] = quantidade_necessaria - quantidade_disponivel

    if contagem_faltantes_beplay:
        resultado_faltantes_bePlay_label.config(
            text=f"Para ter {Componentes.quantidade_desejada_bplay} unidades de bePlay em estoque, compre:")
        resultado_faltantes_bePlay_text.delete(1.0, tk.END)
        for componente, contagem in contagem_faltantes_beplay.items():
            resultado_faltantes_bePlay_text.insert(tk.END, f"{contagem} unidade{maisdeum} de {componente}.\n")
    else:
        resultado_faltantes_bePlay_label.config(text="Todos os componentes necessários estão disponíveis em estoque.")


def abrir_gerenciador_componentes():
    Componentes.carregar_componentes()  # Esta função deve carregar os dados dos componentes do arquivo
    janela_componentes = tk.Toplevel()
    janela_componentes.title("Controle de Estoque")
    janela_componentes.geometry("500x600")
    janela_componentes.iconbitmap('./icones/components1.ico')

    lista_componentes = ['placas', 'caixinha', 'arduino_micro', 'botao_amarelo', 'botao_vermelho', 'resistor470R',
                         'resistor1k', 'encaixe_femea12pinos', 'encaixe_macho4pinos', 'leds', 'rele5V', 'capacitor10v',
                         'conectorRCA', 'caboUSB_3M', 'caboUSB_1M']

    # Dicionário para mapear os nomes técnicos para nomes amigáveis
    nomes_amigaveis = {
        'placas': 'Placas Base',
        'caixinha': 'Caixas Protetoras',
        'arduino_micro': 'Arduino Pro Micro USB-C',
        'botao_amarelo': 'Botões Amarelos',
        'botao_vermelho': 'Botões Vermelhos',
        'resistor470R': 'Resistores 470 Ohm',
        'resistor1k': 'Resistores 1K Ohm',
        'encaixe_femea12pinos': 'Encaixes Fêmeas 12 pinos',
        'encaixe_macho4pinos': 'Encaixes Machos 4 pinos',
        'leds': 'LEDs',
        'rele5V': 'Relés 5V',
        'capacitor10v': 'Capacitores 10V',
        'conectorRCA': 'Conectores RCA',
        'caboUSB_3M': 'Cabos USB 3M',
        'caboUSB_1M': 'Cabos USB 1M'
    }

    entries_adicionar = {}
    entries_subtrair = {}
    labels_quantidade = {}


    for index, componente in enumerate(lista_componentes):
        nome_amigavel = nomes_amigaveis.get(componente,
                                            componente)  # Pega o nome amigável ou usa o técnico se não encontrado
        tk.Label(janela_componentes, text=nome_amigavel).grid(row=index, column=0, padx=10, pady=5)

        entry_sub = tk.Entry(janela_componentes, width=5)
        entry_sub.grid(row=index, column=1, padx=10, pady=5)
        entries_subtrair[componente] = entry_sub

        label_quantidade = tk.Label(janela_componentes, text=str(Componentes.componentes[componente]))
        label_quantidade.grid(row=index, column=2, padx=10, pady=5)
        labels_quantidade[componente] = label_quantidade

        entry_add = tk.Entry(janela_componentes, width=5)
        entry_add.grid(row=index, column=3, padx=10, pady=5)
        entries_adicionar[componente] = entry_add

        btn_atualizar = tk.Button(janela_componentes, text="Atualizar",
                                  command=lambda c=componente: atualizar_estoque(c, entries_adicionar[c], entries_subtrair[c], labels_quantidade[c]))
        btn_atualizar.grid(row=index, column=4, padx=10, pady=5)


    janela_componentes.mainloop()

def atualizar_estoque(componente, entry_add, entry_sub, label_quantidade):
    adicionado = int(entry_add.get()) if entry_add.get() else 0
    subtraido = int(entry_sub.get()) if entry_sub.get() else 0
    nova_quantidade = Componentes.componentes[componente] + adicionado - subtraido
    Componentes.atualizar_componentes(nova_quantidade, componente)
    label_quantidade.config(text=str(nova_quantidade))
    entry_add.delete(0)
    entry_sub.delete(0)

# def atualizar_quantidades(entry_bpulse, entry_bplay):
#     Componentes.quantidade_desejada_bpulse = int(entry_bpulse.get())
#     Componentes.quantidade_desejada_bplay = int(entry_bplay.get())
#     messagebox.showinfo("Atualização", "Quantidades desejadas atualizadas com sucesso!")
#     Componentes.salvar_componentes()  # Salva os dados atualizados de volta ao arquivo ou base de dados

def atualizar_quantidade_bpulse(entry_bpulse):
    try:
        nova_quantidade = int(entry_bpulse.get())  # Converte o valor para inteiro
        Componentes.quantidade_desejada_bpulse = nova_quantidade  # Atualiza a quantidade desejada
        Componentes.salvar_componentes()  # Salva as alterações no arquivo de componentes
        messagebox.showinfo("Atualização", f"Quantidade de bePulse atualizada para: {nova_quantidade}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def atualizar_quantidade_bplay(entry_bplay):
    try:
        nova_quantidade = int(entry_bplay.get())  # Converte o valor para inteiro
        Componentes.quantidade_desejada_bplay = nova_quantidade  # Atualiza a quantidade desejada
        Componentes.salvar_componentes()  # Salva as alterações no arquivo de componentes
        messagebox.showinfo("Atualização", f"Quantidade de bePlay atualizada para: {nova_quantidade}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")


# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Componentes")
janela.geometry("850x530")  # Ajuste a largura para acomodar os dois painéis lado a lado
janela.iconbitmap('./icones/components1.ico')

# Definição dos Frames usando grid para layout lado a lado
bepulse_frame = tk.Frame(janela, borderwidth=2, relief="groove")
bepulse_frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

bePlay_frame = tk.Frame(janela, borderwidth=2, relief="groove")
bePlay_frame.grid(row=0, column=1, sticky="ns", padx=10, pady=10)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)

# Título para bePulse
tk.Label(bepulse_frame, text="------ bePulse ------", font=('Calibri', 13)).pack(pady=(0,10))

# Frame para centralizar os elementos de quantidade desejada
quantidade_frame = tk.Frame(bepulse_frame)
quantidade_frame.pack(pady=10)

# Elemento rótulo acima dos campos de entrada
tk.Label(quantidade_frame, text="Quantidade desejada de bePulse:").pack()

# Frame para entrada e botão, para centralizar horizontalmente
entrada_botao_frame = tk.Frame(quantidade_frame)
entrada_botao_frame.pack(pady=5)  # pequena distância vertical

entry_bpulse = tk.Entry(entrada_botao_frame, width=10)
entry_bpulse.pack(side='left', padx=5)  # Espaço entre a entrada e o botão
tk.Button(entrada_botao_frame, text="Atualizar", command=lambda: atualizar_quantidade_bpulse(entry_bpulse)).pack(side='left')

# Botão para visualizar resultado
tk.Button(bepulse_frame, text="Visualizar Resultado", command=calcular_bepulse).pack(pady=20)
resultado_bepulse_label = tk.Label(bepulse_frame, text="")
resultado_bepulse_label.pack()

# Área para mensagens de faltantes
resultado_faltantes_label = tk.Label(bepulse_frame, text="")
resultado_faltantes_label.pack()
resultado_faltantes_text = tk.Text(bepulse_frame, height=10, width=50)
resultado_faltantes_text.pack(pady=15)


# Título para bePlay
tk.Label(bePlay_frame, text="------ bePlay ------", font=('Calibri', 13)).pack(pady=(0,10))

# Frame para centralizar os elementos de quantidade desejada
quantidade_frame_beplay = tk.Frame(bePlay_frame)
quantidade_frame_beplay.pack(pady=10)

# Elemento rótulo acima dos campos de entrada
tk.Label(quantidade_frame_beplay, text="Quantidade desejada de bePlay:").pack()

# Frame para entrada e botão, para centralizar horizontalmente
entrada_botao_frame_beplay = tk.Frame(quantidade_frame_beplay)
entrada_botao_frame_beplay.pack(pady=5)  # pequena distância vertical

entry_bplay = tk.Entry(entrada_botao_frame_beplay, width=10)
entry_bplay.pack(side='left', padx=5)  # Espaço entre a entrada e o botão
tk.Button(entrada_botao_frame_beplay, text="Atualizar", command=lambda: atualizar_quantidade_bplay(entry_bplay)).pack(side='left')

# Botão para visualizar resultado
tk.Button(bePlay_frame, text="Visualizar Resultado", command=calcular_beplay).pack(pady=20)
resultado_beplay_label = tk.Label(bePlay_frame, text="")
resultado_beplay_label.pack()

# Área para mensagens de faltantes
resultado_faltantes_bePlay_label = tk.Label(bePlay_frame, text="")
resultado_faltantes_bePlay_label.pack()
resultado_faltantes_bePlay_text = tk.Text(bePlay_frame, height=10, width=50)
resultado_faltantes_bePlay_text.pack(pady=15)


btn_gerenciar_componentes = tk.Button(janela, text="Controle de Estoque", command=abrir_gerenciador_componentes)
btn_gerenciar_componentes.grid(row=1, column=0, columnspan=2, pady=20)  # Ajuste conforme necessário
btn_gerenciar_componentes.config(width=20, height=1)


janela.mainloop()