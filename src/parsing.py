class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.variables = []

    def parse(self):
        print("Parsing data...")
        i = 0
        #print(self.tokens)
        for token in self.tokens:

            #Variable Declaration
            if token[0] == "VAR_DECLARATION":
                if self.tokens[i+1][0] == "IDENTIFIER" and self.tokens[i+2][0] == "OPERATOR":
                    identifier = self.tokens[i+1][1]
                    if self.tokens[i+3][0] == "STRING":
                        self.variables.append([identifier, self.tokens[i+3][1][1:-1]])
                    self.variables.append([identifier, self.tokens[i+3][1]])
                else:
                    print("ERROR: Variable is not defined correctly")

            elif token[0] == "PRINT":
                if self.tokens[i+1][0] == "STRING":
                    print(self.tokens[i+1][1][1:-1])
                elif self.tokens[i+1][0] == "IDENTIFIER":
                    print(self.print_variable(self.tokens[i+1][1]))
            i = i + 1

    def print_variable(self, identifier):
        a = 0
        for variable in self.variables:
            if identifier == variable[0]:
                return variable[1]
                break
            a = a + 1
