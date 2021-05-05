#importing all python files (functions)
import weekly
import monthly
import annual
import replay
import requests
from datetime import timedelta
from datetime import date

#getting todays date
todaysdate = date.today()

#displaying option, and taking user input
print('(1) Weekly Prediction')
print('(2) Monthly Prediction')
print('(3) Yearly Prediction')
ui = input()

#-==-=-=- api key = 6091ee932105a3.73891944 =--=-=- only 20 uses per day -=-=-= replace api_token with api key in url2 to use -==-=-=-=

#validating user input
while ui != '1' or ui != '2' or ui != '3':
    if ui == '1' or ui == '2' or ui == '3':
        break
    ui = input('Please enter one of the above options!')

#checking which choice user entered to generate the url - url takes todays date minus the 12 (weekly), 30(monthly), 365(annual)
#part of the url is built and stored - api token is necessary to run all tickers but default key provided can access MCD ticker
if ui =='1':
       enddate = todaysdate - timedelta(days=12)
       enddate = enddate.strftime("%Y-%m-%d")
       td = date.today().strftime("%Y-%m-%d")
       url2 = '.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&period=d&from='+enddate+'&to='+ td
if ui == '2':
    enddate = todaysdate - timedelta(days=30)
    enddate = enddate.strftime("%Y-%m-%d")
    td = date.today().strftime("%Y-%m-%d")
    url2 = '.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&period=d&from=' + enddate + '&to=' + td
if ui == '3':
    enddate = todaysdate - timedelta(days=360)
    enddate = enddate.strftime("%Y-%m-%d")
    td = date.today().strftime("%Y-%m-%d")
    url2 = '.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&period=d&from=' + enddate + '&to=' + td

#getting the user's desired stock ticker to predict data on -- must enter MCD unless api token is entered above
stocktick = input("Please enter the stock ticker you would like to predict on. Example: SPY\n").upper()

#creating the rest of the url and sending a request to get the data
url = 'https://eodhistoricaldata.com/api/eod/'+stocktick
url3 = url+url2
req = requests.get(url3, allow_redirects=True)

#once the data is obtained it is stored in the stockdata file
data = open('stockdata','wb')
data.write(req.content)
data.close()

#displaying correct choice
try:
    if ui == '1':
        #each option allows the user to click on the get request url formed above to see the raw data used for prediction
        #then each chpoice calls the appropriate function passing the stock ticker enetered above for use inside the function
        print("Download the requested stock data: " + url3 + "\n")
        weekly.weeklyprediction(stocktick)
    if ui == '2':
        print("Download the requested stock data: " + url3 + "\n")
        monthly.monthlyprediction(stocktick)
    if ui == '3':
        print("Download the requested stock data: " + url3 + "\n")
        annual.annualprediction(stocktick)

##except statement will trigger if incorrect ticker is entered --- likely the case if api key above is not replaced
except:
    print("Invalid ticker entered!\nRestarting the program!\n")
    #upon error, program essentially restarts
    replay.replay('Y')
