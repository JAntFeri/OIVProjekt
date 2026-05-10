# crt_decoder.py
p1 = 4722366482869645213697
p2 = 4722366482869645213709
p3 = 4722366482869645213717

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def crt_decode(r1, r2, r3):
    moduli = [p1, p2, p3]
    remainders = [r1, r2, r3]
    
    M = p1 * p2 * p3
    M1 = M // p1
    M2 = M // p2
    M3 = M // p3
    
    y1 = mod_inverse(M1, p1)
    y2 = mod_inverse(M2, p2)
    y3 = mod_inverse(M3, p3)
    
    secret = (remainders[0] * M1 * y1 + 
              remainders[1] * M2 * y2 + 
              remainders[2] * M3 * y3) % M
    return secret

def bigint_to_text(n):
    hex_str = hex(n)[2:]
    if len(hex_str) % 2 == 1:
        hex_str = '0' + hex_str
    try:
        return bytes.fromhex(hex_str).decode('utf-8')
    except:
        return bytes.fromhex(hex_str).decode('utf-8', errors='replace')

# ==================== UPORABA ====================
if __name__ == "__main__":
    print("CRT Decoder - Skrivno sporočilo iz HTTP headerjev\n")
    
    r1 = int(input("Vnesi X-Ref-A (r1): "))
    r2 = int(input("Vnesi X-Ref-B (r2): "))
    r3 = int(input("Vnesi X-Ref-C (r3): "))
    
    secret = crt_decode(r1, r2, r3)
    message = bigint_to_text(secret)
    
    print("\n" + "="*60)
    print("Reconstructed BigInt:", secret)
    print("Decoded message:     ", message)
    print("="*60)