from anytree import Node, RenderTree


def increment(to_incr, n):     #increments of n
    return to_incr*n


def decrement(to_decr, n):     #increments of n
    return to_decr*n


def generate_level(node, n, m):
        m = m + 1
        nod1 = Node(root.name, node)
        nod2 = Node(root.name, node)
        #nod1 = Node(root.name + increment(root.name, 0.1)*m, node)
        #nod2 = Node(root.name - increment(root.name, 0.1)*m, node)
        nod1.name = nod1.parent.name + 1
        nod2.name = nod2.parent.name - 1
        if n != 0:
            generate_level(nod1, n-1, m)
            generate_level(nod2, n-1, m)


leaves = 2
branches = 3
root = Node(100)

generate_level(root, 3, 0)

print(RenderTree(root))


