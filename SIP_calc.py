def calculate_sip_future_value(sip_amount, annual_return_rate, investment_period):
    # Convert annual return rate to monthly
    monthly_return_rate = (1 + annual_return_rate) ** (1/12) - 1
    
    # Calculate the future value of SIP
    future_value = 0
    for month in range(1, investment_period * 12 + 1):
        future_value += sip_amount
        future_value *= (1 + monthly_return_rate)
    
    return future_value

if __name__ == "__main__":
    sip_amount = float(input("Enter the monthly SIP amount: "))
    annual_return_rate = float(input("Enter the expected annual return rate (as a percentage): ")) / 100
    investment_period = int(input("Enter the investment period in years: "))
    
    future_value = calculate_sip_future_value(sip_amount, annual_return_rate, investment_period)
    
    print(f"Future Value of SIP {sip_amount} after {investment_period} years at growth {annual_return_rate}% is ₹{future_value:.2f}")
