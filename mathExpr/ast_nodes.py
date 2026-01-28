class AST:
    pass

class Number(AST):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Number({self.value})"

class Variable(AST):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Var({self.name})"
        
class Constant(AST):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Const({self.value})"
    
class BinaryOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f"({self.left}  {self.op} {self.right})"
        
class UnaryOp(AST):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def __repr__(self):
        return f"UnaryOp({self.op} {self.expr})"
        
class FunctionCall(AST):
    def __init__(self, name, argument):
        self.name = name
        self.argument = argument

    def __repr__(self):
        return f"{self.name} ({self.argument})"