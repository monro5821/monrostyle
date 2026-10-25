password = input("Введите пароль: ")
count_lower = 0
count_upper = 0
count_special = 0
count_digit = 0 
if len(password) < 8 :
    print("Пароль слишком короткий")
else:
    if any (i.islower() for i in password):
        count_lower+=1
    elif any (i.isupper() for i in password):
        count_upper+=1
    elif any (i.isdigit() for i in password):
        count_digit+=1
    else: 
        count_special +=1
if (count_special == 0 ) | (count_digit == 0) | (count_lower == 0)| (count_upper == 0):
    print("Не удовлетворяет условиям")
else:
    print ("Пароль корректен ")
