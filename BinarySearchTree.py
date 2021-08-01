import sys
from collections import namedtuple


class Node:
    def __init__(self, k, v, p=None):
        self.left = None
        self.right = None
        self.parent = p
        self.key = k
        self.value = v

    def __str__(self):
        result = f"[{self.key} {self.value}"
        if self.parent:
            result += f" {self.parent.key}"
        return result + "]"

    def insert_child(self, k, v):
        if self.key == k:
            return False
        if k < self.key:
            if self.left:
                return self.left.insert_child(k, v)
            else:
                self.left = Node(k, v, self)
        else:
            if self.right:
                return self.right.insert_child(k, v)
            else:
                self.right = Node(k, v, self)
        return True

    def min_child(self):
        result = self
        while result.left:
            result = result.left
        return result

    def max_child(self):
        result = self
        while result.right:
            result = result.right
        return result


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key, value):
        if self.root:
            return self.root.insert_child(key, value)
        self.root = Node(key, value)
        return True

    def delete(self, key):
        return self.delete_node(self.search(key))

    def delete_node(self, node):
        if node:
            node_parent = node.parent
            if node.left is None and node.right is None:
                if node_parent:
                    if node_parent.left is node:
                        node_parent.left = None
                    else:
                        node_parent.right = None
                else:
                    self.root = None
            elif node.left is None or node.right is None:
                if node.left:
                    child = node.left
                else:
                    child = node.right
                if node_parent:
                    if node_parent.left is node:
                        node_parent.left = child
                    else:
                        node_parent.right = child
                else:
                    self.root = child
                if child:
                    child.parent = node_parent
            else:
                successor = node.left.max_child()
                node.value = successor.value
                node.key = successor.key
                self.delete_node(successor)
            return True
        return False

    def search(self, key):
        result = self.root
        while result:
            if key < result.key:
                result = result.left
            elif key > result.key:
                result = result.right
            else:
                break
        return result

    def set(self, key, value):
        found = self.search(key)
        if found:
            found.value = value
        return found

    def min(self):
        result = self.root
        if result:
            return result.min_child()
        return result

    def max(self):
        result = self.root
        if result:
            return result.max_child()
        return result

    def print(self):
        if not self.root:
            print("_")
            return

        curr_level = [self.root]
        while curr_level:
            if any(curr_level):
                print(' '.join(str(node) if node else "_" for node in curr_level))
            else:
                break
            next_level = list()
            for n in curr_level:
                if n:
                    next_level.append(n.left)
                    next_level.append(n.right)
                else:
                    next_level.extend([None]*2)
            curr_level = next_level


Command = namedtuple("Command", "func argc ret")

commands = {
    "add":    Command(BinarySearchTree.add, 2, bool),
    "set":    Command(BinarySearchTree.set, 2, bool),
    "delete": Command(BinarySearchTree.delete, 1, bool),
    "search": Command(BinarySearchTree.search, 1, Node),
    "min":    Command(BinarySearchTree.min, 0, Node),
    "max":    Command(BinarySearchTree.max, 0, Node),
    "print":  Command(BinarySearchTree.print, 0, None)
}

if __name__ == '__main__':
    bst = BinarySearchTree()
    for line in sys.stdin:
        cmd_args = line.split()
        if not cmd_args:
            continue
        command = commands.get(cmd_args[0], None)
        if command and command.argc == len(cmd_args[1:]):
            ret = None
            if command.argc > 0:
                if cmd_args[1].lstrip("+-").isdigit():
                    ret = command.func(bst, int(cmd_args[1]), *cmd_args[2:])
                    if command.ret is bool:
                        if not ret:
                            print("error")
                    else:
                        if ret:
                            print(f"1 {ret.value}")
                        else:
                            print(0)
                else:
                    print("error")
            else:
                ret = command.func(bst)
                if command.ret is Node:
                    if ret:
                        print(f"{ret.key} {ret.value}")
                    else:
                        print("error")
        else:
            print("error")

