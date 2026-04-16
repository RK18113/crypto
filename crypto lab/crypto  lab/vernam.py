#vernam
def vernam(t,k):
    t=t.upper()
    k=k.upper()
    result =""
    for i in range(len(t)):
        p=ord(t[i])- ord('A')
        kv=ord(k[i])-ord('A')
        result += chr( (p^kv) + ord('A'))
    return result

msg="HELLO"
k="THEJU"
op=vernam(msg,k)
print(f'encrytped {op}')
print(f'dec {vernam(op,k)}')

