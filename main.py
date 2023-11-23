import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class DreamWatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DreamWatch - Sistema de Monitoramento de Sono")

        # Widgets
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(pady=10)

        self.botao_adicionar_noite = tk.Button(self.menu_frame, text="Adicionar Noite de Sono", command=self.adicionar_noite)
        self.botao_adicionar_noite.grid(row=0, column=0, padx=10)

        self.botao_visualizar = tk.Button(self.menu_frame, text="Visualizar Noites de Sono", command=self.visualizar_noites)
        self.botao_visualizar.grid(row=0, column=1, padx=10)

        self.botao_sair = tk.Button(self.menu_frame, text="Sair", command=self.root.destroy)
        self.botao_sair.grid(row=0, column=2, padx=10)

        # Inicializa as informações do arquivo
        self.arquivo_info = []

    def adicionar_noite(self):
        adicionar_janela = tk.Toplevel(self.root)
        adicionar_janela.title("Adicionar Noite de Sono")

        label_temperatura = tk.Label(adicionar_janela, text="Temperatura Média:")
        label_temperatura.grid(row=0, column=0, padx=10, pady=10)

        self.entry_temperatura = tk.Entry(adicionar_janela)
        self.entry_temperatura.grid(row=0, column=1, padx=10, pady=10)

        label_umidade = tk.Label(adicionar_janela, text="Umidade Média:")
        label_umidade.grid(row=1, column=0, padx=10, pady=10)

        self.entry_umidade = tk.Entry(adicionar_janela)
        self.entry_umidade.grid(row=1, column=1, padx=10, pady=10)

        label_movimentos = tk.Label(adicionar_janela, text="Quantidade de Movimentos:")
        label_movimentos.grid(row=2, column=0, padx=10, pady=10)

        self.entry_movimentos = tk.Entry(adicionar_janela)
        self.entry_movimentos.grid(row=2, column=1, padx=10, pady=10)

        label_boa_noite = tk.Label(adicionar_janela, text="Boa Noite de Sono?")
        label_boa_noite.grid(row=3, column=0, padx=10, pady=10)

        self.var_boa_noite = tk.BooleanVar()
        self.checkbox_boa_noite = tk.Checkbutton(adicionar_janela, variable=self.var_boa_noite)
        self.checkbox_boa_noite.grid(row=3, column=1, padx=10, pady=10)

        botao_confirmar = tk.Button(adicionar_janela, text="Confirmar", command=self.confirmar_adicao)
        botao_confirmar.grid(row=4, column=0, columnspan=2, pady=10)

    def confirmar_adicao(self):
        temperatura = self.entry_temperatura.get()
        umidade = self.entry_umidade.get()
        movimentos = self.entry_movimentos.get()
        boa_noite = self.var_boa_noite.get()

        if temperatura.replace(".", "").isdigit() and umidade.replace(".", "").isdigit() and movimentos.isdigit():
            # Cria um novo objeto JSON para a noite atual
            noite_info = {
                'Numero': len(self.arquivo_info) + 1,
                'Data': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Temperatura_Media': float(temperatura),
                'Umidade_Media': float(umidade),
                'Movimentos': int(movimentos),
                'Boa_Noite': boa_noite
            }

            # Adiciona o novo objeto à lista
            self.arquivo_info.append(noite_info)

            # Salva as informações no arquivo
            with open('info_noite.json', 'w') as arquivo:
                json.dump(self.arquivo_info, arquivo, indent=2)

            messagebox.showinfo("Sucesso", "Noite de Sono adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Entrada inválida. Certifique-se de fornecer todas as informações corretamente.")

    def visualizar_noites(self):
        visualizar_janela = tk.Toplevel(self.root)
        visualizar_janela.title("Visualizar Noites de Sono")

        try:
            with open('info_noite.json', 'r') as arquivo:
                conteudo = arquivo.read()
                label_info = tk.Label(visualizar_janela, text=conteudo)
                label_info.pack(padx=10, pady=10)
        except FileNotFoundError:
            messagebox.showinfo("Informação", "Nenhuma Noite de Sono foi registrada ainda.")
            visualizar_janela.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = DreamWatchApp(root)
    root.mainloop()
