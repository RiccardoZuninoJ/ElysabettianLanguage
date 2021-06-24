import lexer

def main():

    #Reads source code from test.lang
    code = ""
    with open('test.lang', 'r') as file:
        code = file.read()

    # Lexer
    # Initialize Lexer class
    lex = lexer.Lexer(code)
    lex.tokenize()

main()
