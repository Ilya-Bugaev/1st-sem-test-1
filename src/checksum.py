def modulo11_checksum(is_bn_number: str):

    if not isbn_number or not isinstance(isbn_number, str):
        raise ValueError("Invalid input: must be non-empty string")
    

    digits = [int(char) for char in is_bn_number if char.isdigit()]

    check_digit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight

    checksum = total % 11
    return checksum == check_digit


while True:
    isbn = input("ISBN: ").strip()
    if isbn == "-1":
        break
    if check_isbn(isbn):
        print("correct")
    else:
        print("incorrect")
