from gme.box import Box
from time import sleep
import sys

sys.setrecursionlimit(5000)

class DepthFirstSearch():
    def __init__(self, box) -> None:
        self.path = dict()
        self.stack = list()
        self.box = box
        self.block_list = self.box.block_list

    def search(self, src, dest):
        sleep(0.01)
        v = src
        v.visit()
        if src == dest:
            return src
        for id in self.box.adjacent_block(v):
            block = self.block_list[id]
            if not block.visited and block.valid:
                blk = self.search(block, dest)
                if blk:
                    # print(self.box.get_id(block=blk))
                    self.path[self.box.get_id(
                        block=blk)] = self.box.get_id(block=v)
                    self.stack.append(blk)
                    return src
        else:
            return 0

    def find_path(self, src, dest):
        sch = self.search(src, dest)
        if not self.stack and not sch:
            return -1
        src_id = self.box.get_id(block=src)
        current_id = self.box.get_id(block=dest)
        # print(self.path)
        while src_id != current_id:
            current_id = self.path[current_id]
            self.box.block_list[current_id].make_path()


if __name__ == "__main__":
    bx = Box(500, 500, 25, 25)
    bx.create_block()
    lst = bx.block_list
    print(lst)
    dfs = DepthFirstSearch(bx)
    dfs.find_path(lst[2], lst[75])
    print(dfs.path)
    print(bx.block_list)
