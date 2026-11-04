def xor_division(dividend, divisor):
    bits = list(dividend)
    n = len(divisor)
    for i in range(len(dividend) - n + 1):
        if bits[i] == "1":
            for j in range(n):
                bits[i + j] = "0" if bits[i + j] == divisor[j] else "1"
    return "".join(bits[-(n - 1):]) if n > 1 else ""

def valid_bits(value):
    return bool(value) and all(bit in "01" for bit in value)

data = input("Enter Data Bits: ").strip()
key = input("Enter Generator Polynomial: ").strip()
if not valid_bits(data) or not valid_bits(key) or len(key) < 2 or key[0] != "1":
    raise SystemExit("Enter valid binary data and a generator beginning with 1 (at least 2 bits).")

remainder = xor_division(data + "0" * (len(key) - 1), key)
codeword = data + remainder
print("CRC Remainder:", remainder)
print("Transmitted Codeword:", codeword)

received = input("Enter Received Codeword: ").strip()
if not valid_bits(received) or len(received) < len(key):
    raise SystemExit("Enter a valid received binary codeword.")
check = xor_division(received, key)
print("No Error Detected" if set(check) <= {"0"} else "Error Detected")
