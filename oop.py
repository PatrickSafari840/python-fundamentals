#declaration de la class
class Plante:
    feille = "feille"
    tige = "tige"
    rasine = "rasine"
    


# test de verification de la class
print("-"*100)
print(Plante.feille)
print(Plante.tige)
print(Plante.rasine)


# creation d'instance par afectation de variable a des variable 
print("-"*100)
pomier = Plante()
mangier = Plante()
rosier = Plante()


pomier.feille = "lisse"
pomier.rasine = "tibereuse"
pomier.tige = "droitte"


print(pomier.feille)
print(pomier.tige)
print(pomier.rasine)

print("-"*100)

