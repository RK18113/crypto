#sdes
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IPI = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

def permute(data,perm):
    return [data[i-1] for i in perm]


def shift(data,s):
    return data[s:]+data[:s]

def sboxlp(data,s):
    row = int( f'{data[0]}{data[3]}',2)
    col = int( f'{data[1]}{data[2]}',2)
    val=s[row][col]
    

    return [int(b) for b in format(val,'02b')]

def cf(data,key):
    
    l,r=data[:4],data[4:]
    exp=permute(r,EP)
    temp=[exp[i]^key[i] for i in range(8)]
    op=sboxlp(temp[0:4],S0) + sboxlp(temp[4:],S1)
    op = permute(op,P4)
    op=[op[i]^l[i] for i in range(4)]
    return r+op

def  kg(key):
    op=permute(key,P10)
    l1,r1=shift(op[:5],1),shift(op[5:],1)
    k1 = permute(l1+r1,P8)

    l2,r2=shift(l1,1),shift(r1,1)
    k2=permute(l2+r2,P8)
    return k1,k2

pt = [1, 0, 0, 1, 0, 1, 1, 1]
master_key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
print(pt)


pt=permute(pt,IP)


k1,k2=kg(master_key)

inter=cf(pt,k1)
inter= inter[4:]+inter[:4]
ct=cf(inter,k2)
ct=permute(ct,IPI)
print('ct = ',ct)

