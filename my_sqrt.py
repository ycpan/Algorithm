# 写出开根号，并且精确到后六位
def sqrt(x):
    l = 0
    r = x
    while(r - l >= 1e-6):
        s = (l + r)/2
        if s * s < x:
            l = s
        elif s * s > x:
            r = s
        else:
            return s
        #if abs(y*y - x) < 0.00001:
        #    return y
        #print(s)
    return l
if __name__ == '__main__':
    print(sqrt(0))
    print(sqrt(4))
    print(sqrt(5))
