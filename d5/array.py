def test():
    try:
        num = input()[-1]
        num = int(num)
    except:
        return ("INPUT ERROR")
    return "ODD" if int(num) in [1,3,5,7,9] else "EVEN"

print(test())