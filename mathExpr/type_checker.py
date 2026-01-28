from ast_nodes import *

class TypeChecker:
    def check(self, node):
        if isinstance(node, Number):
            return "NUMBER"
        
        if isinstance(node, Variable):
            return "NUMBER"
        
        if isinstance(node, Constant):
            return "NUMBER"
        
        if isinstance(node, UnaryOp):
            expr_type = self.check(node.expr)
            if expr_type != "NUMBER":
                raise Exception(f"Unary operation '{node.op}' requires a numeric operand.")
            return "NUMBER"

        if isinstance(node, BinaryOp):
            left_type = self.check(node.left)
            right_type = self.check(node.right)
            if left_type != "NUMBER" or right_type != "NUMBER":
                raise Exception(f"Binary operation '{node.op}' requires numeric operands.")
            return "NUMBER"
        
        if isinstance(node, FunctionCall):
            arg_type = self.check(node.argument)
            if arg_type != "NUMBER":
                raise Exception(f"Function '{node.func_name}' requires a numeric argument.")
            return "NUMBER"
        
        raise Exception(f"Unknown AST node type: {type(node)}")