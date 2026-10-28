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
