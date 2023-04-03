class Visitor:        
    def visit(self, ast):
        ast.accept(self)
            
    def visit_house(self, house):
        house.etage.accept(self)
            
    def visit_etage(self, etage):
        etage.room.accept(self)
        
    def visit_room(self, room):
        pass
        