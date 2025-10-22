

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 330
}


portfolio = {}
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stock holdings (type 'done' to finish):")

while True:
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("Invalid stock symbol! Try again.\n")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("Invalid input! Quantity must be a number.\n")
        continue
    
    
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity


total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print("\nTotal Investment Value: $", total_value)


save_choice = input("\nDo you want to save the result to a file? (y/n): ").lower()

if save_choice == "y":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"Portfolio saved to {filename}")
