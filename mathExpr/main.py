from lexer import Lexer
from parse import Parser
from type_checker import TypeChecker
from optimizer import ConstantFolder
from codegen import CodeGenerator
from vm import StackVM

#INpurt Expression
text = "sin(a + 2) * 3"
lexer = Lexer(text)
parser = Parser(lexer)

ast = parser.expr()
print("AST:", ast)

# Type Checking

checker = TypeChecker()
checker.check(ast)

# Optimization
optimizer = ConstantFolder()
optimized_ast = optimizer.fold(ast)
print("Optimized AST:", optimized_ast)

# Code Generation
codegen = CodeGenerator()
instructions = codegen.generate(optimized_ast)
print("Generated Instructions:", instructions)

for instr in instructions:
    print(instr)
    
# Virtual Machine Execution
variables = {'a': 1}
vm = StackVM()
result = vm.run(instructions, variables)
print("Result:", result)