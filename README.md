# financial_calc
To do important financial calculations

## SIP calculation
FV = P * [(1 + r)^n - 1] / r

Where:

FV is the future value of the investment.
P is the periodic payment (monthly SIP amount).
r is the monthly return rate (annual return rate divided by 12 months).
n is the total number of periods (number of years times 12 months).

For example, if the SIP amount is ₹3,000,
the annual return rate is 14%, and the investment period is 15 years. 
We'll first convert the annual return rate to a monthly rate and then calculate the future value:

Monthly SIP Amount (P): ₹3,000
Annual Return Rate (r): 14% or 0.14 (as a decimal)
Monthly Return Rate (r_m): 0.14 / 12 = 0.01167 (approximately)
Total Number of Periods (n): 15 years * 12 months/year = 180 months
FV = 3,000 * [(1 + 0.01167)^180 - 1] / 0.01167
FV ≈ ₹1,270,704.54

## Amoritized schedule of EMI


