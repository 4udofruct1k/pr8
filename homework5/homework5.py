
sum = 0
fs = 0
fe = 0
while True:
    if fs == 1 and fe == 1:
            break
    num = input("Введите число: ")
    if num.isdigit() or num == "stop" or num == "end":
        if num == "stop":
            fs = 1
        elif num == "end":
            fe = 1
        else:
            sum += float(num)
    else:
        print("Введена буква")
print(sum)
