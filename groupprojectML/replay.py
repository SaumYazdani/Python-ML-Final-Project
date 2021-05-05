def replay(goagain):
    #checking to see if the uer wants to rerun the program or not - if so rerun the original main
    if goagain == 'N':
        print ("\n--- Thank you for using the program!---")
    else:
        # importing all python files (functions)
        import weekly
        import monthly
        import annual
        import requests
        from datetime import timedelta
        from datetime import date
        from datetime import datetime
        todaysdate = date.today()

        #displaying options and validating user input
        print('(1) Weekly Prediction')
        print('(2) Monthly Prediction')
        print('(3) Yearly Prediction')
        ui = input()
        ##-==-=-=- api key = 6091ee932105a3.73891944 =--=-=- only 20 uses per day
        while ui != '1' or ui != '2' or ui != '3':
            if ui == '1' or ui == '2' or ui == '3':
                break
            ui = input('Please enter one of the above options!')
        if ui == '1':
            enddate = todaysdate - timedelta(days=12)
            enddate = enddate.strftime("%Y-%m-%d")
            td = date.today().strftime("%Y-%m-%d")
            url2 = '.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&period=d&from=' + enddate + '&to=' + td
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

        stocktick = input("Please enter the stock ticker you would like to predict on. Example: SPY\n").upper()
        url = 'https://eodhistoricaldata.com/api/eod/' + stocktick
        url3 = url + url2
        req = requests.get(url3, allow_redirects=True)
        data = open('stockdata', 'wb')
        data.write(req.content)
        data.close()
        # displaying correct choice
        try:
            if ui == '1':
                weekly.weeklyprediction(stocktick)
                print("Download the requested stock data: " + url3 + "\n")
            if ui == '2':
                monthly.monthlyprediction(stocktick)
                print("Download the requested stock data: " + url3 + "\n")
            if ui == '3':
                annual.annualprediction(stocktick)
                print("Download the requested stock data: " + url3 + "\n")
        except:
            print("Invalid ticker entered!\nRestarting the program!\n")
            replay('Y')