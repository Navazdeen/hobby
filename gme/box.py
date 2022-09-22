from gme.block import Block


class Box:
    def __init__(self, width, height, rows, cols, dispsurf, gameobj) -> None:
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.block_count = self.rows * self.cols
        self.block_list = list()
        self.width_space = self.width // self.rows
        self.height_space = self.height // self.cols
        self.line_thick = 1
        self.dispsurf = dispsurf
        self.gameobj = gameobj
        self.src = None
        self.dest = None

    def create_block(self) -> None:
        for x in range(self.rows * self.cols):
            row = x // self.rows
            col = x % self.cols
            self.block_list.append(
                Block(self.width_space * row, self.height_space * col, x)
            )

    def update_block(self, dispsurf=None, pygame=None) -> None:
        if dispsurf == None and pygame == None:
            dispsurf = self.dispsurf
            pygame = self.gameobj
        for block in self.block_list:
            # print(block.color)
            pygame.draw.rect(
                dispsurf,
                block.color,
                (
                    block.x,
                    block.y,
                    self.width_space - self.line_thick,
                    self.height_space - self.line_thick,
                ),
            )
        pygame.display.update()

    def get_row_col(self, x=None, y=None, block=None):
        if not x and not y and block:
            x = block.x
            y = block.y
        row = x // self.width_space
        col = y // self.height_space
        return (row, col)

    def get_id(self, x=None, y=None, row=None, col=None, block=None):
        if not x and not y and block:
            x = block.x
            y = block.y
        row, col = self.get_row_col(x=x, y=y)
        return int(row * self.rows + col)

    def select_block(self, x, y):
        # row, col = self.get_row_col(x, y)
        id = self.get_id(x=x, y=y)
        # print((row, col), id)
        if 0 <= id < (self.rows * self.cols):
            self.block_list[id].select()
            self.block_list[id].set_color("Aqua")

    def set_source(self, block):
        if self.src:
            self.src.set_color("White")

        self.src = block
        self.src.set_color("Orange")

    def set_dest(self, block):
        if self.dest:
            self.dest.set_color("White")

        self.dest = block
        self.dest.set_color("Blue")

    def adjacent_block(self, block):
        x = block.x
        y = block.y
        row = x // self.width_space
        col = y // self.height_space
        adjacent_blocks = list()
        # print("row",row,"col", col)
        for rc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            if (0 <= row + rc[0] < self.rows) and (0 <= col + rc[1] < self.cols):
                id = int((row + rc[0]) * self.rows + (col + rc[1]))
                # blk = self.block_list[id]
                adjacent_blocks.append(id)
                # print(row-rc[0], col-rc[1])
                # print(row, rc[0], col, rc[1])
        return adjacent_blocks


if __name__ == "__main__":
    pass
