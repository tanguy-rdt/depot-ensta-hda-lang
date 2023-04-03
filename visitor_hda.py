class Visitor:        
    def visit(self, ast):
        ast.accept(self)
            
    def visit_house(self, house):
        house.floor.accept(self)
            
    def visit_floor(self, etage):
        #etage.room.accept(self)
        pass
        
    def visit_room(self, room):
        pass
    
    def visit_kitchen(self, kitchen):
        pass
        