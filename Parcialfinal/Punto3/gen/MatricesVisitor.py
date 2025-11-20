# Generated from Matrices.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatricesParser import MatricesParser
else:
    from MatricesParser import MatricesParser

# This class defines a complete generic visitor for a parse tree produced by MatricesParser.

class MatricesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatricesParser#programa.
    def visitPrograma(self, ctx:MatricesParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#sentencia.
    def visitSentencia(self, ctx:MatricesParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#asignacion.
    def visitAsignacion(self, ctx:MatricesParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#impresion.
    def visitImpresion(self, ctx:MatricesParser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#expresion.
    def visitExpresion(self, ctx:MatricesParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#matriz.
    def visitMatriz(self, ctx:MatricesParser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#filas.
    def visitFilas(self, ctx:MatricesParser.FilasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#fila.
    def visitFila(self, ctx:MatricesParser.FilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#numeros.
    def visitNumeros(self, ctx:MatricesParser.NumerosContext):
        return self.visitChildren(ctx)



del MatricesParser