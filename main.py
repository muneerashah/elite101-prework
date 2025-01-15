print("Welcome to the Instrument Info Installment!!")
name = input('What is your name?  ')

current_year = input(f'Hello {name}!!, what year is it currently?  ')

birth_year = input(f'And {name}, what year were you born?    ')

age = current_year - birth_year
if age < 10:
    print(f"oops!! {name}, you're too young to be here! please start over !!")
