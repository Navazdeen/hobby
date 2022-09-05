from collections import deque
from re import search
from gme.box import Box


class BreadhFirstSearch():
    def __init__(self, box) -> None:
        self.path = dict()
        self.queue = deque()
        self.box = box

    def search(self, src, dest):
        self.queue.clear()
        self.path.clear()
        self.queue.append(src)
        while self.queue:
            # print(self.queue)
            v = self.queue.popleft()
            v.select()
            if v == dest:
                # print("found", self.path)
                return 1
            for block_id in self.box.adjacent_block(v):
                block = self.box.block_list[block_id]
                if not self.box.block_list[block_id].visited and block.valid:
                    block.visit()
                    self.path[self.box.get_id(
                        block=block)] = self.box.get_id(block=v)
                    self.queue.append(block)
                    self.box.update_block()
        else:
            return 0

    def find_path(self, source, dest):
        if not self.search(source, dest):
            return
        source_id = self.box.get_id(block=source)
        dest_id = self.box.get_id(block=dest)
        current_id = dest_id
        # print(current_id, dest_id, source_id, self.path[3])
        while source_id != current_id:
            current_id = self.path[current_id]
            self.box.block_list[current_id].make_path()
            # print(f"{current_id} -> ", end="")
        source.set_color("Orange")
        dest.set_color("Blue")


if __name__ == "__main__":
    bx = Box(500, 500, 20, 20)
    bx.create_block()
    lst = bx.block_list
    # print(lst)
    bfs = BreadhFirstSearch(bx, lst[70])
    bfs.find_path(lst[150])
    # print(bx.block_list)
