class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.variables = []

    def parse(self):
        i = 0
        #print(self.tokens)
        for token in self.tokens:

            #Variable Declaration
            if token[0] == "VAR_DECLARATION":

                #If variable declaration is correct
                if self.tokens[i+1][0] == "IDENTIFIER" and self.tokens[i+2][0] == "OPERATOR":
                    identifier = self.tokens[i+1][1]

                    #Adds a variable "string"
                    if self.tokens[i+3][0] == "STRING":

                        #If variable does not exist yet
                        if not self.checkVariable(identifier):
                            self.variables.append([identifier, self.tokens[i+3][1][1:-1]])

                        else:
                            newValue = self.tokens[i+3][1][1:-1]
                            self.changeVariable(identifier, newValue)

                    #If the variable gets another variable value
                    elif self.tokens[i+3][0] == "IDENTIFIER":
                        if self.checkVariable(identifier):
                            self.changeVariable(identifier, self.print_variable(self.tokens[i+3][1]))
                        else:
                            self.variables.append([identifier, self.print_variable(self.tokens[i+3][1])])

                    #If the variable is a integer
                    elif self.tokens[i+3][0] == "INTEGER":
                        if self.checkVariable(identifier):
                            self.changeVariable(identifier, self.tokens[i+3][1])
                        else:
                            self.variables.append([identifier, self.tokens[i+3][1]])
                else:
                    print("ERROR: Variable is not defined correctly")

            #Printing Function
            elif token[0] == "PRINT":
                if self.tokens[i+1][0] == "STRING":
                    print(self.tokens[i+1][1][1:-1])
                elif self.tokens[i+1][0] == "IDENTIFIER":
                    if self.checkVariable(self.tokens[i+1][1]):
                        print(self.print_variable(self.tokens[i+1][1]))
                    else:
                        print("WARNING! Print error - Variable " + self.tokens[i+1][1] + " does not exist!")

            #Printing Variables Function
            elif token[0] == "PRINT_VARIABLES":
                print("=== Printing all the variables in a Dictionary ===")
                print(self.variables)
            i = i + 1



    def print_variable(self, identifier):
        a = 0
        for variable in self.variables:
            if identifier == variable[0]:
                return variable[1]
                break
            a = a + 1

    def changeVariable(self, identifier, newValue):
        flag = 0
        for variable in self.variables:
            if identifier == variable[0]:
                variable[1] = newValue
                flag = 1
                break
        if flag == 0:
            print("Variable " + identifier + " does not exist!")

    def checkVariable(self, identifier):
        for variable in self.variables:
            if identifier == variable[0]:
                return 1
                break
        return 0
