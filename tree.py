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
        nod1.__setattr__(("prob"), (nod1.parent.__getattribute__("prob") * prob_inc))       # probability of reaching that specific leaf
        nod2.__setattr__(("prob"), (nod2.parent.__getattribute__("prob") * prob_dec))
        if n != 0:
            generate_tree(nod1, n - 1, inc, dec, prob_inc, prob_dec)            # recursive branches generation
            generate_tree(nod2, n - 1, inc, dec, prob_inc, prob_dec)


root = Node(100, prob=1)            # test root


def main():

    print("\n\nBinary tree - Insert parameters for the projection: \n\n")

    valore_iniziale = input("Inserisci il valore iniziale:\n\n")
    incremento = input("\nInsert %% of increase, \nper period [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    decremento = input("\nInserisci percentuale di DEcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    dec_prob = input("\nInserisci probabilità di DEcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    incr_prob = input("\nInserisci probabilità di DEcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    periodi = input("\nInserisci quanti periodi vuoi esaminare: \nattenzione alla crescita esponenziale dei calcoli [2^n, n = numero di periodi]\n\n")

    root = Node(valore_iniziale, prob = 1)

    generate_tree(root, int(periodi), float(incremento), float(decremento), float(incr_prob), float(dec_prob)) # generate the tree

    results = []
    values = []
    probs = []
    print(RenderTree(root))
    for child in root.descendants:
        if child.is_leaf:
            res = Result(round(child.name), round(child.prob, 2))
            results.append(res)

    for el in results:
        values.append(round(el.value))
    for el in results:
        probs.append(round(el.prob, 3))

    occ_dic = dict()
    prob_dic = dict((a, b) for a, b in zip(values, probs))
    for val in values:
        if val in occ_dic:
            occ_dic.__setitem__(val, occ_dic.__getitem__(val) + 1)
        else:
            occ_dic.__setitem__(val, 1)
    print("\nconsidering the combine cases, the projections are \n")
    for res in occ_dic:
        calc = ((occ_dic[res] * prob_dic[res]) * 100)
        print("price   %g  --- > p(event)  ==  %g %%" % (res, round((occ_dic[res] * prob_dic[res]) * 100)))

main()

