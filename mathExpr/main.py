from lexer import Lexer

text = "sin(a + 2.5) * 3"
lexer = Lexer(text)

token = lexer.get_next_token()
while token.type != 'EOF':
    print(token)
    token = lexer.get_next_token()

print(token)  # Print the EOF token