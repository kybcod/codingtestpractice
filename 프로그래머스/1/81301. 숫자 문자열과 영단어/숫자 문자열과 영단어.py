def solution(s):

    dic = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    answer = s
    for key, value in dic.items():
        answer = answer.replace(key, value)
        
    # answer = ''
    # word = ''

#     for i in s:
#         if i.isalpha():
#             word += i
#             if word in dic:
#                 answer += dic[word]
#                 word = ''
#         else:
#             answer += i

    return int(answer)