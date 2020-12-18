from io import StringIO
import sys
from sly import Lexer, Parser

class CalcLexer(Lexer):
    tokens = {NUMBER, PLUS, TIMES, LPAREN, RPAREN}
    ignore = ' \t'

    # Tokens
    NUMBER = r'\d+'

    # Special symbols
    PLUS = r'\+'
    TIMES = r'\*'
    LPAREN = r'\('
    RPAREN = r'\)'


class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', PLUS, TIMES),
        )

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)


class CalcParser2(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', TIMES),
        ('left', PLUS),
        )

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)


def evaluate(text: str) -> int:
    lexer = CalcLexer()
    parser = CalcParser()
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    parser.parse(lexer.tokenize(text))
    sys.stdout = old_stdout
    return int(mystdout.getvalue().strip())


def evaluate2(text: str) -> int:
    lexer = CalcLexer()
    parser = CalcParser2()
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    parser.parse(lexer.tokenize(text))
    sys.stdout = old_stdout
    return int(mystdout.getvalue().strip())


def main():
    lines = open('input.txt').read().splitlines()
    sum = 0
    for line in lines:
        sum += evaluate(line)
    print(f"Sum of lines is {sum}")
    sum = 0
    for line in lines:
        sum += evaluate2(line)
    print(f"Sum2 of lines is {sum}")

if __name__ == "__main__":
    main()
