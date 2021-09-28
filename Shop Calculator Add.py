sum = 0
while(True):
    price = input('provide the item price or press "q" to quit: \n' )
    if (price != 'q'):
        sum = sum + int(price)
        print(f"the updated value is {sum}")
    else:
        print(f'thanks for shopping with us , your total bill is {sum}')
        break


