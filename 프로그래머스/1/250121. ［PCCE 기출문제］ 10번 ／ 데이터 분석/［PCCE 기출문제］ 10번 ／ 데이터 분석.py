def solution(data, ext, val_ext, sort_by):
    answer = []
    
    data_Anl = ["code", "date", "maximum", "remain"]
    ve = data_Anl.index(ext)
    sb = data_Anl.index(sort_by)
    
    for i in range(len(data)):
        if data[i][ve] < val_ext:
            answer.append(data[i]) # 행자체로 append해주기

    answer.sort(key=lambda x:x[sb])
    return answer