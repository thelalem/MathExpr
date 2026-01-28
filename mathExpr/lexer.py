import math

# Token

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"
    
#lexer
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
    
    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
            
    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    
    def number(self):
        result = ''
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return Token('NUMBER', float(result))
    
    def identifier(self):
        result = ''
        while self.current_char and self.current_char.isalpha():
            result += self.current_char
            self.advance()
            
        if result == 'sin':
            return Token('SIN')
        elif result == 'cos':
            return Token('COS')
        elif result == 'sqrt':
            return Token('SQRT')
        elif result == 'pi':
            return Token('CONST_PI', math.pi)
        elif result == 'e':
            return Token('CONST_E', math.e)
        elif len(result) == 1:
            return Token('VAR', result)
        else:
            raise Exception(f"Unknown identifier: {result}")
            
    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit(): 
                return self.number()
            
            if self.current_char.isalpha():
                return self.identifier()
            
            if self.current_char == '+':
                self.advance()
                return Token('PLUS')
            if self.current_char == '-':
                self.advance()
                return Token('MINUS')
            if self.current_char == '*':
                self.advance()
                return Token('MUL')
            if self.current_char == '/':
                self.advance()
                return Token('DIV')
            if self.current_char == '^':
                self.advance()
                return Token('POW')
            if self.current_char == '(':
                self.advance()
                return Token('LPAREN')
            if self.current_char == ')':
                self.advance()
                return Token('RPAREN')
            
            raise Exception(f"Invalid character: {self.current_char}")
        
        return Token('EOF')
        