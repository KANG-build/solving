def solution(my_string):
    box = []
    keep = []
    for idx, i in enumerate(my_string):
        if i.isdigit():  # 숫자라면
            string = ''
            while my_string[idx].isdigit():
                if idx not in keep:
                    string += my_string[idx]
                keep.append(idx)
                idx += 1
                
                if idx >= len(my_string):
                    break
                
            if string:
                box.append(int(string))
    return sum(box)