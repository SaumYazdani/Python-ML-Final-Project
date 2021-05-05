def weeklyprediction(stocktick):
    #importing libraries and replay function
    import replay
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.neighbors import LocalOutlierFactor

    #Reading in data, and setting data to index
    data = pd.read_csv("stockdata")
    data=data.dropna()
    data.index = data['Date']
    # predicttime is the number of days we want our model to predict -- set to 1/3the # our data
    predicttime = 4
    #setting data to only = adj close data
    data = data[["Adjusted_close"]]
    #inserting predicted_close to be size of predicttime
    data["Predicted_Close"] = data["Adjusted_close"].shift(-predicttime)
    #creating feature to = data without predicted values, and target to equal data's close values
    feature = np.array(data.drop(["Predicted_Close"], axis = 1))[:-predicttime]
    target = np.array(data['Predicted_Close'])[:-predicttime]
    #train test split data
    x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size = .4)
    # remove local outliers
    lof = LocalOutlierFactor()
    lof.fit_predict(x_train)

    # apply linear regression on our fitted data
    reg = LinearRegression().fit(x_train, y_train)
    # calculating r^2 accuracy score
    print("R^2 is: ", reg.score(x_test, y_test))
    # setting data 2 to equal data values w/o predicted values - also removing the number of predicttime values
    data2 = data.drop(["Predicted_Close"], axis=1)[:-predicttime]
    # setting data2 = to tail length of predicttime
    data2 = data2.tail(predicttime)
    # setting data 2 to = np array
    data2 = np.array(data2)
    # using linear regression to predict values of data2 --- setting = to regprediction variable
    regprediction = reg.predict(data2)
    # data 3 is set = to all ddata values
    data3 = data[feature.shape[0]:]
    # data 3 adding 'Predicted Adj Close' column - these values are set = to linear regression prediction values -> regprediction vals
    data3['Predicted Adj Close'] = regprediction

    #outputting predicted values to a csv that is respective to the stock ticker and the time duration requested
    data3["Predicted Adj Close"].to_csv(stocktick + "_predicted_weekly.csv")

    # setting figure size to = 15x20
    plt.figure(figsize=(15, 20))
    # original data set to = blue and cyan, predicted values set to = orange
    #rotating dates
    degrees = 90
    plt.xticks(rotation=degrees)
    plt.plot(data["Adjusted_close"], color="blue")
    plt.plot(data3["Adjusted_close"], color="cyan")
    plt.plot(data3["Predicted Adj Close"], color="orange")
    # setting labels and displaying plot
    plt.xlabel ('Date')
    # graph title set to stock ticker and time duration and details
    plt.title(stocktick + " Weekly Data: Actual = Blue and Cyan, Predicted = Orange")
    plt.ylabel ('Adjusted Close Price')
    plt.show()

    #rerun the program error logic and function call
    goagain = input ("Would you like to run again? y/n").upper()
    while goagain != 'Y' or goagain!= 'N':
        if goagain == 'Y' or goagain == 'N':
            break
        goagain = input ("Please enter y to run again, or n to exit").upper()
    replay.replay(goagain)


