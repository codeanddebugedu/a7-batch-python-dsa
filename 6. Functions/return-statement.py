def odd_even(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# def odd_even(num: int) -> None:
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


x = odd_even(10)
print(x)
