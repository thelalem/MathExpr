# MathExpr Compiler

## Description
A small compiler for a mathematical expression language (MathExpr) 
that supports arithmetic operations, constants, variables, and functions (sin, cos, sqrt). 
It performs lexical analysis, parsing, type checking, optimization (constant folding), 
and generates stack-based VM instructions executable in a custom virtual machine.

---
## Group Members

- **Zelalem Argaw**
- **Khalid Abduljelil**
- **Naod Wubshet**
- **Edomiyas Wondwossen**
- **Natnael Amde**

---

## Features
- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `^`  
- **Constants:** `π`, `e`  
- **Variables:** single-letter `a-z`  
- **Functions:** `sin()`, `cos()`, `sqrt()`  
- **Parentheses** for controlling precedence  
- **Compiler Phases Implemented:**
  - Lexer / Tokenizer
  - Recursive Descent Parser (AST generation)
  - Type Checker
  - Constant Folding Optimizer
  - Stack-based Code Generator
  - Custom Stack VM to execute expressions

---

## Requirements
- Python 3.x

---

## Project Structure
```text
mathExpr/
├── lexer.py        # Tokenizes input expressions
├── parser.py       # Parses tokens and builds AST
├── ast_nodes.py    # AST node classes with pretty-printing
├── type_checker.py # Semantic analysis (type checking)
├── optimizer.py    # Constant folding optimizer
├── codegen.py      # Stack-based VM code generator
├── vm.py           # Stack-based virtual machine
├── main.py         # Example program to run expressions
└── README.md       # Project documentation

---

## Setup & Run
1. Clone the repository:
```bash
git clone <https://github.com/thelalem/MathExpr>
cd mathExpr
2. Run main.py
python main.py
3. Edit main.py to change the expressions or variable values

    Example:
    text = "sin(a + 2) * 3"
    variables = {"a": 1}

    AST: ((SIN((Var(a) PLUS Number(2.0))) MUL Number(3.0))
    Optimized AST: ((SIN((Var(a) PLUS Number(2.0))) MUL Number(3.0))
    Generated VM code:
    LOAD a
    PUSH 2.0
    ADD
    SIN
    PUSH 3.0
    MUL
    Result: 0.4233600241796016
```

# Notes
- Fully demonstrates compiler phases from lexing → parsing → AST → type checking → optimization → code generation → execution.
- Custom stack-based VM executes arithmetic expressions with variables and math functions.
- Designed for educational purposes and Compiler Design coursework.

# Course Information
Course: Compiler Design
Year: 3rd Year
Date: 2026-01-28
