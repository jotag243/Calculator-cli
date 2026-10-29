# calculatrice CLI en python
from operator import addition, soustraction, division,multiplication

def checkOpertor(op):
    operator =("+", "-", "/", "*")
    while(op  not in operator ):
        print("Operation de calcul non permit, veuillez entrer un methode de calcul accepeter! ")
        op = input("Veuillez reesayer! : ")
        
    return op

def isThisNumber(numb):
    try:
        numb = float(numb)
        return numb
    except ValueError:
        print("la valeur entrer n'est pas un chiffre ou un nombre reesayer!\n")
        return entry()


def entry():

    num1 = input("veuillez saisir le premier nombre a calculer : ")
    num1 =isThisNumber(num1)

    operator = checkOpertor(input("Veuillez saisir l'operation a effectuer (+,-, *, /) : "))

    num2= input("veuillez saisir le second nombre a calculer : ")
    num2 = isThisNumber(num2)
    return num1,num2,operator



num1,num2,ope = entry()

# Main calculator
def calculator(a,b,op):
    # a = float(a)
    # b = float(b)

    # global rslt

    match op:
        case "+":
            rslt= addition(a,b)
            return rslt,iscalculDone(rslt)
        case "-":
            rslt = soustraction(a,b)
            return rslt,iscalculDone(rslt)
        case "/":
            rslt = division(a,b)
            return rslt,iscalculDone(rslt)
        case "*":
            rslt = multiplication(a,b)
            return rslt,iscalculDone(rslt)
        case _:
            print("Operation de calcul non permit, veuillez entrer un methode de calcul accepeter! ")


def iscalculDone(rslt):
    
    print(f"Resultat {rslt}\n")
    demand=input("voulez-vous continuez a partir du calcule precedent? (O ou Y pour continuer | N pour arret) ")
    while(demand != "N".lower and demand == "Y".lower()):
        # global op,a,b
        a = rslt
        op = checkOpertor(input("Quel operation voulez-vous effectuer au calcul precedent, (+,-, *, /)? "))
       
        b = input("Entrez le deuxieme nombre : ")
        b = isThisNumber(b)
        rslt = calculator(a,b,op)
        print(f"Resultat : {rslt}\n")

        demand=input("voulez-vous continuez a partir du calcule precedent? (O ou Y pour continuer | N pour arret) ")

    demand = input("\nD'accord!\nEntrer q pour quitter ou r pour recommencer le calcul de zero : ")
    if (demand == "q".lower()):
            print('Bye!')
    elif (demand == "r".lower()):
        
        a,b,op = entry()
        rslt = calculator(a,b,op)
        # print(f"Resultat : {rslt}\n")
        # iscalculDone()
    else:
        print("commande non reconnue, veuillez reesayer!")
        demand = input("\nEntrer q pour quitter ou r pour recommencer le calcul de zero : \n")
calculator(num1,num2, ope)


