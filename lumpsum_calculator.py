def calculate_lump_sum_investment(initial_investment, annual_interest_rate, years):
    # Convert the annual interest rate to a decimal and calculate the future value
    annual_interest_rate_decimal = annual_interest_rate / 100
    future_value = initial_investment * (1 + annual_interest_rate_decimal) ** years
    return future_value

if __name__ == "__main__":
    try:
        initial_investment = float(input("Enter the initial investment amount: $"))
        annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        years = int(input("Enter the number of years for the investment: "))

        future_value = calculate_lump_sum_investment(initial_investment, annual_interest_rate, years)

        print(f"Future value after {years} years: ${future_value:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numerical values for the investment details.")
