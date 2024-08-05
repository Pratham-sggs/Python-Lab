def modulo (a,b) :
    if b == 0 :
        return "Enter Valid Number"
    if a == 0 :
        return 0
    if a > 0 and b >0 :
        sum = 0
        while (sum<a) :
            sum = sum + b;
        if (sum>a):
            return a-sum+b;
        return a-sum;
    if a < 0 and b > 0:
        a = str(a)
        a =a[1:]
        a = int(a)
        while (a>0) :
            a = a - b;
        a = str(a)
        a =a[1:]
        a = int(a)
        return a;
    if a > 0 and b < 0 :
        sum = 0
        b = abs(b)
        while (sum<a) :
            sum = sum + b;
        if (sum>a):
            return a-sum;
        return a-sum-b;

k = modulo(40,-7) 
print(k)