import logging
import compiler.ast_hda as ast

logger = logging.getLogger(__name__)


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================
    def accept(self):
        """
        Pops the lexem out of the lexems list.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            house = self.parse_house()
            return house
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_house(self):
        """
        Parses a program which is a succession of assignments.
        """        
        floor = []
        while self.show_next().tag != "END":
            floor.append(self.parse_floor())
        self.accept()
                    
        return ast.House(floor)

    def parse_floor(self):
        self.accept()
        
        lenght = self.expect("DIM")
        width = self.expect("DIM")
        
        room = []
        while self.show_next().tag == "ROOM":
            room.append(self.parse_room())
        
        return ast.Floor(lenght, width, room)

    def parse_room(self):
        name = self.accept()
        lenght = self.expect("DIM")
        width = self.expect("DIM")
        
        position = None
        pos = ["RIGHT", "LEFT", "TOP", "BOTTOM"]
        if self.show_next().tag in pos:
            position = [self.accept(), self.expect("ROOM")]
        
        return ast.Room(lenght, width, name, position)
    
