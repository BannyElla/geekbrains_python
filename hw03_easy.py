# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    mult = pow(10, ndigits)
    my_round = int(number * mult + 0.5) / mult
    return my_round


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    sum_first = 0
    sum_last = 0
    for i in range(1, 7):
        temp = ticket_number % 10
        if i <= 3:
            sum_last += temp
        else:
            sum_first += temp
        ticket_number //= 10
    if sum_first == sum_last:
        return True
    else:
        False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
