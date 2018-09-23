from anytree import Node, RenderTree


def variation(to_incr, n):     #increments of n
    return to_incr*n

def generate_level(node, n, inc, dec):
       # m = m + 1
        nod1 = Node(root.name, node)
        nod2 = Node(root.name, node)
        nod1.name = nod1.parent.name + variation (nod1.parent.name, inc)
        nod2.name = nod2.parent.name - variation (nod1.parent.name, dec)
        if n != 0:
            generate_level(nod1, n-1, inc, dec)
            generate_level(nod2, n-1, inc, dec)


leaves = 2
branches = 3
root = Node(100)

def main ():

    print("\n\nBinary tree - Inserisci i parametri per la ricerca\n\n")

    valore_iniziale = input("Inserisci il valore iniziale:\n\n")
    incremento = input("\nInserisci percentuale di INcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    decremento = input("\nInserisci percentuale di DEcremento, \nper ogni periodo  [formato decimale:  se 10% --> inserisci 0.1]\n\n")
    periodi = input("\nInserisci quanti periodi vuoi esaminare: \nattenzione alla crescita esponenziale dei calcoli [2^n, n = numero di periodi]\n\n")
    root = Node(int(valore_iniziale))
    generate_level(root, int(periodi), float(incremento), float(decremento))
    print(RenderTree(root))


main()

