# Define stock prices (stock name: price per share)
stock_prices = {
    "AAPL": 150.0,
    "GOOGL": 2800.0,
    "MSFT": 300.0,
    "TSLA": 700.0,
    "AMZN": 3300.0
}

# Dictionary to store quantities of each stock
portfolio = {}
total_investment = 0.0

# Get user input
print("Enter the number of shares you own for each stock:")
for stock, price in stock_prices.items():
    quantity = int(input(f"{stock} (${price}): "))
    portfolio[stock] = quantity
    total_investment += quantity * price

# Display the investment summary
print("\nYour Investment Portfolio:")
for stock in portfolio:
    amount = portfolio[stock] * stock_prices[stock]
    print(f"{stock}: {portfolio[stock]} shares × ${stock_prices[stock]} = ${amount:.2f}")

print(f"\nTotal Investment: ${total_investment:.2f}")

# Save to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Your Investment Portfolio:\n")
    for stock in portfolio:
        amount = portfolio[stock] * stock_prices[stock]
        file.write(f"{stock}: {portfolio[stock]} shares × ${stock_prices[stock]} = ${amount:.2f}\n")
    file.write(f"\nTotal Investment: ${total_investment:.2f}\n")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")
