Name= input('Enter your name')
Monthly_net_income= int(input('Enter your Monthly net income'))
Fixed_expenses= int(input('Enter your Fixed expenses '))
Variable_expenses= int(input('Enter your Variable expenses '))
Current_savings= int(input('Enter your Current savings amount'))
down_payment_goal= int(input('Enter your Apartment down payment goal'))
Months= int(input('Enter your Months until desired purchase'))

monthly_expenses= Fixed_expenses+Variable_expenses
Monthly_savings=Monthly_net_income-monthly_expenses
Saving_rate=Monthly_savings/Monthly_net_income*100
Projected_savings=Monthly_savings*Months
Total_projected=Current_savings+Projected_savings
#Monthly savings needed to reach goal (total_needed / months)
Monthly_savings_needed= Total_projected / Months
#additional monthly savings needed (can be negative if already sufficient)
Addiional_monthly_savings_needed= Monthly_savings_needed - Monthly_savings
#Shortfall or surplus (total_projected - goal, negative = shortfall, positive = surplus)
shortfall=Total_projected- down_payment_goal
surplus= Total_projected -down_payment_goal
                                  

Critical_warning =  bool(Monthly_savings>= Monthly_net_income)
Below_recommended =bool(Saving_rate< 20)
Good_position=bool(Saving_rate>= 20 and Saving_rate < 30)
Excellent_position=bool(Saving_rate >= 30)
Goal_achievable=bool(Total_projected>= down_payment_goal)

#ncome: Monthly net income
#Expense breakdown (all categories itemized)
#Total fixed expenses
#Total variable expenses
#Total monthly expenses
#Savings analysis:
#Monthly savings amount
#
#Current savings
#Projected savings in X months
#Total projected
#Goal analysis:
#Target amount
#Monthly savings needed for goal
#Additional monthly savings needed (show actual number, can be negative)
#All financial health indicators (True/False for each)
#Goal achievability status (True/False)
#Numeric gap: shortfall or surplus amount

print(f'Young professional budget summary for {Name}')
print(f"Income: {Monthly_net_income}")
print(f"Expense breakdown : ")
print(f'Fixed expenses: {Fixed_expenses}')
print(f'Variable expenses: { Variable_expenses}')
print(f'Total monthly expenses : {monthly_expenses}')
print()
print(f'Savings analysis:')
print(f'Monthly savings amount: {Monthly_savings}')
print(f'Savings rate percentage: {Saving_rate}')
print(f'Current savings: {Current_savings}')
print(f'Projected savings in x months: {Projected_savings}')
print(f'Total projected amount: {Total_projected}')
print()
print(f'Goal analysis: ')
print(f' Target amount: {down_payment_goal}')
print(f'Monthly savings needed for goal: {Monthly_savings_needed}')
print(f'Additional monthly savings needed: {Addiional_monthly_savings_needed}')
print(f'All financial health indicators:')
print(f'Critical warning: {Critical_warning}')
print(f'Below recommended: {Below_recommended}')
print(f'Good position: {Good_position}')
print(f'Excellent position: {Excellent_position}')
print(f'Goal achievable: {Goal_achievable}')
print()
print(f'Numeric gap:')
print(f'Shorfall: {shortfall} {Total_projected- down_payment_goal < 0}' )
print(f'Surplus: {surplus} {Total_projected- down_payment_goal > 0} ')
