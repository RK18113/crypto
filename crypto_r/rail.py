def railfence_enc(text, key):
    rail = ['' for _ in range(key)]
    row, direction = 0, 1
    
    for char in text:
        rail[row] += char
        row += direction

        if row == 0 or row == key-1:
            direction *= -1

    cipher = ''.join(rail)
    return cipher

def railfence_dec(cipher, key):
    rail = [[' '] * len(cipher) for _ in range(key)]
    row, direction = 0, 1

    for col in range(len(cipher)):
        rail[row][col] = '*'
        row += direction

        if row == 0 or row == key-1:
            direction *= -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    for r in rail:
        print(" ".join(r))

    result = ""
    row, direction = 0, 1
    for col in range(len(cipher)):
        result += rail[row][col]
        row += direction

        if row == 0 or row == key-1:
            direction *= -1

    return result

text = "helloworld"
key = 3
cipher = railfence_enc(text, 3)
print(cipher)
print(railfence_dec(cipher, 3))
