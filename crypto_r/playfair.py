def generate_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []
    
    for char in key + string.ascii_uppercase:
        if char not in seen and char != "J":
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    for i in range(5):
        for j in range(5):
            if char == matrix[i][j]:
                return i, j

def split_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    split = []
    i = 0
    
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            split.append((a, 'X'))
            i += 1
        else:
            split.append((a, b))
            i += 2
    return split       

def playfair_enc(text, key):
    matrix = generate_matrix(key)
    split = split_text(text)
    result = ""

    for a, b in split:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1+1) % 5] + matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            result += matrix[(r1+1) % 5][c1] + matrix[(r2+1) % 5][c2]
        else: 
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

def playfair_dec(cipher, key):
    matrix = generate_matrix(key)
    split = [(cipher[i], cipher[i+1]) for i in range(0, len(cipher), 2)]
    result = ""

    for a, b in split:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1) % 5] + matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            result += matrix[(r1-1) % 5][c1] + matrix[(r2-1) % 5][c2]
        else: 
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

# text = "hello"
# key = "bye"
# cipher = playfair_enc(text, key)
# print(cipher)
# print(playfair_dec(cipher, key))
