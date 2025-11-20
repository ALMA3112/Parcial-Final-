
import sys
from antlr4 import FileStream, CommonTokenStream
from MatricesLexer import MatricesLexer
from MatricesParser import MatricesParser
from MatricesVisitor import MatricesVisitor

class ValorMatriz:
    def __init__(self, filas, columnas, valor):
        self.filas = filas
        self.columnas = columnas
        self.valor = valor 

    def __repr__(self):
        return f"Matriz({self.filas}x{self.columnas}, {self.valor})"

class EvaluadorVisitor(MatricesVisitor):

    def __init__(self):
        self.entorno = {}  

    def visitPrograma(self, ctx):
        for st in ctx.sentencia():
            self.visit(st)
        return None

    def visitAsignacion(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.entorno[nombre] = valor
        return valor

    def visitImpresion(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre not in self.entorno:
            print(f"Error: variable '{nombre}' no definida")
        else:
            m = self.entorno[nombre]
            print(f"{nombre} ({m.filas} × {m.columnas}):")
            for fila in m.valor:
                print("  " + str(fila))

    def visitExpresion(self, ctx):
        if ctx.matriz():
            return self.visit(ctx.matriz())
        if ctx.IDENTIFICADOR():
            nombre = ctx.IDENTIFICADOR().getText()
            if nombre not in self.entorno:
                raise Exception(f"Variable '{nombre}' no definida")
            return self.entorno[nombre]
        if len(ctx.expresion()) == 2:
            izquierda = self.visit(ctx.expresion(0))
            derecha = self.visit(ctx.expresion(1))
            return self.multiplicar(izquierda, derecha)
        raise Exception("Expresion no reconocida")

    def visitMatriz(self, ctx):
        lista_filas = [self.visit(f) for f in ctx.filas().fila()]
        if len(lista_filas) == 0:
            raise Exception("Matriz vacia no permitida")
        num_columnas = len(lista_filas[0])
        for fila in lista_filas:
            if len(fila) != num_columnas:
                raise Exception("Filas con diferente longitud en la matriz literal")
        return ValorMatriz(len(lista_filas), num_columnas, lista_filas)

    def visitFilas(self, ctx):
        return [self.visit(r) for r in ctx.filas().row()] 

    def visitFila(self, ctx):
        lista_num = []
        for nctx in ctx.numeros().NUMERO():
            texto = nctx.getText()
            if '.' in texto:
                lista_num.append(float(texto))
            else:
                lista_num.append(int(texto))
        return lista_num

    def multiplicar(self, A: ValorMatriz, B: ValorMatriz) -> ValorMatriz:
        if A.columnas != B.filas:
            raise Exception(f"Dimensiones incompatibles: {A.filas}x{A.columnas} * {B.filas}x{B.columnas}")

        m = A.filas
        n = A.columnas
        p = B.columnas
        C = [[0 for _ in range(p)] for _ in range(m)]

        for i in range(m):
            for j in range(p):
                suma = 0
                for k in range(n):
                    suma += A.valor[i][k] * B.valor[k][j]
                C[i][j] = suma

        return ValorMatriz(m, p, C)


def main(argv):
    if len(argv) < 2:
        return

    entrada = FileStream(argv[1], encoding='utf-8')
    lexer = MatricesLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = MatricesParser(tokens)
    arbol = parser.programa()

    visitor = EvaluadorVisitor()
    visitor.visit(arbol)


if __name__ == "__main__":
    main(sys.argv)
