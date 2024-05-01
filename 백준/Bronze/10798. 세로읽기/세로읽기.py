string_list= [input() for _ in range(5)]
string = ''

for i in range(15):
    for j in range(5):
        if len(string_list[j]) > i:
            string += string_list[j][i]
    
    
print(string)