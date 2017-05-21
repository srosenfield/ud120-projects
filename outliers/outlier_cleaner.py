#!/usr/bin/python

# ####steve testing here
# import random
# import numpy
# import matplotlib.pyplot as plt
# import pickle
#
# ages = pickle.load( open("practice_outliers_ages.pkl", "r") )
# net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "r") )
# ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
# net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
# from sklearn.cross_validation import train_test_split
# ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)
# from sklearn.linear_model import LinearRegression
# reg = LinearRegression()
# reg.fit(ages_train, net_worths_train)
# predictions = reg.predict(ages_train)
#
# #####steve testing done

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    ### your code goes here
    #first create a list of the tuples with all data
    for x, y, z in zip(predictions, ages, net_worths):
        error = abs(x - z)
        cleaned_data.append((y, z, error))

    #now remove the 10% of data with the largest errors
    from operator import itemgetter
    import math

    ten_percent_of_data = int(math.ceil(len(cleaned_data)*.1))

    for i in range(ten_percent_of_data):
        #item getter gets the third item in the tuple corresponding to error
        cleaned_data.remove(max(cleaned_data,key=itemgetter(2)))
        #print("max error in cleaned_data is ", max(cleaned_data,key=itemgetter(2)))


    return cleaned_data

# #####steve testing below
# clean_data = outlierCleaner(predictions, ages_train, net_worths_train)
# print(len(clean_data))
