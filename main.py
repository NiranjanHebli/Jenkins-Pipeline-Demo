#!/usr/bin/python3

print("Content-type: text/html")
print()

import cgi

form = cgi.FieldStorage()
hours = form.getvalue("q")
# print(hours)
# print(hours)
# print(str(type(hours)))
import pandas
import numpy
dataset=pandas.read_csv("Student.csv")
from sklearn.linear_model import LinearRegression
model=LinearRegression()

X=dataset["Hours"][:4]
Y=dataset["Score"][:4]

X= numpy.array(X)
Y=numpy.array(Y)

X=X.reshape(4,1)
Y=Y.reshape(4,1)

mlmodel=model.fit(X,Y)

# print("Hello there!")


# value=int(input("Enter your hours of study:"))
value = int(hours)
output=model.predict([[value]])
print(str(int(output[0,0]))+ "marks")