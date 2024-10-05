
sum = 0
cnt = 0
while True:
    num = input("Введите число: ")
    if num.isdigit() or num == "stop" or num == "end":
        if num == "stop" or num == "end":
            cnt += 1
        else:
            sum += int(num)
    else:
        print("Введена буква")
    if cnt == 2:
        break
print(sum)
