from lexer import Lexer
from analisys import Parser

text_input = """1. A, C def A
2. ~A def ~ 1
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser(state=text_input)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)