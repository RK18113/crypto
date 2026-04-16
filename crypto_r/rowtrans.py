def rt_enc(text, key, rows, cols):
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(cols):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1
            else:
                matrix[i][j] = 'X'

    cipher = ""
    for k in key:   # column order
        col_index = k - 1
        for r in range(rows):
            cipher += matrix[r][col_index]

    return cipher


def rt_dec(cipher, key, rows, cols):
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for k in key:
        col_index = k - 1
        for r in range(rows):
            matrix[r][col_index] = cipher[index]
            index += 1

    plaintext = ""
    for i in range(rows):
        for j in range(cols):
            plaintext += matrix[i][j]

    return plaintext

text = "HELLOWORLD"
key = [3,1,4,2]
rows = 3
cols = 4
