def find_str(str1, str2):
    i = 0
    count = 0
    while i < len(str1):
        j = 0
        if str1[i] == str2[0]:
            while j < len(str2):
                if i + j >= len(str1)-1:
                    if j == len(str2)-1:
                        count += 1
                        break
                    else:
                        break
                elif str1[i + j] != str2[j]:
                    break
                elif j == len(str2)-1:
                    count += 1
                j += 1
        i += 1
    return count


s1 = 'awklmdl cSLKFelkcvfkdlawklmdyuawk'
s2 = 'LK'
print(find_str(s1, s2))
