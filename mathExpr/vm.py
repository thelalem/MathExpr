import math

class StackVM:
    def __init__(self):
        self.stack = []
    
    def run(self, instructions, variables = {}):
        self.stack = []
        
        for instr in instructions:
            parts = instr.split()
            op = parts[0]
            
            if op == "PUSH":
                value = float(parts[1])
                self.stack.append(value)
            
            elif op == "LOAD":
                var_name = parts[1]
                if var_name in variables:
                    self.stack.append(variables[var_name])
                else:
                    raise Exception(f"Undefined variable: {var_name}")
                
            elif op == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
                
            elif op == "SUB":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
            
            elif op == "MUL":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
                
            elif op == "DIV":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a / b)
                
            elif op == "POW":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a ** b)
            
            elif op == "NEG":
                a = self.stack.pop()
                self.stack.append(-a)
                
            elif op == "SIN":
                a = self.stack.pop()
                self.stack.append(math.sin(a))
            
            elif op == "COS":
                a = self.stack.pop()
                self.stack.append(math.cos(a))
            
            elif op == "SQRT":
                a = self.stack.pop()
                self.stack.append(math.sqrt(a))
            
            else:
                raise Exception(f"Unknown instruction: {instr}")
            
        if len(self.stack) != 1:
            raise Exception("Stack did not end with a single value")
        
        return self.stack[0]