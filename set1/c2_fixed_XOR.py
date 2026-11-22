
HEX_INPUT = "1c0111001f010100061a024b53535009181c"
KEY = "686974207468652062756c6c277320657965"
EXPECTED = "746865206b696420646f6e277420706c6179"

def xor(data: bytes, key:bytes)->bytes:
    return bytes(d ^ k for d, k in zip(data, key, strict=True))

if __name__ == "__main__":
    raw = bytes.fromhex(HEX_INPUT)
    raw_key = bytes.fromhex(KEY)

    result = xor(raw, raw_key)
    print(result)

    assert result.hex() == EXPECTED, "Wrong answer!"




