syracuse.py
#%%
def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    l = [n]
    while n != 1:
        if n%2==0:
            n = n//2
        else : 
            n = n*3 +1
        l.append(n)
    return(l)


print(syracuse(3))
# %%
def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1, n_max) : 
        louloulou = syracuse(i)
        if louloulou[-1] != 1: 
            return(False)
        
    return(True)

            



print(testeConjecture(10000))
    # %%
