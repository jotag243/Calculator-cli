from operator import addition, soustraction, division,multiplication

# calculatrice CLI en python


def checkOpertor(op):
    while (op!="+" and op!="-" and op!="*" and op!="/"):
        print("Operation de calcul non permit, veuillez entrer un methode de calcul accepeter! ")
        op = input("Veuillez reesayer! : ")
        
    return op

def entry():

    num1 = input("veuillez saisir le premier nombre a calculer : ")


    operator = checkOpertor(input("Veuillez saisir l'operation a effectuer (+,-, *, /) : "))

    num2= input("veuillez saisir le second nombre a calculer : ")
    return num1,num2,operator



num1,num2,ope = entry()

# Main calculator
def calculator(a,b,op):
    a = float(a)
    b = float(b)

    global rslt

    match op:
        case "+":
            rslt= addition(a,b)
            return rslt
        case "-":
            rslt = soustraction(a,b)
            return rslt
        case "/":
            rslt = division(a,b)
            return rslt
        case "*":
            rslt = multiplication(a,b)
            return rslt
        case _:
            print("Operation de calcul non permit, veuillez entrer un methode de calcul accepeter! ")

    print("operation terminer!\n")
    print(rslt)

    def iscalculDone():
        print(f"Resultat {rslt}\n")
        demand=input("voulez-vous continuez a partir du calcule precedent? (O ou Y pour continuer | N pour arret) ")
        while(demand != "N".lower ):
            global op,a,b

            a = rslt
            op = checkOpertor(input("Quel operation voulez-vous effectuer au calcul precedent, (+,-, *, /)? "))
       
            b = input("Entrez le deuxieme nombre : ")

            rslt = calculator(num1,num2,op)
            print(f"Resultat : {rslt}\n")

            demand=input("voulez-vous continuez a partir du calcule precedent? (O ou Y pour continuer | N pour arret) ")

        demand = input("\nD'accord!\nEntrer q pour quitter ou r pour recommencer le calcul de zero : ")
        if (demand == "q".lower()):
            print('Bye!')
        elif (demand == "r".lower()):
            # global num1,num2,ope 
            num1,num2,ope = entry()
        # rslt = calculator(num1,num2,ope)
            print(f"Resultat : {rslt}\n")
            iscalculDone()
        else:
            print("commande non reconnue, veuillez reesayer!")
            demand = input("\nEntrer q pour quitter ou r pour recommencer le calcul de zero : \n")

# global num1,num2,ope 
# num1,num2,ope = entry()

calculator(num1,num2, ope)
# print(f"Resultat {respond}\n")

# print(respond)


