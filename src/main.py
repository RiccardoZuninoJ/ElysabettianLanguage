import lexer
import parsing
import argparse

def main():

    inputParser = argparse.ArgumentParser()
    inputParser.add_argument("-s", "--Source", help = "Source code")
    args = inputParser.parse_args()

    #Reads source code from test.lang
    code = ""

    if(args.Source):

        with open(args.Source, 'r') as file:
            code = file.read()
        if code:

            # Lexer
            # Initialize Lexer class
            lex = lexer.Lexer(code)
            tokens = lex.tokenize()
            parser = parsing.Parser(tokens)
            parser.parse()
        else:
            print("Error while opening source code.")
    else:
        print("!!! You must specify a source code !!!")

main()
