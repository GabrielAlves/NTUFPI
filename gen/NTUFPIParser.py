# Generated from C:/Users/Gabriel/PycharmProjects/NTUFPI\NTUFPI.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,33,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,4,1,15,8,1,11,1,12,1,16,1,1,5,1,20,8,1,10,1,12,1,23,9,1,
        1,2,5,2,26,8,2,10,2,12,2,29,9,2,1,2,1,2,1,2,0,0,3,0,2,4,0,1,2,0,
        2,13,15,17,33,0,7,1,0,0,0,2,14,1,0,0,0,4,27,1,0,0,0,6,8,3,2,1,0,
        7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,
        12,5,0,0,1,12,1,1,0,0,0,13,15,3,4,2,0,14,13,1,0,0,0,15,16,1,0,0,
        0,16,14,1,0,0,0,16,17,1,0,0,0,17,21,1,0,0,0,18,20,5,1,0,0,19,18,
        1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,3,1,0,0,0,23,
        21,1,0,0,0,24,26,7,0,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,
        0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,14,0,0,31,5,
        1,0,0,0,4,9,16,21,27
    ]

class NTUFPIParser ( Parser ):

    grammarFileName = "NTUFPI.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ESTADO", "SIGLA", "ARTIGO", 
                      "NUMERO", "DIA_DA_SEMANA", "MES", "HORARIO", "DATA", 
                      "ADVERBIO", "PORCENTAGEM", "PONTUACAO", "ABREVIACAO", 
                      "PONTO_FINAL", "DINHEIRO", "NOME_PROPRIO", "PALAVRA", 
                      "Space" ]

    RULE_noticia = 0
    RULE_paragrafo = 1
    RULE_frase = 2

    ruleNames =  [ "noticia", "paragrafo", "frase" ]

    EOF = Token.EOF
    T__0=1
    ESTADO=2
    SIGLA=3
    ARTIGO=4
    NUMERO=5
    DIA_DA_SEMANA=6
    MES=7
    HORARIO=8
    DATA=9
    ADVERBIO=10
    PORCENTAGEM=11
    PONTUACAO=12
    ABREVIACAO=13
    PONTO_FINAL=14
    DINHEIRO=15
    NOME_PROPRIO=16
    PALAVRA=17
    Space=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NoticiaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NTUFPIParser.EOF, 0)

        def paragrafo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NTUFPIParser.ParagrafoContext)
            else:
                return self.getTypedRuleContext(NTUFPIParser.ParagrafoContext,i)


        def getRuleIndex(self):
            return NTUFPIParser.RULE_noticia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoticia" ):
                listener.enterNoticia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoticia" ):
                listener.exitNoticia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoticia" ):
                return visitor.visitNoticia(self)
            else:
                return visitor.visitChildren(self)




    def noticia(self):

        localctx = NTUFPIParser.NoticiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_noticia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.paragrafo()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 262140) != 0)):
                    break

            self.state = 11
            self.match(NTUFPIParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagrafoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def frase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NTUFPIParser.FraseContext)
            else:
                return self.getTypedRuleContext(NTUFPIParser.FraseContext,i)


        def getRuleIndex(self):
            return NTUFPIParser.RULE_paragrafo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagrafo" ):
                listener.enterParagrafo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagrafo" ):
                listener.exitParagrafo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParagrafo" ):
                return visitor.visitParagrafo(self)
            else:
                return visitor.visitChildren(self)




    def paragrafo(self):

        localctx = NTUFPIParser.ParagrafoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_paragrafo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 13
                    self.frase()

                else:
                    raise NoViableAltException(self)
                self.state = 16 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 18
                self.match(NTUFPIParser.T__0)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PONTO_FINAL(self):
            return self.getToken(NTUFPIParser.PONTO_FINAL, 0)

        def ARTIGO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.ARTIGO)
            else:
                return self.getToken(NTUFPIParser.ARTIGO, i)

        def PALAVRA(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.PALAVRA)
            else:
                return self.getToken(NTUFPIParser.PALAVRA, i)

        def DIA_DA_SEMANA(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.DIA_DA_SEMANA)
            else:
                return self.getToken(NTUFPIParser.DIA_DA_SEMANA, i)

        def MES(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.MES)
            else:
                return self.getToken(NTUFPIParser.MES, i)

        def HORARIO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.HORARIO)
            else:
                return self.getToken(NTUFPIParser.HORARIO, i)

        def ADVERBIO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.ADVERBIO)
            else:
                return self.getToken(NTUFPIParser.ADVERBIO, i)

        def PORCENTAGEM(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.PORCENTAGEM)
            else:
                return self.getToken(NTUFPIParser.PORCENTAGEM, i)

        def PONTUACAO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.PONTUACAO)
            else:
                return self.getToken(NTUFPIParser.PONTUACAO, i)

        def SIGLA(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.SIGLA)
            else:
                return self.getToken(NTUFPIParser.SIGLA, i)

        def NOME_PROPRIO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.NOME_PROPRIO)
            else:
                return self.getToken(NTUFPIParser.NOME_PROPRIO, i)

        def DINHEIRO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.DINHEIRO)
            else:
                return self.getToken(NTUFPIParser.DINHEIRO, i)

        def ESTADO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.ESTADO)
            else:
                return self.getToken(NTUFPIParser.ESTADO, i)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.NUMERO)
            else:
                return self.getToken(NTUFPIParser.NUMERO, i)

        def DATA(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.DATA)
            else:
                return self.getToken(NTUFPIParser.DATA, i)

        def ABREVIACAO(self, i:int=None):
            if i is None:
                return self.getTokens(NTUFPIParser.ABREVIACAO)
            else:
                return self.getToken(NTUFPIParser.ABREVIACAO, i)

        def getRuleIndex(self):
            return NTUFPIParser.RULE_frase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrase" ):
                listener.enterFrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrase" ):
                listener.exitFrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrase" ):
                return visitor.visitFrase(self)
            else:
                return visitor.visitChildren(self)




    def frase(self):

        localctx = NTUFPIParser.FraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_frase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 245756) != 0):
                self.state = 24
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245756) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(NTUFPIParser.PONTO_FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





