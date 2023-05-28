# Generated from C:/Users/Gabriel/PycharmProjects/NTUFPI\NTUFPI.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NTUFPIParser import NTUFPIParser
else:
    from NTUFPIParser import NTUFPIParser

# This class defines a complete generic visitor for a parse tree produced by NTUFPIParser.

class NTUFPIVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NTUFPIParser#noticia.
    def visitNoticia(self, ctx:NTUFPIParser.NoticiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NTUFPIParser#paragrafo.
    def visitParagrafo(self, ctx:NTUFPIParser.ParagrafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NTUFPIParser#frase.
    def visitFrase(self, ctx:NTUFPIParser.FraseContext):
        return self.visitChildren(ctx)



del NTUFPIParser