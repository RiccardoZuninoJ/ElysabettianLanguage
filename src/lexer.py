import re

class Lexer(object):

    def __init__(self, source_code):
         self.source_code = source_code

    def tokenize(self):
        #All the tokens
        tokens = []

        #Creates a word list
        source_code = self.source_code.split()

        #Word index
        indexsource = 0

        #Loop of all the words
        while indexsource < len(source_code):

            word = source_code[indexsource]

            #Deletes ; if exists. If not it works the same
            if word[-1] == ";":
                word = word[:-1]


            #If there is a Variable declaration
            if word == "var":
                tokens.append(["VAR_DECLARATION", word])

            #If a word
            elif (re.match('[a-z]', word) or re.match('[A-Z]', word)) and word != "print":
                tokens.append(["IDENTIFIER", word])

            #If a integer
            elif re.match('[0-9]', word):
                tokens.append(["INTEGER", word])

            elif word in "=/*-+":
                tokens.append(["OPERATOR", word])

            elif word == "print":
                tokens.append(["PRINT", word])

            elif word == ";":
                tokens.append(["LINE_ENDING", word])
            elif word[0] == "\"" and word[-1] == "\"":
                tokens.append(["STRING", word])
            indexsource = indexsource + 1



        #Returns all the tokens
        return tokens
