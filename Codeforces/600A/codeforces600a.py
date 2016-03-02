def find_strings(original):
    digits = "0123456789"
    a = []
    b = []
    for word in original:
        wordB = False
        if len(word) is 0:
            b.append(word)
            wordB = True
        for x in word:
            if word[0] is '0' and len(word) > 1:
                b.append(word)
                wordB = True
                break
            if x not in digits:
                b.append(word)
                wordB = True
                break
        if not wordB:
            a.append(word)
    if len(a) is 0:
        print "-"
    else:
        aPrint = "\""
        counter = 0
        for x in a:
            aPrint = aPrint + x
            counter = counter + 1
            if counter is not len(a):
                aPrint = aPrint + ","
        aPrint = aPrint + "\""
        print aPrint
    if len(b) is 0:
        print "-"
    else:
        bPrint = "\""
        counter = 0
        for x in b:
            bPrint = bPrint + x
            counter = counter + 1
            if counter is not len(b):
                bPrint = bPrint + ","
        bPrint = bPrint + "\""
        print bPrint

import re
original = raw_input()
original = re.split(';|,', original)
find_strings(original)
