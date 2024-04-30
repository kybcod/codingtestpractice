string = input()
upper_string = string.upper()
alphabet_dict = {
    'A' : 0, 'B' : 0,'C' : 0,'D' : 0,'E' : 0,
    'F' : 0,'G' : 0,'H' : 0,'I' : 0,'J' : 0,
    'K' : 0,'L' : 0,'N' : 0,'M' : 0,'O' : 0,
    'P' : 0,'Q' : 0,'R' : 0,'S' : 0,'T' : 0,
    'U' : 0,'W' : 0,'X' : 0,'Y' : 0,'V' : 0,
    'Z' : 0
}

for ch in upper_string:
    alphabet_dict[ch] += 1

max_value = max(alphabet_dict.values())
max_list = [key for key, value in alphabet_dict.items() if value == max_value]
if len(max_list) > 1:
    print("?")
elif len(max_list) == 1:
    print(*max_list)