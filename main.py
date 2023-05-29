import antlr4
from gen.NTUFPILexer import NTUFPILexer
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog as fd, messagebox as msg
import threading

class NTUFPIGUI:
    def __init__(self):
        self.criar_widgets()
        self.definir_teclas_de_atalho()
        self.dicionario_de_tipos = {
            "PALAVRA" : "Palavra",
            "ESTADO" : "Estado",
            "SIGLA" : "Sigla",
            "ARTIGO" : "Artigo",
            "NUMERO" : "Número",
            "DIA_DA_SEMANA" : "Dia da semana",
            "MES" : "Mês",
            "HORARIO" : "Horário",
            "DATA" : "Data",
            "ADVERBIO" : "Advérbio",
            "PORCENTAGEM" : "Porcentagem",
            "PONTUACAO" : "Pontuação",
            "ABREVIACAO" : "Abreviação",
            "PONTO_FINAL" : "Ponto final",
            "DINHEIRO" : "Dinheiro",
            "NOME_PROPRIO" : "Nome próprio",
            "Space" : "Espaço",
            "PREPOSICAO" : "Preposição",
            "PRONOME": "Pronome",
            "CIDADE" : "Cidade",
            "TEMPO" : "Tempo",
            "CONJUNCAO" : "Conjunção"
        }

        self.tokens_extraidos = []

    def criar_widgets(self):
        self.criar_janela()
        self.criar_frame1()
        self.criar_frame2()
        self.criar_frame3()

    def criar_janela(self):
        self.janela = tk.Tk()
        self.configurar_janela()

    def configurar_janela(self):
        self.janela.title("NT-UFPI")
        self.janela.geometry("450x525")
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
        self.escrever_texto_do_arquivo_no_campo(filename)
        self.extrair_tokens()

    def escrever_filename_no_campo(self, filename):
        self.campo_com_filename.configure(state="normal")
        self.campo_com_filename.delete(0, tk.END)
        self.campo_com_filename.insert(0, filename)
        self.campo_com_filename.configure(state="readonly")

    def escrever_texto_do_arquivo_no_campo(self, filename):
        with open(filename, mode = "r", encoding = "utf-8") as arquivo:
            texto = arquivo.read()

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

    def criar_frame2(self):
        self.frame2 = ttk.Frame(self.janela)
        self.frame2.pack(pady=1)
        self.criar_widgets_do_frame2()

    def criar_widgets_do_frame2(self):
        self.criar_treeview_de_tokens()
        self.criar_label_de_pesquisa_de_token()
        self.criar_campo_de_pesquisa_de_token()
        self.criar_label_de_pesquisa_de_tipo()
        self.criar_campo_de_pesquisa_de_tipo()

    def criar_treeview_de_tokens(self):
        self.treeview_de_tokens = ttk.Treeview(self.frame2)
        self.definir_colunas_da_treeview()
        self.definir_barra_de_titulo_da_treeview()
        self.treeview_de_tokens.grid(row = 0, columnspan = 2, pady = 5)

    def definir_colunas_da_treeview(self):
        self.treeview_de_tokens["columns"] = ("Token", "Tipo")
        self.treeview_de_tokens.column("#0", width=0, minwidth=0)
        self.treeview_de_tokens.column("Token", width=120, minwidth=90, anchor=tk.W)
        self.treeview_de_tokens.column("Tipo", width=120, minwidth=90, anchor=tk.W)

    def definir_barra_de_titulo_da_treeview(self):
        self.treeview_de_tokens.heading("#0", text="", anchor=tk.W)
        self.treeview_de_tokens.heading("Token", text="Token", anchor=tk.W)
        self.treeview_de_tokens.heading("Tipo", text="Tipo", anchor=tk.W)

    def criar_label_de_pesquisa_de_token(self):
        self.label_de_pesquisa_de_token = ttk.Label(self.frame2, text = "Token", font = ("Arial", 12))
        self.label_de_pesquisa_de_token.grid(row=1, column=0, pady=3)

    def criar_campo_de_pesquisa_de_token(self):
        self.campo_de_pesquisa_de_token = ttk.Entry(self.frame2)
        self.campo_de_pesquisa_de_token.grid(row = 1, column = 1, pady=3)

    def criar_label_de_pesquisa_de_tipo(self):
        self.label_de_pesquisa_de_tipo = ttk.Label(self.frame2, text = "Tipo", font = ("Arial", 12))
        self.label_de_pesquisa_de_tipo.grid(row=2, column=0)

    def criar_campo_de_pesquisa_de_tipo(self):
        self.campo_de_pesquisa_de_tipo = ttk.Entry(self.frame2)
        self.campo_de_pesquisa_de_tipo.grid(row = 2, column = 1)

    def criar_frame3(self):
        self.frame3 = ttk.Frame(self.janela)
        self.frame3.pack(pady=10)
        self.criar_widgets_do_frame3()

    def criar_widgets_do_frame3(self):
        self.criar_botao_de_filtragem()

    def criar_botao_de_filtragem(self):
        self.botao_de_filtragem = ttk.Button(self.frame3, text="Filtrar",
                                                      command= lambda : self.filtrar_tokens(""))
        self.botao_de_filtragem.pack()

    def limpar_treeview(self):
        for item in self.treeview_de_tokens.get_children():
            self.treeview_de_tokens.delete(item)

    def preencher_treeview_pela_primeira_vez(self):
        filename = self.campo_com_filename.get()
        palavras = antlr4.FileStream(filename, encoding = "utf-8")
        lexer = NTUFPILexer(palavras)

        for i, token in enumerate(lexer.getAllTokens()):
            tipo = lexer.ruleNames[token.type - 1]

            if tipo == "T__0":
                continue

            tipo = self.dicionario_de_tipos[tipo]
            token = token.text

            self.tokens_extraidos.append((token, tipo))
            self.treeview_de_tokens.insert(parent="", index="end", iid=i, values=(token, tipo))

    def preencher_treeview_apos_primeira_vez(self, token_pesquisado, tipo_pesquisado):
        for i, token in enumerate(self.tokens_extraidos):
            tipo = token[1]
            token = token[0]

            if tipo_pesquisado in tipo and token_pesquisado in token:
                self.treeview_de_tokens.insert(parent="", index="end", iid=i, values=(token, tipo))

    def extrair_tokens(self):
        self.limpar_treeview()
        self.preencher_treeview_pela_primeira_vez()

    def filtrar_tokens(self, evento):
        self.limpar_treeview()
        token_pesquisado = self.campo_de_pesquisa_de_token.get()
        tipo_pesquisado = self.campo_de_pesquisa_de_tipo.get()
        self.preencher_treeview_apos_primeira_vez(token_pesquisado, tipo_pesquisado)

    def definir_teclas_de_atalho(self):
        self.janela.bind("<Return>", self.filtrar_tokens)

if __name__ == "__main__":
    gui = NTUFPIGUI()
    gui.janela.mainloop()