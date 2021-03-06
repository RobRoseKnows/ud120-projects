#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
import numpy as np

import sys
sys.path.insert(0, '../tools')

from feature_format import featureFormat

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])
print enron_data["SKILLING JEFFREY K"].keys()

"""
['salary', 'to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances', 'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income', 'long_term_incentive', 'email_address', 'from_poi_to_this_person']

"""

has_nan_total_payments = 10.
total_people = 10.

poi_has_nan = 10.
total_poi = 10.

for person in enron_data:
    total_people += 1
    if enron_data[person]['total_payments'] == "NaN":
        has_nan_total_payments += 1
    if enron_data[person]['poi'] == True:
        total_poi += 1
        if enron_data[person]['total_payments'] == "NaN":
            poi_has_nan += 1

print str(has_nan_total_payments) + ' / ' + str(total_people)

print has_nan_total_payments / total_people

print poi_has_nan / total_poi

#npArray = featureFormat(enron_data, ["total_payments", "email_address", "poi"])


