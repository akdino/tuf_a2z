d={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

def rec(lst,ind):

    if ind==len(digits):
        final.append("".join(lst[:]))
    for i in range(ind,len(digits)):
        for j in d[digits[i]]:
            lst.append(j)
            rec(lst,i+1)
            lst.pop()
    return final

final=[]
digits="23"
k=rec([],0)
print(k)


#better version


final = []
def rec(lst, ind):
    if len(lst) == len(digits):   
        final.append("".join(lst))
        return
    
    for j in d[digits[ind]]:      
        lst.append(j)
        rec(lst, ind+1)           
        lst.pop()

rec([], 0)
