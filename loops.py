print("-"*100)
# to start
print("this is a training ment for me to learn boucle in pyhton...")
print("-"*100)
print("-"*100)







# fro the boucle for we have:
i=1
for i in range(1,10):
   print(f"{i} je sui plus inteligeant que j'ai ne le croix.")
   i+=1
print("-"*100)

a=[]
for a in [1,2,3,4,5]  :
    print(a)
print("-"*100)
print("-"*100)








#for the boucle while we have:
y=1
while y<10 :
    print (f"{y}je me sant bien.")
    y+=1
print("-"*100)


Continue="o"
while Continue=="o":
    a=input("comment vous vous appellez?:")
    print(f"ravie de faire votre connaisance {a} .")
    print("-"*100)

   #As long as your responce is o you will continue giving your name
    Continue=input("vouler vous continue? o/n :")
    print("-"*100)








#petite exercice avec la boucle while true 
mdp = input("saisisez votre mot de passe(min 8 caractaire):")
mdp_cour= ("mot de passe tros cours !")

while True :
    if len(mdp) == 0 :
        print(mdp_cour)
        mdp = input("saisisez votre mot de passe(min 8 caractaire):")
    elif len(mdp) < 8 :
        print(mdp_cour)
        mdp = input("saisisez votre mot de passe(min 8 caractaire):") 
    elif mdp.isdigit() :
        print("votre mot de passe ne contien que des nombre ")
        mdp = input("saisisez votre mot de passe(min 8 caractaire):")  
    else:
        print ("inscription termine ")
        break  
      
print("-"*100)