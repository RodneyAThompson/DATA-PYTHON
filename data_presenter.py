cup_cake = open('CupcakeInvoices.csv')
for line in cup_cake:
    print(line)


cup_cake.seek(0,0)

for line in cup_cake:
    if 'Vanilla' in line:
        print('Vanilla')
    elif 'Chocolate' in line:
        print('Chocolate')
    elif 'Strawberry' in line:
        print('Strawberry')


    line = line.rstrip('\n').split(',')
    print(line)
    cost = []
    value_one = float(line[-1])
    value_two = float(line[-2])
    order_total = value_one * value_two
    cost.append(order_total)
    print(cost)


    total = 0
    for line in cup_cake:
        values = line.split(',')
        total = total + (int(values[3]) * float(values[4]))

    print (f'The total is {total}')

    cup_cake.close()