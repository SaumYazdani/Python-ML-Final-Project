def monthlyprediction():
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.neighbors import LocalOutlierFactor


    # Reading in data, and setting data to index
    data = pd.read_csv("spy monthly")
    data.index = data['Date']
    # redicttime is the number of days we want our model to predict -- set to around half the # our data
    predicttime = 25
    # setting data to only = adj close data
    data = data[["Adj Close"]]
    # inserting predicted_close to be size of predicttime
    data["Predicted_Close"] = data["Adj Close"].shift(-predicttime)
    # creating feature to = data without predicted values, and target to equal data's close values
    feature = np.array(data.drop(["Predicted_Close"], axis=1))[:-predicttime]
    target = np.array(data['Predicted_Close'])[:-predicttime]
    # train test split data
    x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=.15)#trying to allocate more data for training to improve accuracy -Connor
    lof = LocalOutlierFactor()
    lof.fit_predict(x_train)  # remove local outliers - Connor

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

    # setting figure size to = 15x20
    plt.figure(figsize=(15, 20))
    # original data set to = blue and cyan, predicted values set to = orange
    plt.plot(data["Adj Close"], color="blue")
    plt.plot(data3["Adj Close"], color="cyan")
    plt.plot(data3["Predicted Adj Close"], color="orange")
    # setting labels and displaying plot
    plt.xlabel('Date')
    plt.title("Monthly Data: Actual = Blue and Cyan, Predicted = Orange")
    plt.ylabel('Adjusted Close Price (Predicted is')
    plt.show()

