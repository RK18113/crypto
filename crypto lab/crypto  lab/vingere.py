def vingere(text,m,k):
    result=""
    for i in range(len(text)):
        if m =='e':
            s=ord(k[i%len(k)]) - ord('A')
        else:
            s=-(ord(k[i%len(k)])- ord('A'))

        result += chr((ord(text[i])-ord('A')+s)%26 +ord('A'))

    return result

    
m="HELLO"
k='HIH'
op=vingere(m,'e',k)
print(f'encrpted {op}')
print(f'decr {vingere(op,"d",k)}')
