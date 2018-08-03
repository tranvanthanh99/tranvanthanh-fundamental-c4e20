F1 = 1
F2 = 2
count = 0

while count < 5:
    print("month {}: {} pair(s) of rabit".format(count,F1))
    Fn = F1 + F2
    F1 = F2
    F2 = Fn
    count += 1
