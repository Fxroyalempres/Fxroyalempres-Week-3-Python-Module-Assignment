from discount import
calculate_discount #assuming your function is in a file named discount.py

try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    
    if discount_percent >= 20:
        print(f"The final price after {discount_percent}% discount is: {final_price}")
    else:
        print(f"No discount applied. The price remains: {final_price}")
        
except ValueError as e:
    print(e)