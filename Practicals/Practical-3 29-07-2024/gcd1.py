def gcd (*a) :
    minimum_num=min(a)
    total_len = len(a)
    while(minimum_num>0) :
        number = 0
        for i in range (total_len) :
            if(a[i] % minimum_num==0) :
                number=number+1
                if(number==total_len):
                    break
        minimum_num = minimum_num-1;
    return minimum_num
k =gcd(16,24)
print(k);