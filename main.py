from rich import print as rprint
import sys
import os
from openpyxl import load_workbook

def write_to_excel(choice, quantity, amount):
    if (choice == 1):
        cn = 'B2'
        qn = 'C2'
    elif(choice ==2):
        cn = 'B3'
        qn = 'C3'
    elif(choice ==3):
        cn = 'B4'
        qn = 'C4'
    elif(choice ==4):
        cn = 'B5'
        qn = 'C5'
    elif(choice == 5):
        cn='B6'
        qn='C6'
    else:
        pass

    filename = 'data.xlsx'
    workbook = load_workbook(filename=filename)
    sheet = workbook.active
    print(cn)

    sheet[cn] = int(sheet[cn].value) + quantity
    sheet[qn] = int(sheet[qn].value) + amount

    workbook.save(filename=filename)

def take_input():
    rprint('[b white on black]Welcome to the cashier software[/b white on black]')
    rprint('[italic]Enter 1 for [italic yellow]Strange "Pizza Puri"[/italic yellow][/italic]')
    rprint('[italic]Enter 2 for [italic yellow]The upside down "Basket Chaat"[/italic yellow][/italic]')
    rprint('[italic]Enter 3 for [italic yellow]Mornings are for coffee(Half)[/italic yellow][/italic]')
    rprint('[italic]Enter 4 for [italic yellow]Mornings are for coffee(Full)[/italic yellow][/italic]')
    rprint('[italic]Enter 5 for [italic yellow]Mouthbreather "Lemonade"[/italic yellow][/italic]')
    rprint('[italic red on black]Enter 6 to exit[/italic red on black]')
    choice = int(input('Enter a choice:'))
    if(choice == 6):
        os.system('CLS')
        sys.exit()
    quantity = int(input('Enter the quantity:'))
    #print(choice)

    dish = ''
    amount = 1

    if ( choice == 1 ):
        dish = "Strange 'Pizza Puri'"
        amount = 40*quantity
    elif (choice == 2):
        dish = 'The Upside down "Basket Chaat"'
        amount = 30*quantity
    elif (choice == 3):
        dish = 'Mornings are for coffee(Half)'
        amount = 20*quantity
    elif (choice == 4):
        dish = 'Mornings are for coffee(Full)'
        amount = 35*quantity
    elif (choice == 5):
        dish = 'Mouthbreather "Lemonade"'
        amount = 20*quantity
    else:
        rprint('[red]Wrong choice![/red]')

    if(dish == ''):
        rprint('[red]Try again[/red]')
    else:
        rprint(f" Dish: {dish} \n Quantity: {quantity} \n Amount: {amount}")
        write_to_excel(choice, quantity, amount)



if __name__ == "__main__":
    while(True):
        take_input()
