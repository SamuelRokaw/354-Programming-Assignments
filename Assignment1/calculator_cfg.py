#Samuel Rokaw
#2444664
#rokaw@chapman.edu
#CPSC 354
#PA1
#
from lark import Lark, Transformer
import sys
import math

#Loads Grammar from grammar.lark
with open('grammar.lark', 'r') as grammar_file:
    grammar = grammar_file.read()

#Creates Lark parser
parser = Lark(grammar, parser='lalr')

#Transform CST to AST
class CalcTransformer(Transformer):
    def num(self, items):
        return float(items[0])

    def plus(self, items):
        return ('plus', items[0], items[1])

    def minus(self, items):
        return ('minus', items[0], items[1])

    def times(self, items):
        return ('times', items[0], items[1])
    
    def log(self, items):
        return ('log', items[0], items[1])

    def power(self, items):
        return ('power', items[0], items[1])

    def neg(self, items):
        return ('neg', items[0])

    def parenthesis(self, items):
        return items[0]


#Evaluate AST
def evaluate(ast):
    if isinstance(ast, (int, float)):
        return ast
    if ast[0] == 'plus':
        return evaluate(ast[1]) + evaluate(ast[2])
    elif ast[0] == 'minus':
        return evaluate(ast[1]) - evaluate(ast[2])
    elif ast[0] == 'times':
        return evaluate(ast[1]) * evaluate(ast[2])
    elif ast[0] == 'power':
        return evaluate(ast[1]) ** evaluate(ast[2])
    elif ast[0] == 'log':
        return math.log(evaluate(ast[1]), evaluate(ast[2]))
    elif ast[0] == 'neg':
        return -evaluate(ast[1])
    elif ast[0] == 'parenthesis':
        return evaluate(ast[1])
    elif ast[0] == 'num':
        return ast[1]
    else:
        raise ValueError(f"Unknown AST node: {ast[0]}")

#Main
if __name__ == "__main__":
    calc_transformer = CalcTransformer()
    input_string = sys.argv[1]
    cst = parser.parse(input_string)
    #print(cst)
    ast = calc_transformer.transform(cst)
    #print(ast)
    result = evaluate(ast)
    print(result)