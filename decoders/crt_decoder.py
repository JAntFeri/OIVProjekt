# crt_decoder.py

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

def crt_decode(remainders, moduli):
    """
    General CRT decoder.
    remainders: [r1, r2, r3]
    moduli: [p1, p2, p3]
    """
    M = 1
    for m in moduli:
        M *= m
    
    secret = 0
    for i in range(len(moduli)):
        Mi = M // moduli[i]
        yi = mod_inverse(Mi, moduli[i])
        secret += remainders[i] * Mi * yi
        
    return secret % M

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
    print("--- CRT Decoder Shell ---")
    print("Vnesi vrednosti za rekonstrukcijo skrivnosti.\n")
    
    p1 = int(input("Vnesi Modulo P1: "))
    p2 = int(input("Vnesi Modulo P2: "))
    p3 = int(input("Vnesi Modulo P3: "))
    
    print("-" * 30)
    
    r1 = int(input("Vnesi ostanek r1 (X-Ref-A): "))
    r2 = int(input("Vnesi ostanek r2 (X-Ref-B): "))
    r3 = int(input("Vnesi ostanek r3 (X-Ref-C): "))
    
    secret = crt_decode([r1, r2, r3], [p1, p2, p3])
    message = bigint_to_text(secret)
    
    print("\n" + "="*60)
    print(f"Rekonstruirano število: {secret}")
    print(f"Decoded message:      {message}")
    print("="*60)