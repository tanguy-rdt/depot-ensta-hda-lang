import io
from optparse import OptionParser

from compiler.lexer import Lexer
from compiler.parser_hda import Parser
from compiler.house_designer import HouseDesigner
from compiler.house_designer import HouseDesigner3D


class Builder:
    def read_content(self, input_file):
        fd = open(input_file)
        return fd.readlines()
        
    def build(self, input_file):
        content = self.read_content(input_file)
        
        lexer = Lexer()
        lexems = lexer.lex(content)

        print(lexems)
        
        parser = Parser(lexems)
        ast = parser.parse() 
        
        hd = HouseDesigner()
        hd.design(ast)

        hd3d = HouseDesigner3D()
        hd3d.design(ast)
        
class Interactive:
    def run(self):        
        wish = input(">>> ")
        content = []
        content.append(wish)
        content.append(';')
        while wish != "exit\n":        
            lexer = Lexer()
            lexems = lexer.lex(content)
            
            parser = Parser(lexems)
            ast = parser.parse() 
            
            hd = HouseDesigner(mode='i')
            hd.design(ast)
            
            wish = input(">>> ")
            wish = wish + '\n'
            content.insert(-1, wish)
        exit()

def option_parser():
    parser = OptionParser()

    parser.add_option("-b", 
                    "--build", 
                    action="store", 
                    type="string",
                    dest="input_file", 
                    metavar="INPUT_PATH")
    
    parser.add_option("-o", 
            "--output", 
            action="store", 
            type="string",
            dest="output_file", 
            metavar="OUTPUT_PATH")
    
    parser.add_option("-i", 
            "--interactive", 
            action="store_true", 
            dest="interactive_mode")
    
    
    options, args = parser.parse_args()

    if not options.input_file and not options.output_file and not options.interactive_mode:
        parser.print_help()
        exit()
    
    return options.input_file, options.output_file, options.interactive_mode
    

def main():
    input_file, output_file, interactive_mode = option_parser()
    
    if interactive_mode:
        console = Interactive()
        console.run()
    else :
        builder = Builder()
        builder.build(input_file)

if __name__ == "__main__":
    main()