from optparse import OptionParser
from lexer import Lexer
from parser_hda import Parser
from visitor_hda import Visitor

class Compilateur:
    def __init__(self):
        input_file = self.option_parser()
        self.content = self.read_content(input_file)
    
    def option_parser(self):
        parser = OptionParser()
    
        parser.add_option("-i", 
                        "--input", 
                        action="store", 
                        type="string",
                        dest="input_file", 
                        metavar="INPUT_PATH")
        
        
        options, args = parser.parse_args()
    
        if (not options.input_file):
            parser.print_help()
            exit()
        
        return options.input_file
    
    def read_content(self, input_file):
        fd = open(input_file)
        return fd.readlines()
        
    def build(self):
        lexer = Lexer()
        lexems = lexer.lex(self.content)
        
        parser = Parser(lexems)
        ast = parser.parse() 
        
        visitor = Visitor.Visitor()
        visitor.visit(ast)
        

c = Compilateur()
c.build()
        
        