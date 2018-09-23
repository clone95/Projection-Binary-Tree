from anytree import Node, RenderTree


def increment(to_incr, n):     #increments of n
    val = to_incr + (to_incr*n)
    return val


def decrement(to_decr, n):     #increments of n
    val = to_decr - (to_decr*n)
    return val


def generate_level(node, n):
        nod1 = Node("salita", node)
        nod2 = Node("discesa", node)
        if n != 0:
            generate_level(nod1, n-1)
            generate_level(nod2, n-1)


leaves = 2
branches = 3
root = Node(100)

generate_level(root, 3)

print(RenderTree(root))


