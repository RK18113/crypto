#caesar
def cs(text,s,m):
    result =""
    if m=='e':
        s=s;
    else:
        s=-s;
    for c in text:
        result += chr((ord(c)-ord('A')+s)+ ord('A'))
    return result

m='HELLO';
op=cs(m,3,'e')
print(f'encrypted :{op}')
print(f'decryper: {cs(op,3,'d')}')

            

