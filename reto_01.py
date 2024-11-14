def decoder(number, code):
    number_str = str(number)
    ar_numbers = [int(x) for x in number_str]
    ar_codes = list(code)
    n = len(ar_numbers)
    i = 0

    for c in ar_codes:
        num = ar_numbers[i]
        num, i, n = actions(c,num,i,n)
        if c == 'U' or c == 'D':
            ar_numbers[i] = num
    result = int(''.join(str(digit) for digit in ar_numbers))
    return result

def actions(letter,num, i, n):
    if letter == 'R' and i == n-1 :
        i = 0
    elif letter == 'R' and i < n-1:
        i += 1
    elif letter == 'L' and i == 0:
        i = n-1
    elif letter == 'L' and i > 0:
        i -= 1
    elif letter == 'U' and num == 9:
        num = 0
    elif letter == 'U' and num < 9:
        num += 1
    elif letter == 'D' and num == 0:
        num = 9
    elif letter == 'D' and num > 0:
        num -= 1
    return num, i, n

print(decoder(528934712834,'URDURUDRUDLLLLUUDDUDUDUDLLRRRR'))
