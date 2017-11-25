import random
import numpy as np
np.random.seed(4)

h = 10
w = 10

def create_map(h=10,w=10,ratio = 0.5):
    m = np.zeros([h,w])
    num_of_one = int(round(h*w*ratio))
    list_x = np.random.randint(0,w,size =num_of_one)
    list_y = np.random.randint(0,h,size =num_of_one)
    for x,y in zip(list_x,list_y):
        m[x,y] = 1
    return m


m = create_map(h=h,w=w)
# used_idx = np.ones(m.shape)
# all_groups = []
# group_idx = []
# x = 0
# y = 0
# def find_group(y,x,group_idx,used_idx,all_group,m):
#     if np.sum(used_idx[:]) == 0:
#         return all_groups
#     for x,y in zip(np.where(used_idx==1)[1],np.where(used_idx==1)[0]):
#         if m[y,x] == 1:
#             group_idx.append([y,x])
#             used_idx[y,x] = 0
#             #send to R
#             # if x == m.shape[1]-1 and y == m.shape[0]-1:
#             #     #finish
#             # elif x == m.shape[1]-1 or used_idx[y,x+1] == 0:
#             #     #cant send
#             # else:
#             #     find_group(y,x+1,group_idx,used_idx,m)
#
#         else:
#             if len(group_idx)!=0:
#                 all_groups.append(group_idx)
#                 return used_idx
#             # start from the next open spot
#
# find_group(x,y,group_idx,used_idx,all_groups,m)
# class Position:
#     def __init__(self,r,c):
#         self.pos =
class NODE:
    def __init__(self,r,c,val):
        self.pos = (r,c)
        self.val = val

    def neighbors(self,matrix):
        y,x = self.pos
        group = []
        #go left
        if x-1 >= 0:
            v = matrix[y][x-1].val
            group.append(NODE(y,x-1,v))

        #go right
        if x+1 <= len(matrix[y])-1:
            v = matrix[y][x+1].val
            group.append(NODE(y,x+1,v))
        #go up
        if y-1 >= 0:
            v = matrix[y-1][x].val
            group.append(NODE(y-1,x,v))

        #go right
        if y+1 <= len(matrix[x])-1:
            v = matrix[y+1][x].val
            group.append(NODE(y+1,x,v))

        return group

    def find_good_neighbors(self,matrix):
        return [node for node in self.neighbors(matrix) if node.val == self.val]
    # def __str__(self):
    #     return `self.val, (self.pos)`[1:-1]

    def __hash__(self):
        return hash((self.pos, self.val))

    @staticmethod
    def mat2node(matrix):
        for y,row in enumerate(matrix):
            for x,item in enumerate(row):
                matrix[y][x] =NODE(y,x,item)
        return matrix

    @staticmethod
    def node2mat(matrix):
        for y,row in enumerate(matrix):
            for x,node in enumerate(row):
                matrix[y][x] =node.val
        return matrix

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.val == other.val and self.pos == other.pos
        return False

# checked = set()

def connected_values(node,matrix,checked=None):
    checked =checked or set()

    checked.add(node)
    nodes = []
    for neighbor in node.find_good_neighbors(matrix):
        nodes.append(neighbor)
        if neighbor not in checked:
            nodes+=connected_values(neighbor,matrix,checked)
    return nodes

def all_connected(matrix):
    global checked

    groups =[]
    for row in matrix:
        for node in row:
            # checked =set()
            values = set(connected_values(node,matrix))
            values.add(node)
            groups.append(values)
    print '\n'.join({str(group[0].val) + ": " + ', '.join(map(str, sorted([(node.pos) for node in group]))) for group in map(list,groups)})
    print
    # Prints out the original matrix
    print '\n'.join(map(str, NODE.node2mat(matrix)))
example_matrix = [
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [1, 0, 1, 0]
                 ]
NODE.mat2node(example_matrix)
all_connected(example_matrix)