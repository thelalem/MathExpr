from ast_nodes import *
from lexer import Token

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Unexpected token: {self.current_token}, expected: {token_type}")
        
    # expr -> addExpr
    def expr(self):
        return self.addExpr()
    
    # addExpr -> mulExpr (( '+' | '-' ) mulExpr)*
    def addExpr(self):
        node = self.mul_expr()
        
        while self.current_token.type in ('PLUS', 'MINUS'):
            op = self.current_token.type
            self.eat(op)
            right = self.mul_expr()
            node = BinaryOp(node, op, right)
            
        return node
    
    # mulExpr -> powExpr (( '*' | '/' ) powExpr)*
    def mul_expr(self):
        node = self.pow_expr()
        
        while self.current_token.type in ('MUL', 'DIV'):
            op = self.current_token.type
            self.eat(op)
            right = self.pow_expr()
            node = BinaryOp(node, op, right)
            
        return node
    
    # powExpr -> unaryExpr ( '^' powExpr )*
    def pow_expr(self):
        node = self.unary_expr()
        
        if self.current_token.type == 'POW':
            op = self.current_token.type
            self.eat("POW")
            right = self.pow_expr()
            node = BinaryOp(node, op, right)
            
        return node
    
    # unaryExpr -> ( '+' | '-' ) unaryExpr | primaryExpr
    def unary_expr(self):
        if self.current_token.type == 'PLUS':
           self.eat('PLUS')
           return self.unary_expr()
       
        if self.current_token.type == 'MINUS':
           self.eat('MINUS')
           return UnaryOp('MINUS', self.unary_expr())
       
        return self.primary()
    
    # primary → NUMBER | VARIABLE | CONSTANT | FUNCTION '(' expr ')' | '(' expr ')'
    def primary(self):
        token = self.current_token
        
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token.value)
        
        if token.type == 'VAR':
            self.eat('VAR')
            return Variable(token.value)
        
        if token.type in ('CONST_PI', "CONST_E"):
            self.eat(token.type)
            return Constant(token.value)
        
        if token.type in ("SIN", "COS", "SQRT"):
            func_name = token.type
            self.eat(token.type)
            self.eat('LPAREN')
            arg = self.expr()
            self.eat('RPAREN')
            return FunctionCall(func_name, arg)
        
        if token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        
        raise Exception(f"Unexpected token: {token}")