
from c2_fixed_XOR import xor

CIPHERTEXT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Source: https://en.wikipedia.org/wiki/Letter_frequency
COMMON = b" etaon"
COMMON_PAIRS = [b"th", b"he", b"an", b"re", b"er", b"in", b"on", b"at", b"nd", b"st", 
                b"es", b"en", b"of", b"te", b"ed", b"or", b"ti", b"hi", b"as", b"to"]

def score(text: bytes) -> int:
    text = text.lower()

    key_score = 0
    
    for b in text: 
        if b in COMMON: 
            key_score += 1

    for pair in COMMON_PAIRS:
        key_score += text.count(pair)

    return key_score


def bruteforce_xor(data: bytes) -> list[tuple[int, int, bytes]]:
    results = []
    for key in range(256):
        plaintext = xor(data, bytes([key] * len(data)))
        results.append((score(plaintext), key, plaintext))
    results.sort(reverse=True)
    return results


if __name__ == "__main__":
    raw = bytes.fromhex(CIPHERTEXT)
    top3 = bruteforce_xor(raw)[:3]
    for s, key, plaintext in top3:
        print(f"{s:3}  key={key:3} ({chr(key)!r}) {plaintext}")

    assert top3[0][1] == 88, "Wrong key!"