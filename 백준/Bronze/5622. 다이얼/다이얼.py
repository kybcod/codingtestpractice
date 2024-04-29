cnt = 0
dial = input()
for s in dial:
    if s == 'A' or s == 'B' or s == 'C':
        cnt += 3
    elif s=='D' or s == 'E' or s == 'F':
        cnt += 4
    elif s=='G' or s == 'H' or s == 'I':
        cnt += 5
    elif s=='J' or s == 'K' or s == 'L':
        cnt += 6
    elif s=='M' or s == 'N' or s == 'O':
        cnt += 7
    elif s=='P' or s == 'Q' or s == 'R' or s == 'S':
        cnt += 8
    elif s=='T' or s == 'U' or s == 'V':
        cnt += 9
    elif s=='W' or s == 'X' or s == 'Y' or s == 'Z':
        cnt += 10
print(cnt)