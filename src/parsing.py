class Parser(object):


    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        variables = []
        print("Parsing data...")
        i = 0
        print(self.tokens)
        for token in self.tokens:

            #Variable Declaration
            if token[0] == "VAR_DECLARATION":
                if self.tokens[i+1][0] == "IDENTIFIER" and self.tokens[i+2][0] == "OPERATOR":
                    identifier = self.tokens[i+1][1]
                    print("==== Variable Declaration ====")
                    print("Variable name " + self.tokens[i+1][1] + "\n")
                    variables.append([identifier, self.tokens[i+3][1]])

                else:
                    print("ERROR: Variable is not defined correctly")
            elif token[0] == "PRINT":
                print("==== Print ====")
            i = i + 1

        print("\n\n=== VARIABLES ===")
        print(variables)
