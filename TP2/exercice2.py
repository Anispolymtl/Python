def tri_bulle(tab):
    # TODO écrire l'algorithme du tri à bulle comme décrit dans l'énoncé    
    for i in range (len(tab),1, -1):
        for j in range (0, i-1):         
            if tab[j+1] < tab[j]:                
                temp = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = temp
    return tab

if __name__ == '__main__':
    val = [5,8,1,9,6,2,4,3,7,5]
    sorted_val = tri_bulle(val)
    print(val)    
    #print(sorted_val)
