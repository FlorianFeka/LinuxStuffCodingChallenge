# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

# For example, given the following Node class

# class Node: def init(self, val, left=None, right=None):
#     self.val = val self.left = left self.right = right 

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    depth = 0
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        if(left is not None):
            left.addDepth()
        if(right is not None):
            right.addDepth()
        self.left = left
        self.right = right
    
    def serialize(self, depth=None):
        string = str(self.val)+'-'
        if(self.left is not None):
            string += f'l/{self.depth}#'+self.left.serialize(self.depth)
        if(self.right is not None):
            string += f'r/{self.depth}#'+self.right.serialize(self.depth)
        if(depth is not None):
            dif = self.depth-depth
            for i in range(0,dif):
                string += '-'
        return string

    def addDepth(self):
        self.depth += 1

    def setVal(self, val):
        self.val = val
    
    def add(self, left=None, right=None):
        if(left is not None):
            self.left = left
        if(right is not None):
            self.right = right
    
    def setDepth(self, depth):
        self.depth = depth

def deserialize(string=None, base=None, nextPos=None, parentNode=None):
    base = string.split('-')
    rootNode = Node(base[0])
    deserializePart(base, 1, rootNode)
    return rootNode;


def deserializePart(base, nextPos, parentNode):
    if(len(base)<=nextPos):
        return
    if(base[nextPos] == ''):
        nextPos += 1
        deserializePart(base, nextPos, parentNode)
        return
    part = base[nextPos]
    nextPos += 1
    posVal = part.split('#')
    val = posVal[1]
    pos = posVal[0].split('/')[0]
    depth = int(posVal[0].split('/')[1])
    node = Node(val)
    node.setDepth(depth)
    deserializePart(base, nextPos, node)
    
    if(pos == 'l'):
        parentNode.add(left=node)
    if(pos == 'r'):
        parentNode.add(right=node)

        



node = Node('root', Node('left', Node('left.left'), Node('right.right')), Node('right'))

nodeStr = node.serialize()
print(nodeStr)
n = deserialize(nodeStr)
print(n.serialize())

