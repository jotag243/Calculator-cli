# calculatrice en python


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


# add function
def addition(a,b):
    return a+b

# minus
def soustraction(a,b):
    return a-b

# multiplication
def multiplication(a,b):
    return a * b

# division
def division(a,b):
    if (b==0):
        print ("Impossible de diviser par 0, veuillez reesayer!\n")
        b = float(input("veuillez saisir le second nombre a calculer : "))
        return division(a,b)
    else :
        return a/b
    
# Main calculator
def calculator(a,b,op):
    a = float(a)
    b = float(b)

    rslt = float()
    
    if(op == "+"):
        rslt = addition(a,b)
        return rslt
        # print("Resultat : ",rslt)

    elif(op == "-"):
        rslt = soustraction(a,b)
        return rslt

        # print("Resultat : ",rslt)
    elif(op== "/"):
        rslt = division(a,b)
        return rslt

        # print("Resultat : ",rslt)
    elif(op == "*"):
        rslt = multiplication(a,b)
        return rslt

        # print("Resultat : ",rslt)
    else:
        print("Operation de calcul non permit, veuillez entrer un methode de calcul accepeter! ")
    print("operation terminer!\n")


global num1,num2,ope 
num1,num2,ope = entry()
   
respond = calculator(num1,num2, ope)
print(f"Resultat {respond}\n")

def iscalculDone():
    demand=input("voulez-vous continuez a partir du calcule precedent? (O ou Y pour continuer | N pour arret) ")
    while(demand != "n" and demand != "N" ):

        global respond

        global num1 
        num1 = respond

        global op
        # op = 
        operator = checkOpertor(input("Quel operation voulez-vous effectuer au calcul precedent, (+,-, *, /)? "))
        global num2
        num2 = input("Entrez le deuxieme nombre : ")

        respond = calculator(num1,num2,operator)
        print(f"Resultat : {respond}\n")
        demand=input("voulez-vous continuez a partir du calcule precedent? (O ou Y pour continuer | N pour arret) ")
    else :
        demand = input("\nD'accord!\nEntrer q pour quitter ou r pour recommencer le calcul de zero : ")
        if (demand == "q"):
            print('Bye!')
        elif (demand == "r"):
            # global num1,num2,ope 
            num1,num2,ope = entry()
            respond = calculator(num1,num2,ope)
            print(f"Resultat : {respond}\n")
            iscalculDone()
        else:
            print("commande non reconnue, veuillez reesayer!")
            demand = input("\nEntrer q pour quitter ou r pour recommencer le calcul de zero : \n")

iscalculDone()
# print(respond)


