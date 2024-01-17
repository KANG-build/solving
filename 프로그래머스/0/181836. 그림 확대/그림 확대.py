def solution(picture, k):
    new = []
    for i in picture:
        new_sentence = []
        for j in i:
            new_sentence.append(j*k)
        for i in range(k):
            new.append(''.join(new_sentence))         
    return new