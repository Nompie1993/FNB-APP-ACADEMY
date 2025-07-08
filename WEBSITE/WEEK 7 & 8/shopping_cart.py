foods = []
prices = []
total = 0

while True:
    food = input("Enter food item (or 'done' to finish): ")
    if food.lower == 'done':
        break
    else:
        price= float(input(f"Enter price for {food}: R "))
    foods.append(food)
    
    price = float(input("enter a food to buy or press q to quit: "))
    prices.append(price)
    
    print("--------Your Shopping Cart--------")
    for food in foods:
        print(f"{food} - R {price:.2f}")    
    total += price
    