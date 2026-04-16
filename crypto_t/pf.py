def creatematrix(k):
    k=k.upper().replace("J","I")
    m =[]
    seen=set()
    for char in k +"ABCDEFGHIKLMNOPQRSTUVWXYZ":
          if char not in seen:
               seen.add(char)
               m.append(char)

    return [m[i:i+5] for i in range(0,25,5)]

def findpos(m,c):
    for idx,val in enumerate(m):
        if c in val:
            return idx,val.index(c)



def encrypt(text,key):
    text = text.upper().replace("J","I")
    matrix=creatematrix(key)
    nt=""
    i=0
    op=""
    while i <len(text):
        a=text[i]
        b=text[i+1] if i+1 <len(text) else "X"

        if(a==b):
             nt+=a+"X"
             i+=1
        else:
             nt+=a+b
             i+=2

    for j in range(0, len(nt), 2):
        r1,c1=findpos(matrix,nt[j])
        r2,c2=findpos(matrix,nt[j+1])
        if(r1==r2):
            op+=matrix[r1][(c1+1)%5]+matrix[r2][(c2+1)%5]
        elif(c1==c2):
            op+=matrix[(r1+1)%5][c1]+matrix[(r2+1)%5][c2]
        else:
            op+=matrix[r1][c2] + matrix[r2][c1]
    return op

def decrypt(text,key):
    text = text.upper().replace("J","I")
    matrix=creatematrix(key)
    nt=text
    i=0
    op=""
 

    for j in range(0, len(nt), 2):
        r1,c1=findpos(matrix,nt[j])
        r2,c2=findpos(matrix,nt[j+1])
        if(r1==r2):
            op+=matrix[r1][(c1-1)%5]+matrix[r2][(c2-1)%5]
        elif(c1==c2):
            op+=matrix[(r1-1)%5][c1]+matrix[(r2-1)%5][c2]
        else:
            op+=matrix[r1][c2] + matrix[r2][c1]
    return op
    

key_word = "MONARCHY"
message = "INSTRUMENTS"

cipher_text = encrypt(message, key_word)

print(f"Matrix: {creatematrix(key_word)}")
print(f"Encrypted: {cipher_text}")
print(f"Encrypted: {decrypt(cipher_text,key_word)}")