from ast_nodes import *

class CodeGenerator:
    def __init__(self):
        self.instructions = []
        
    def generate(self, node):
        if isinstance(node, Number):
            self.instructions.append(f"PUSH {node.value}")
            
        elif isinstance(node, Variable):
            self.instructions.append(f"LOAD {node.name}")
            
        elif isinstance(node, Constant):
            self.instructions.append(f"PUSH {node.value}")
        
        elif isinstance(node, UnaryOp):
            self.generate(node.expr)
            if node.op == 'MINUS':
                self.instructions.append("NEG")
        
        elif isinstance(node, BinaryOp):
            self.generate(node.left)
            self.generate(node.right)
            if node.op == 'PLUS':
                self.instructions.append("ADD")
            elif node.op == 'MINUS':
                self.instructions.append("SUB")
            elif node.op == 'MUL':
                self.instructions.append("MUL")
            elif node.op == 'DIV':
                self.instructions.append("DIV")
            elif node.op == 'POW':
                self.instructions.append("POW")
        
        elif isinstance(node, FunctionCall):
            self.generate(node.argument)
            if node.name == 'SIN':
                self.instructions.append("SIN")
            elif node.name == 'COS':
                self.instructions.append("COS")
            elif node.name == 'SQRT':
                self.instructions.append("SQRT")
        
        else:
            raise Exception(f"Unknown node type: {type(node)}")
        
        return self.instructions