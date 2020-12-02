liste_de_lexo = [1, 5 ,6 ,8, 10, 90]
for i in range(len(liste_de_lexo)): 
    som= sum(liste_de_lexo)
print(som)


liste_exodeux = [5,8,15,17]
for i in range(len(liste_exodeux)) : 
    liste_exodeux.sort()
print(liste_exodeux[-1])


for element in liste_de_lexo : 
    if element in liste_exodeux : 
        print(element)

liste_pair = []
liste_impair = []



liste_de_lexo = [2,4,6,8,10]
liste_pairun = []
liste_impairdeux = []
for i in liste_de_lexo : 
    if i%2==0 :
        liste_pairun.append(i)
    else : 
        liste_impairdeux.append(i)

print(liste_pairun, liste_impairdeux)
#%%
listee = []
liste_exodeux = [2,2,4,6,8,10]
liste_exodeux.sort()
k = 0
j = 0
for i in range(len(liste_exodeux)-2) :
    j = liste_exodeux[i]
    k = liste_exodeux[i+1]
    if j == k : 
        del liste_exodeux[i]

print(liste_exodeux)

l

# %%
liste_co = ["hguihjdhufhuhjfhjghfhj", "fgfhjioshjhdjfk", "ghugnjfkose", "gjig"]
liste_co.sort(key=len)
print(liste_co)
del liste_co[-1]
print(liste_co)
# %%
liste_bi = [1,1,1,1,5,5,5,5,6,5,8]
liste_bi = list(dict.fromkeys(liste_bi))
print(liste_bi)
# %%
