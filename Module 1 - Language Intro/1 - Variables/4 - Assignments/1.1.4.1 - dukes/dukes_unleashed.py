"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
Total_InState = 30792 #dollar amount for Instate tuition
Total_OutState = 47882 #dollar amount for Outstate tuition
Investment = 5/100 #percent of return on investment
in_state_gift = Total_InState/Investment
out_state_gift = Total_OutState/Investment

donation = in_state_gift + out_state_gift
print(donation)