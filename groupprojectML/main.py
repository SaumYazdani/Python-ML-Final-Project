#importing all python files (functions)
import weekly
import monthly
import annual

#displaying options and validating user input
print('(1) Weekly Prediction')
print('(2) Monthly Prediction')
print('(3) Yearly Prediction')
ui = input()
while ui != '1' or ui != '2' or ui != '3':
    if ui == '1' or ui == '2' or ui == '3':
        break
    ui = input('Please enter one of the above options!')
#displaying correct choice
if ui == '1':
    weekly.weeklyprediction()
if ui == '2':
    monthly.monthlyprediction()
if ui == '3':
    annual.annualprediction()