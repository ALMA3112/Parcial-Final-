# Generated from Matrices.g4 by ANTLR 4.13.1
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
        4,1,12,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,3,4,47,8,4,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,64,8,6,10,6,12,6,67,9,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,5,8,76,8,8,10,8,12,8,79,9,8,1,8,0,1,8,9,0,2,4,
        6,8,10,12,14,16,0,0,77,0,21,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,
        38,1,0,0,0,8,46,1,0,0,0,10,56,1,0,0,0,12,60,1,0,0,0,14,68,1,0,0,
        0,16,72,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,
        25,1,1,0,0,0,26,27,3,4,2,0,27,28,5,1,0,0,28,33,1,0,0,0,29,30,3,6,
        3,0,30,31,5,1,0,0,31,33,1,0,0,0,32,26,1,0,0,0,32,29,1,0,0,0,33,3,
        1,0,0,0,34,35,5,10,0,0,35,36,5,2,0,0,36,37,3,8,4,0,37,5,1,0,0,0,
        38,39,5,3,0,0,39,40,5,4,0,0,40,41,5,10,0,0,41,42,5,5,0,0,42,7,1,
        0,0,0,43,44,6,4,-1,0,44,47,3,10,5,0,45,47,5,10,0,0,46,43,1,0,0,0,
        46,45,1,0,0,0,47,53,1,0,0,0,48,49,10,1,0,0,49,50,5,6,0,0,50,52,3,
        8,4,2,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,
        9,1,0,0,0,55,53,1,0,0,0,56,57,5,7,0,0,57,58,3,12,6,0,58,59,5,8,0,
        0,59,11,1,0,0,0,60,65,3,14,7,0,61,62,5,9,0,0,62,64,3,14,7,0,63,61,
        1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,13,1,0,0,0,
        67,65,1,0,0,0,68,69,5,7,0,0,69,70,3,16,8,0,70,71,5,8,0,0,71,15,1,
        0,0,0,72,77,5,11,0,0,73,74,5,9,0,0,74,76,5,11,0,0,75,73,1,0,0,0,
        76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,17,1,0,0,0,79,77,1,
        0,0,0,6,21,32,46,53,65,77
    ]

class MatricesParser ( Parser ):

    grammarFileName = "Matrices.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'imprimir'", "'('", "')'", 
                     "'*'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFICADOR", "NUMERO", 
                      "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_impresion = 3
    RULE_expresion = 4
    RULE_matriz = 5
    RULE_filas = 6
    RULE_fila = 7
    RULE_numeros = 8

    ruleNames =  [ "programa", "sentencia", "asignacion", "impresion", "expresion", 
                   "matriz", "filas", "fila", "numeros" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    IDENTIFICADOR=10
    NUMERO=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MatricesParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatricesParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MatricesParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MatricesParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MatricesParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==10:
                self.state = 18
                self.sentencia()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(MatricesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(MatricesParser.AsignacionContext,0)


        def impresion(self):
            return self.getTypedRuleContext(MatricesParser.ImpresionContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = MatricesParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.asignacion()
                self.state = 27
                self.match(MatricesParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.impresion()
                self.state = 30
                self.match(MatricesParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(MatricesParser.IDENTIFICADOR, 0)

        def expresion(self):
            return self.getTypedRuleContext(MatricesParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = MatricesParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MatricesParser.IDENTIFICADOR)
            self.state = 35
            self.match(MatricesParser.T__1)
            self.state = 36
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(MatricesParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return MatricesParser.RULE_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpresion" ):
                listener.enterImpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpresion" ):
                listener.exitImpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpresion" ):
                return visitor.visitImpresion(self)
            else:
                return visitor.visitChildren(self)




    def impresion(self):

        localctx = MatricesParser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MatricesParser.T__2)
            self.state = 39
            self.match(MatricesParser.T__3)
            self.state = 40
            self.match(MatricesParser.IDENTIFICADOR)
            self.state = 41
            self.match(MatricesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matriz(self):
            return self.getTypedRuleContext(MatricesParser.MatrizContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(MatricesParser.IDENTIFICADOR, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatricesParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MatricesParser.ExpresionContext,i)


        def getRuleIndex(self):
            return MatricesParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatricesParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 44
                self.matriz()
                pass
            elif token in [10]:
                self.state = 45
                self.match(MatricesParser.IDENTIFICADOR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatricesParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 48
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 49
                    self.match(MatricesParser.T__5)
                    self.state = 50
                    self.expresion(2) 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filas(self):
            return self.getTypedRuleContext(MatricesParser.FilasContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = MatricesParser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_matriz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MatricesParser.T__6)
            self.state = 57
            self.filas()
            self.state = 58
            self.match(MatricesParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fila(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatricesParser.FilaContext)
            else:
                return self.getTypedRuleContext(MatricesParser.FilaContext,i)


        def getRuleIndex(self):
            return MatricesParser.RULE_filas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilas" ):
                listener.enterFilas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilas" ):
                listener.exitFilas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilas" ):
                return visitor.visitFilas(self)
            else:
                return visitor.visitChildren(self)




    def filas(self):

        localctx = MatricesParser.FilasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_filas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.fila()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 61
                self.match(MatricesParser.T__8)
                self.state = 62
                self.fila()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeros(self):
            return self.getTypedRuleContext(MatricesParser.NumerosContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_fila

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFila" ):
                listener.enterFila(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFila" ):
                listener.exitFila(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFila" ):
                return visitor.visitFila(self)
            else:
                return visitor.visitChildren(self)




    def fila(self):

        localctx = MatricesParser.FilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fila)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MatricesParser.T__6)
            self.state = 69
            self.numeros()
            self.state = 70
            self.match(MatricesParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(MatricesParser.NUMERO)
            else:
                return self.getToken(MatricesParser.NUMERO, i)

        def getRuleIndex(self):
            return MatricesParser.RULE_numeros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeros" ):
                listener.enterNumeros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeros" ):
                listener.exitNumeros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeros" ):
                return visitor.visitNumeros(self)
            else:
                return visitor.visitChildren(self)




    def numeros(self):

        localctx = MatricesParser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_numeros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MatricesParser.NUMERO)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 73
                self.match(MatricesParser.T__8)
                self.state = 74
                self.match(MatricesParser.NUMERO)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




