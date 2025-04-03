def calculate(physics, chemistry, english, hindi, computer):
    print(f"physics = {physics}")
    print(f"chemistry = {chemistry}")
    print(f"english = {english}")
    print(f"hindi = {hindi}")
    print(f"computer = {computer}")
    total = physics + chemistry + english + hindi + computer
    print(f"Your total marks = {total}")


# calculate(35, 17, 82)
# calculate(52, 74)

# Named Arguments
calculate(5, 10, hindi=65, english=100, computer=43)
