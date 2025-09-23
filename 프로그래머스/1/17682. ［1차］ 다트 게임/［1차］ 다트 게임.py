import re

def solution(dartResult):
    parts = re.findall(r'(\d{1,2}[SDT][*#]?)', dartResult)
    scores = []

    for i, part in enumerate(parts):
        num = int(re.match(r'\d{1,2}', part).group())
        bonus = re.search(r'[SDT]', part).group()
        option_match = re.search(r'[*#]', part)
        option = option_match.group() if option_match else ''

        if bonus == 'S':
            score = num ** 1
        elif bonus == 'D':
            score = num ** 2
        else:  # 'T'
            score = num ** 3

        if option == '*':
            score *= 2
            if i > 0:
                scores[i-1] *= 2
        elif option == '#':
            score *= -1

        scores.append(score)

    return sum(scores)
