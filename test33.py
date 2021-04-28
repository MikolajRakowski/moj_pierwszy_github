lista3=[]
def dodawanie(lista1, lista2, lista3):
    if len(lista1)>0:
        dodaj = lista1[0] + lista2[0]
        lista3.append(dodaj)
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])
        return dodawanie(lista1, lista2, lista3)
    else:
        return lista3

lista4=[3, 2, 1, 5]
lista5=[1, 7, 3, 4]
koncowy_wynik=dodawanie(lista4, lista5, lista3)
print(koncowy_wynik)
lista3.clear()

lista6=[7, 2, 4, 6, 6]
lista7=[2, 4, 1, 5, 3]
koncowy_wynik=dodawanie(lista6, lista7, lista3)
print(koncowy_wynik)
lista3.clear()

lista6=[1, 9, 4, 12, 31, 43]
lista7=[6, 1, 6, 9, 12, 15]
koncowy_wynik=dodawanie(lista6, lista7, lista3)
print(koncowy_wynik)
lista3.clear()
