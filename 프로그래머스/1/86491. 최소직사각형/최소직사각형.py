def solution(sizes):
    max_h = 0
    max_w = 0

    # w,h를 미리 정렬하여 w가 h보다 저 작게 만든다.
    for card in sizes:
        w, h = sorted(card)
        max_h = max(max_h, h)
        max_w = max(max_w, w)

    return max_h * max_w