from rich import print as rprint

if __name__ == "__main__":
    while(true):
        take_input()

def take_input():
    rprint('[b white on black]Welcome to the cashier software[/b white on black]')
    rprint('[italic]Enter 1 for [italic yellow]Strange "Pizza Puri"[/italic yellow][/italic]')
    rprint('[italic]Enter 2 for [italic yellow]The upside down "Basket Chaat"[/italic yellow][/italic]')
    rprint('[italic]Enter 3 for [italic yellow]Mornings are for coffee[/italic yellow][/italic]')
    rprint('[italic]Enter 4 for [italic yellow]Mouthbreather "Lemonade"[/italic yellow][/italic]')
    choice = int(input('Enter a choice:'))
    quantity = int(input('Enter the quantity:'))
    #print(choice)

    dish = ''

    if ( choice == 1 ):
        dish = "Strange 'Pizza Puri'"
        amount = 40*quantity
    elif (choice == 2):
        dish = 'The Upside down "Basket Chaat"'
        amount = 30*quantity
    elif (choice == 3):
        dish = 'Mornings are for coffee'
        horf = input("1 for Half or 2 for Full")
        if(horf == 1):
            amount = 20*quantity
        elif (horf == 2):
            amount = 35*quantity
        else:
            rprint('[red]Wrong choice![/red]')
    elif (choice == 4):
        dish = 'Mouthbreather "Lemonade"'
        amount = 20*quantity
    else:
        rprint('[red]Wrong choice![/red]')

    if(dish == '')
        rprint('[red]Try again[/red]')
    else:
        rprint(f" Dish: {dish} \n Quantity: {quantity} \n Amount: {amount}")


