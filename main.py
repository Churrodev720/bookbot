
print("hello world")
alpha_dic = {'a' : 0,
             'b' : 0,
             'c' : 0,
             'd' : 0,
             'e' : 0,
             'f' : 0,
             'g' : 0,
             'h' : 0,
             'i' : 0,
             'j' : 0,
             'k' : 0,
             'l' : 0,
             'm' : 0,
             'n' : 0,
             'o' : 0,
             'p' : 0,
             'q' : 0,
             'r' : 0,
             's' : 0,
             't' : 0,
             'u' : 0,
             'v' : 0,
             'w' : 0,
             'x' : 0,
             'y' : 0,
             'z' : 0 
            }
word_count = 0
with open("frankenstein.txt") as frank:
    file = frank.read()
    cfile = file.split()
    file = file.lower()
    lfile = list(file)
    for i in range(len(cfile)):
        word_count += 1
    for char in lfile:
        if char in alpha_dic:
            alpha_dic[char] += 1
       
    print(file)  
    sorted_dict = dict(sorted(alpha_dic.items(), key=lambda item: item[1], reverse=True))
    print(f"**Report of frankestein.txt**\nword count {word_count}")

    print(f"char count {sorted_dict}")