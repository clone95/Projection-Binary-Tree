from anytree import Node, RenderTree


class Result:                                   # class for hosting value and probability of happening
    def __init__(self, value, prob):
        self.value = value
        self.prob = prob


def variation(to_incr, n):     # variation EACH period
    return to_incr*n


def generate_tree(node, n, inc, dec, prob_inc, prob_dec):
        nod1 = Node(root.name, node, prob=1)        # generate leaves
        nod2 = Node(root.name, node, prob=1)
        nod1.name = nod1.parent.name + variation(nod1.parent.name, inc)         # variation on the price
        nod2.name = nod2.parent.name - variation(nod1.parent.name, dec)
        nod1.__setattr__("prob", (nod1.parent.__getattribute__("prob") * prob_inc))    # chance of reaching the leaf
        nod2.__setattr__("prob", (nod2.parent.__getattribute__("prob") * prob_dec))
        if n != 0:
            generate_tree(nod1, n - 1, inc, dec, prob_inc, prob_dec)            # recursive branches generation
            generate_tree(nod2, n - 1, inc, dec, prob_inc, prob_dec)


root = Node(100, prob=1)            # test root


def main():

    print("\n\nBinary tree - Insert parameters for the projection: \n\n")
    init_value = input("Insert initial value of the item:\n\n")
    incr = input("\nInsert % of increase, \nper age [decimal format:  se 10% --> insert 0.1]\n\n")
    decr = input("\nInsert % of decrease, \nper age [decimal format:  se 10% --> insert 0.1]\n\n")
    dec_prob = input("\nInsert down probability, \nper period[decimal format:  se 10% --> Insert 0.1]\n\n")
    incr_prob = input("\nInsert down probability, \nper period[decimal format:  se 10% --> Insert 0.1]\n\n")
    ages = input("\nInsert how many period you want to be examined: \ntake care about the "
                 "exponential growth of the computations [2^n, n = n. of periods]\n\n")

    actual_root = Node(int(init_value), prob=1)

    generate_tree(actual_root, int(ages), float(incr), float(decr), float(incr_prob), float(dec_prob))  # generate the tree

    results = []
    values = []
    probs = []

    print(RenderTree(root))
    for child in root.descendants:                   # select just the last leaves
        if child.is_leaf:
            res = Result(round(child.name), round(child.prob, 2))
            results.append(res)

    for el in results:                              # supports vector
        values.append(round(el.value))
    for el in results:
        probs.append(round(el.prob, 3))

    occ_dic = dict()
    prob_dic = dict((a, b) for a, b in zip(values, probs))            # one way to fill dictionary (more elegant)

    for val in values:                                                # another one, with more logic control
        if val in occ_dic:
            occ_dic.__setitem__(val, occ_dic.__getitem__(val) + 1)
        else:
            occ_dic.__setitem__(val, 1)

    print("\nconsidering the combine cases, the projections are \n")
    for res in occ_dic:                                                     # prints out the table with results
        print("price   %g  --- > p(event)  ==  %g %%" % (res, round((occ_dic[res] * prob_dic[res]) * 100)))


main()

