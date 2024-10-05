cnt = 0
sum = 0
while True:
    num = input("Введите целое число [введите q для выхода]: ")
    if num.isdigit() or num == "q":
        if num == "q":
            break
        else:
            sum += int(num)
            cnt += 1
            if cnt == 2:
                break
    else:
        print("Введена буква")
print(sum)
