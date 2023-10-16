def calculate_housing_emi(principal, annual_interest_rate, loan_tenure_years):
    # Convert annual interest rate to monthly and calculate number of installments
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_installments = loan_tenure_years * 12
    
    # Calculate EMI using the formula
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_installments
    emi /= ((1 + monthly_interest_rate) ** total_installments - 1)
    
    return emi

if __name__ == "__main__":
    try:
        principal = float(input("Enter the loan amount (principal) in dollars: $"))
        annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        loan_tenure_years = int(input("Enter the loan tenure in years: "))

        emi = calculate_housing_emi(principal, annual_interest_rate, loan_tenure_years)

        print(f"Your Equated Monthly Installment (EMI) is: ${emi:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numerical values for the loan details.")
