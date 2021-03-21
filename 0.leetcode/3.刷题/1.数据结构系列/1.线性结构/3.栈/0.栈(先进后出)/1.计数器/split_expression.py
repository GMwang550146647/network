def string2list(expression):
    tempt_num = '#'
    result = []
    for char_i in expression:
        if char_i == ' ':
            continue
        elif char_i.isdigit():
            tempt_num = (tempt_num if tempt_num != '#' else 0) * 10 + int(char_i)
        else:
            if tempt_num != '#':
                result.append(tempt_num)
                tempt_num = '#'
            result.append(char_i)
    if tempt_num != '#':
        result.append(int(tempt_num))
    return result