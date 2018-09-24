from anytree import Node, RenderTree


def variation(to_incr, n):     # increment
    return to_incr*n


def probabilities ():
    return True


def generate_level(node, n, inc, dec, prob_inc, prob_dec):
        nod1 = Node(root.name, node, prob=1)
        nod2 = Node(root.name, node, prob=1)
        nod1.name = nod1.parent.name + variation(nod1.parent.name, inc)
        nod2.name = nod2.parent.name - variation(nod1.parent.name, dec)
        nod1.__setattr__(("prob"), (nod1.parent.__getattribute__("prob")*prob_inc))
        nod2.__setattr__(("prob"), (nod2.parent.__getattribute__("prob")*prob_dec))

        #nod1.prob = root.children * prob_inc
        #nod2.prob = nod2.parent.prob * prob_dec
        if n != 0:
            generate_level(nod1, n-1, inc, dec, prob_inc, prob_dec)
            generate_level(nod2, n-1, inc, dec, prob_inc, prob_dec)


root = Node(100, prob=1)
generate_level(root, 4, 0.1, 0.1, (6/10), (4/10))
print(type(root.children[1]))
print(RenderTree(root))

def main():

    print("\n\nBinary tree - Inserisci i parametri per la ricerca\n\n")

    valore_iniziale = input("Inserisci il valore iniziale:\n\n")
    incremento = input("\nInserisci percentuale di INcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    decremento = input("\nInserisci percentuale di DEcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    dec_prob = input("\nInserisci probabilità di DEcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    incr_prob = input("\nInserisci probabilità di DEcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    periodi = input("\nInserisci quanti periodi vuoi esaminare: \nattenzione alla crescita esponenziale dei calcoli [2^n, n = numero di periodi]\n\n")
    root = Node(int(valore_iniziale))
    generate_level(root, int(periodi), float(incremento), float(decremento))



#main()

