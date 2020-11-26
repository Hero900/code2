import os
import json


do_ch = os.path.dirname(__file__)
fi = os.path.join(do_ch,'poi.json')
if os.path.exists(fi):
    with open(fi,"r") as f:
        liste = json.load(f)
else:
    liste = []

afi = """
\t1
\t2
\t3
\t4
\t5
"""
op = "0"

print('\tBonjour Yan')
while op != "5":
    op = input(afi +"\n\top:")

    if op == "1":
        test = input("text:")
        liste.append(test)
    elif op == "2":
        liste.clear()
    elif op == "3":
        print("\n".join(liste))

    elif op == "4":
        rm = input('\n\trm:')
        if rm in liste:
            liste.remove(rm)

with open(fi,"w") as f:
    json.dump(liste,f)

print('Fini')
        
    

    