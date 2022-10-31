from typing import List

def BFS(start, end, neighbours):

    searchTree = {}     # child --> parent, for retracing
    queue = [start]

    while len(queue) > 0:

        node = queue.pop(-1)

        if node == end:
            break

        neighberhood = neighbours(node)
        for n in neighberhood:
            if str(n) not in searchTree:

                searchTree[str(n)] = node   # str is hushable
                queue.insert(0, n)
    
    else:
        return None     # not found

    rout = [end]
    while rout[0] != start:
        rout.insert(0, searchTree[str(rout[0])])
    
    return rout


if __name__ == '__main__':
    
    
    def four_neighbours(node) -> List:

        x, y = node
        return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]

    print(BFS((0, 0), (-10, 10), four_neighbours))