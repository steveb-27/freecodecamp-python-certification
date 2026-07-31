def verify_card_number(cardnum):
    cardnum = str(cardnum)
    total = 0
    valid_chars = 0
    for i in range(len(cardnum)):
        rtl = len(cardnum) - i
        char = cardnum[rtl-1]
        if char not in '0123456789':
            continue
        valid_chars += 1
        digit = int(char)
        if valid_chars % 2 != 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

if __name__ == '__main__':
    print(verify_card_number('41111111 - the GOAT - 11111111'))
    print(verify_card_number('4111-1111-1111-1111'))
    print(verify_card_number('1234 5678 9012 3456'))