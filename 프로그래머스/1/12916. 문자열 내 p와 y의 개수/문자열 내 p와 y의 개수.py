from collections import Counter
def solution(s):

    st = s.upper()
    cnt = Counter(st)

    if cnt["P"] == cnt["Y"]:
        return True
    else:
        return False