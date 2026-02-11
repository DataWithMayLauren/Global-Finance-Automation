def currency_converter(amount_usd, exchange_rate=56.20):
    """Converts USD to local currency (Default: PHP)"""
    return amount_usd * exchange_rate

def budget_forecaster(current_savings, monthly_income, monthly_expenses, months=6):
    """Predicts future savings based on monthly net profit."""
    net_monthly_profit = monthly_income - monthly_expenses
    future_total = current_savings + (net_monthly_profit * months)
    return future_total

if __name__ == "__main__":
    # Example Scenario
    payment_usd = 500
    php_total = currency_converter(payment_usd)
    
    current_bal = 1000
    income = 1500
    expenses = 900
    forecast = budget_forecaster(current_bal, income, expenses)

    print("--- DataWithMayLauren Finance Toolkit ---")
    print(f"1. Currency Check: ${payment_usd} USD = ₱{php_total:,.2f} PHP")
    print(f"2. 6-Month Forecast: Estimated balance will be ${forecast:,.2f}")
    print("-----------------------------------------")
