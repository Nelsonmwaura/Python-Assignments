def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount.
    Discount applies only if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# --- Main program ---
# Prompt user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call function
final_price = calculate_discount(price, discount_percent)

# Display result
print(f"The final price is: {final_price:.2f}")
