def pal(s):
    if s== s[::-1]:
        return True
    return False

print(pal('avava'))