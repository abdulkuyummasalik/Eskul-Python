# for number in range(10):
#     if number % 2 == 0:
#         continue
#     print(number)
    
# num = 20
# if num != 20:
#     print(f"Number {num} ")


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FezzBuzz")
        elif i % 3 == 0:
            print("Fezz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz_buzz()