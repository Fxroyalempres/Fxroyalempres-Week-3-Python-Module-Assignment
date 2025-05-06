#Calculate_discount(price, discount_percent)
#This function takes a price and a discount percentage as input and returns the discounted price.
def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price given the original price and discount percentage.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.

    Returns:
    float: The discounted price.
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount percentage must be non-negative.")
    
    if discount_percent >= 20:
        discount_amount =
        (discount_percent / 100) * price
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price