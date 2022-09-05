class Block():
    def __init__(self, x, y, id) -> None:
        self.x = x
        self.y = y
        self.color = "White"
        self.visited = False
        self.valid = True
        self.selected = False
    
    def visit(self) -> None:
        self.visited = True
        self.color = "Green"

    def select(self) -> None:
        # self.color = "Aqua"
        self.valid = False
    
    def unselect(self) -> None:
        self.color = "White"

    def make_path(self):
        self.color = "Red"

    def set_color(self, color):
        self.color = color
    
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y 

    def __repr__(self) -> str:
        return f"point: ({self.x}, {self.y})"