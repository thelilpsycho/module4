a ='abcdfaa'
'''
def strcounter(s):
    counter=0
    for sym in s:
        counter +=1
    print(counter)
strcounter(a)
'''
'''
def strcounter(s):
    for sym in s:
        counter=0
        for sub_sym in s:
            if sym==sub_sym:
                counter +=1
            print(sym, counter)

strcounter(a)
'''
'''
def strcounter(s):
    for sym in set(s):
        counter=0
        for sub_sym in s:
            if sym==sub_sym:
                counter+=1
        print(sym,counter)

strcounter(a)
'''

def strcounter(s):
    sym_counter={}
    for sym in s:
        sym_counter[sym]=1
    print(sym_counter)

strcounter(a)
