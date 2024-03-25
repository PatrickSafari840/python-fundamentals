#la declaration d'une list
print("-"*100)
nom = input("nom : ")
postnom = input("post-nom : ")
prenom = input("pre-nom: ")
age = input("age: ")
a = [nom ,postnom ,prenom ,age] 
print(a)



#suprimer un element d'une list
print("-"*100)
a.remove(nom)
print(a)



#ajoute un element a une list
print("-"*100)
b = []
b.append(["amen !","alleluilla !","thanks !"])
print(b)



#ajoute plusieur element dans une list
print("-"*100)
c = []
c.extend([1,2,3,4,5])
print(b)


print("-"*100)
# la declaration des dictionnaire :::::
dictionaire = {
    0 : {"prenom ": "patrick",
        "nom":"cimana",
        "age":"23"},
    1 : {"prenom ": "bertran",
        "nom":"civil",
        "age":"22"},
    2 : {"prenom ": "niriam",
        "nom":"dwenyn",
        "age":"25"},
    2 : {"prenom ": "norine",
        "nom":"sun",
        "age":"20"}
}
print(dictionaire[0]["prenom "])
print("-"*100)

 