import math
from ast_nodes import *

class ConstantFolder:
    def fold(self, node):
        
        if isinstance(node , (Number, Variable, Constant)):
            return node
        
        if isinstance(node, UnaryOp):
            expr = self.fold(node.expr)
            
            if isinstance(expr, Number):
                if node.op == 'MINUS':
                    return Number(-expr.value)
            return UnaryOp(node.op, expr)
        
        if isinstance(node, BinaryOp):
            left = self.fold(node.left)
            right = self.fold(node.right)
            
            if isinstance(left, Number) and isinstance(right, Number):
                if node.op == 'PLUS':
                    return Number(left.value + right.value)
                elif node.op == 'MINUS':
                    return Number(left.value - right.value)
                elif node.op == 'MUL':
                    return Number(left.value * right.value)
                elif node.op == 'DIV':
                    return Number(left.value / right.value)
                elif node.op == 'POW':
                    return Number(left.value ** right.value)
            return BinaryOp(left, node.op, right)
        
        if isinstance(node, FunctionCall):
            arg = self.fold(node.argument)
            
            if isinstance(arg, Number):
                if node.func_name == 'SIN':
                    return Number(math.sin(arg.value))
                elif node.func_name == 'COS':
                    return Number(math.cos(arg.value))
                elif node.func_name == 'SQRT':
                    return Number(math.sqrt(arg.value))
                
            return FunctionCall(node.name, arg)
        raise Exception(f"Unknown node type: {type(node)}")