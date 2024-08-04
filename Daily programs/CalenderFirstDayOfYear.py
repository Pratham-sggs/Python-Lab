print("0 = Sunday")
print("1 = Monday")
print("2 = Tuesday")
print("3 = Wednesday")
print("4 = Thursday")
print("5 = Friday")
print("6 = Saturday")
first_two_digit = 00;
last_two_digit = 00;
k = input("Enter Year :")
k = int(k);
k = k - 1;
k = str(k);
if len(k) == 4 :
    first_two_digit = int(k[0:2])
    last_two_digit = int(k[2:4])

f = int(1+int((13*11-1)/5)+last_two_digit+int(last_two_digit/4)+int(first_two_digit/4)-2*first_two_digit)
print(f%7)