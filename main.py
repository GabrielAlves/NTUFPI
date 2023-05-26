import antlr4

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog as fd, messagebox as msg

from random import randint

class NTUFPIGUI:
    def __init__(self):
        self.ultimo_arquivo_analisado = ""
        self.criar_widgets()

    def criar_widgets(self):
        self.criar_janela()
        self.criar_frame1()
        self.criar_treeview_de_tokens()

    def criar_janela(self):
        self.janela = tk.Tk()
        self.configurar_janela()

    def configurar_janela(self):
        self.janela.title("NT-UFPI")
        self.janela.geometry("450x475")
        self.janela.resizable(False, False)
        self.janela.iconbitmap(self.janela, "img/ufpi_brasao.ico")

    def criar_frame1(self):
        self.frame1 = ttk.Frame(self.janela)
        self.frame1.pack(pady = 10)
        self.criar_widgets_do_frame1()

    def criar_widgets_do_frame1(self):
        self.criar_botao_de_selecao_de_arquivo()
        self.criar_campo_com_filename()
        self.criar_campo_com_texto_do_arquivo()

    def criar_botao_de_selecao_de_arquivo(self):
        self.botao_de_selecao_de_arquivo = ttk.Button(self.frame1, text="Selecionar arquivo", command = self.selecionar_arquivo)
        self.botao_de_selecao_de_arquivo.grid(row=0, column=0, padx = 3, sticky = tk.NSEW)

    def selecionar_arquivo(self):
        filename = fd.askopenfilename(title = "Selecione um arquivo", filetypes = [('text files', '*.txt')])
        self.escrever_filename_no_campo(filename)

        with open(filename, mode = "r", encoding = "utf-8") as arquivo:
            texto = arquivo.read()

        self.escrever_texto_do_arquivo_no_campo(texto)
        self.extrair_tokens()

    def escrever_filename_no_campo(self, filename):
        self.campo_com_filename.configure(state="normal")
        self.campo_com_filename.delete(0, tk.END)
        self.campo_com_filename.insert(0, filename)
        self.campo_com_filename.configure(state="readonly")

    def escrever_texto_do_arquivo_no_campo(self, texto):
        self.campo_com_texto_do_arquivo.configure(state="normal")
        self.campo_com_texto_do_arquivo.delete("1.0", tk.END)
        self.campo_com_texto_do_arquivo.insert("1.0", texto)
        self.campo_com_texto_do_arquivo.configure(state="disabled")

    def criar_campo_com_filename(self):
        self.campo_com_filename = ttk.Entry(self.frame1)
        self.campo_com_filename.grid(row=0, column=1, padx = 3, sticky = tk.NSEW)
        self.frame1.columnconfigure(1, weight=1)
        self.campo_com_filename.configure(state="readonly")

    def criar_campo_com_texto_do_arquivo(self):
        self.campo_com_texto_do_arquivo = scrolledtext.ScrolledText(self.frame1, width = 40, height=7, font=("Arial", 12),wrap=tk.WORD)
        self.campo_com_texto_do_arquivo.grid(row = 1, columnspan = 2, pady = 5)
        self.campo_com_texto_do_arquivo.config(state="disabled")

    def criar_treeview_de_tokens(self):
        self.treeview_de_tokens = ttk.Treeview(self.janela)
        self.definir_colunas_da_treeview()
        self.definir_barra_de_titulo_da_treeview()
        self.treeview_de_tokens.pack(pady = 5)

    def definir_colunas_da_treeview(self):
        self.treeview_de_tokens["columns"] = ("Token", "Tipo")
        self.treeview_de_tokens.column("#0", width=0, minwidth=0)
        self.treeview_de_tokens.column("Token", width=120, minwidth=90, anchor=tk.W)
        self.treeview_de_tokens.column("Tipo", width=120, minwidth=90, anchor=tk.W)

    def definir_barra_de_titulo_da_treeview(self):
        self.treeview_de_tokens.heading("#0", text="", anchor=tk.W)
        self.treeview_de_tokens.heading("Token", text="Token", anchor=tk.W)
        self.treeview_de_tokens.heading("Tipo", text="Tipo", anchor=tk.W)

    def limpar_treeview(self):
        for item in self.treeview_de_tokens.get_children():
            self.treeview_de_tokens.delete(item)

    def preencher_treeview(self):
        palavras = self.campo_com_texto_do_arquivo.get("1.0", tk.END).split()

        for i, palavra in enumerate(palavras):
            self.treeview_de_tokens.insert(parent="", index="end", iid=i, values=(palavra, f"Tipo {randint(1, 9)}"))

    def extrair_tokens(self):
        # Só modifica a treeview se um novo arquivo for selecionado.
        if self.campo_com_filename.get() != self.ultimo_arquivo_analisado:
            self.ultimo_arquivo_analisado = self.campo_com_filename.get()

            self.limpar_treeview()
            self.preencher_treeview()

if __name__ == "__main__":
    gui = NTUFPIGUI()
    gui.janela.mainloop()