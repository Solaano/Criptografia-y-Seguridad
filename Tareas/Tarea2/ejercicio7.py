import base64

IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

FP = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

P = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

KEY_SHIFT = [
    1,1,2,2,2,2,2,2,
    1,2,2,2,2,2,2,1
]

S_BOXES = [
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],

    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],

    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
     [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
     [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
     [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],

    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
     [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],

    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
     [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
     [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
     [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],

    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
     [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
     [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
     [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],

    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
     [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
     [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
     [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],

    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
     [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
     [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
     [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]


# ==========================================
# FUNCIONES DES
# ==========================================

def pad(data):
    if len(data) % 8 == 0:
        return data
    padding_len = 8 - (len(data) % 8)
    return data + bytes([padding_len] * padding_len)


def unpad(data):
    if not data:
        return data
    padding_len = data[-1]
    if 0 < padding_len < 8:
        return data[:-padding_len]
    return data


def permute(block, table, bits):
    result = 0
    for p in table:
        result = (result << 1) | ((block >> (bits - p)) & 1)
    return result


def left_rotate(val, shift, size):
    return ((val << shift) & ((1 << size) - 1)) | (val >> (size - shift))


def sbox_substitution(block):
    result = 0
    for i in range(8):
        chunk = (block >> (42 - 6*i)) & 0x3F
        row = ((chunk & 0x20) >> 4) | (chunk & 1)
        col = (chunk >> 1) & 0xF
        result = (result << 4) | S_BOXES[i][row][col]
    return result


def generate_keys(key):
    keys = []
    key = permute(key, PC1, 64)
    left = (key >> 28) & 0xFFFFFFF
    right = key & 0xFFFFFFF
    for shift in KEY_SHIFT:
        left = left_rotate(left, shift, 28)
        right = left_rotate(right, shift, 28)
        combined = (left << 28) | right
        keys.append(permute(combined, PC2, 56))
    return keys


def des_block(block, keys):
    block = permute(block, IP, 64)
    left = (block >> 32) & 0xFFFFFFFF
    right = block & 0xFFFFFFFF
    for k in keys:
        temp = right
        right = permute(right, E, 32)
        right ^= k
        right = sbox_substitution(right)
        right = permute(right, P, 32)
        right ^= left
        left = temp
    combined = (right << 32) | left
    return permute(combined, FP, 64)


def des_encrypt(data, key):
    data = pad(data)
    keys = generate_keys(key)
    result = b""
    for i in range(0, len(data), 8):
        block = int.from_bytes(data[i:i+8], "big")
        enc = des_block(block, keys)
        result += enc.to_bytes(8, "big")
    return result


def des_decrypt(data, key):
    keys = generate_keys(key)
    keys.reverse()
    result = b""
    for i in range(0, len(data), 8):
        if len(data[i:i+8]) < 8:
            continue
        block = int.from_bytes(data[i:i+8], "big")
        dec = des_block(block, keys)
        result += dec.to_bytes(8, "big")
    return unpad(result)


# ==========================================
# FUNCIONES PLAYFAIR
# ==========================================

def create_playfair_matrix(key):
    key = "".join([c.upper() for c in key if c.isalpha()]).replace("J", "I")
    matrix_letters = []
    for char in key:
        if char not in matrix_letters:
            matrix_letters.append(char)
            
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix_letters:
            matrix_letters.append(char)
            
    matrix = [matrix_letters[i:i+5] for i in range(0, 25, 5)]
    return matrix


def print_matrix(matrix):
    print("Matriz Playfair generada:")
    for row in matrix:
        print(" ".join(row))
    print()


def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    print_matrix(matrix)
    
    def find_pos(letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None
        
    ciphertext = "".join([c.upper() for c in ciphertext if c.isalpha()])
    
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1] if i+1 < len(ciphertext) else 'X'
        
        pos1 = find_pos(char1)
        pos2 = find_pos(char2)
        
        if not pos1 or not pos2:
            continue 
            
        r1, c1 = pos1
        r2, c2 = pos2
        
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]
            
    return plaintext


# ==========================================
# EJECUCIÓN
# ==========================================

if __name__ == "__main__":
    print("-" * 60)
    print(" Encontramos la clave correspondiente:")
    print("-" * 60)
    
    ciphertext_b64 = "h+F7XMoHpF0="
    cipher_bytes = base64.b64decode(ciphertext_b64)
    
    lista_claves = [
        "root#001", "admin@02", "exploit$", "buffer%1", "shell&01", "kernel*1", 
        "hacker+1", "crack=01", "patch?01", "bug!0001", "zero^001", "ovfl~001", 
        "malw@001", "trojan<1", "worm>001", "virus/01", "payld:01", "script;1", 
        "sql_inj1", "inject-1", "brute#01", "force@01", "hash$001", "salt%001", 
        "cipher&1", "crypto*1", "key+0001", "lock=001", "token?01", "cookie!1", 
        "phish^01", "spoof~01", "spam|001", "botnet<1", "ddos>001", "flood/01", 
        "nmap:001", "burp@001", "zap-0001", "proxy#01", "tunnel@1", "vpn$0001", 
        "tor%0001", "onion&01", "dark*001", "net+0001", "deep=001", "web?0001", 
        "rootkit1", "backdr^1", "keylog~1", "sniff|01", "trace<01", "forge>01", 
        "mask/001", "cloak:01", "stealth1", "breach01", "leak-001", "dump#001", 
        "scan@001", "port$001", "firew%01", "IDS&0001", "IPS*0001", "SIEM+001", 
        "sPyWar3?", "alert=01", "log?0001", "audit!01", "secure^1", "safe~001", 
        "vault|01", "shield<1", "guard>01", "protect1", "defense1", "code;001", 
        "binary01", "sudo-001", "passwd01", "ssh@0001", "cert$001", "tls%0001", 
        "ssl&0001", "hash*001", "enc+0001", "dec=0001", "xor?0001", "key!0001", 
        "auth^001", "token~01", "user|001", "root<001", "admin>01", "sys/0001", 
        "net:0001", "hack;001", "vuln_001", "exploit1"
    ]

    
    playfair_key_encontrada = None

    for posible_clave in lista_claves:
        try:
            key_bytes = posible_clave.encode("utf-8")
            key_int = int.from_bytes(key_bytes, "big")
            
            decrypted_bytes = des_decrypt(cipher_bytes, key_int)
            decrypted_text = decrypted_bytes.decode("utf-8")
            
            print(f"Clave encontrada en DES: '{posible_clave}'")
            print(f"Clave Playfair: '{decrypted_text}'\n")
            playfair_key_encontrada = decrypted_text
            break 
            
        except (UnicodeDecodeError, Exception):
            pass
            

    print("-" * 60)
    print("DESCIFRADO PLAYFAIR")
    print("-" * 60)
    
    texto_cifrado_playfair = """
    SHPETXSQZNSPLBMBWFFKCEBRBQMVQSEGOLRBLGXPPSUXHWLGXPDL-
    SZSNAZINELFTEQRGTSRIFWKBRGZVNPWKBQPGPBMZOMGEQMXPHGUF
    
    DIKBSCMGQMSHVZXTQMFXFOGPSHBWIOSNOQNPWKKCOQMFAVSHSM-
    FOSNDKHGMVSZSHQPIYSQAVPNEGCERZQBQOKSSCOFOHPYQSBKQOZSHP
    
    FKEGKCRLSNQOIKOQOWPSTDPSBRAVGMVZQZKGFRZVVPZVSHPG-
    VAOHRBGEZVEQHGWMKSNSZSRZPHZVPSZSIRDLSNAZINDLOBFWSKGPZS
    
    3
    
    MZQZOWMCAVSHGRMPXGNSPGFPKFHBMGSQSGPEKGQSFSSNOW-
    BLPYSQKBSQBRQSEFSGKSKSUXHWLGXPZSZSNSZKRGFZQPOQDYSXTFRZQ
    
    MPQRGXECNZPCEGLBQNQPCMESNOWBLPYSCGSOHQPFSRIFWKBQB-
    DTQOQNDOZVMIZPUFDIKBSCNGRYCYBLQGBQOQZAMRZPBRPESNGRQEPE
    
    SNVPVZBKZVVPPSKSSPQBKGBKQOBKWHKDZVYMMGMQZLKEIOEQGLBR-
    WHUXFOSPZSGPGFQOGKAV
    """
    
    print(f"Usando clave obtenida: {playfair_key_encontrada}")
    print("-" * 50)
    
    mensaje_claro = playfair_decrypt(texto_cifrado_playfair, playfair_key_encontrada)
    
    print("Mensaje Descifrado:")
    print(mensaje_claro)