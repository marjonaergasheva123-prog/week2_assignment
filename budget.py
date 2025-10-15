#Name
#monthly net income
#Fixed expenses: Rent, utilities, internet, phone bill
#Variable expenses: Groceries, transportation, entertainment
#Current savings amount
#partment down payment goal
#Months until desired purchase
name= input ('Enter your name:')
monthly_net_income= int(input('Enter your monthly net income'))
variable_expenses=int(input('Enter your variable expenses'))
current_savings_amount= int(input('Enter your current savings amount'))
partment_down_payment_goal=int(input('Enter your partment down payment goal:'))
months_until_desired_purchase= int(input('Enter your moths until desired purchase'))
fixed_expenses= int(input('Enter your fixed expenses'))
#Total monthly expenses (sum of all categories)
total_monthly_expenses=(f"{variable_expenses} +{fixed_expenses}")
# savings (income - expenses)
Monthly_savings=(f"{monthly_net_income}-{total_monthly_expenses}")
# rate percentage (savings / income * 100)
rate_percentage=(f"{Monthly_savings}/{monthly_net_income}*100")
#projected savings after target months (monthly_savings * months)
Projected_savings_after_target_months= (f"{Monthly_savings}*{months_until_desired_purchase}")
#Total projected amount (current_savings + projected_savings)
Total_projected_amount=(f"{current_savings_amount}+{Projected_savings_after_target_months}")
# monthly savings needed to reach goal (total_needed / months)
Monthly_savings_needed_to_reach_goal=(f'{Total_projected_amount}/{months_until_desired_purchase}')
Additional monthly savings needed (can be negative if already sufficient)
Shortfall or surplus (total_projected - goal, negative = shortfall, positive = surplus