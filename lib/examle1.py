import pandas
import numpy
from sklearn.cross_validation import train_test_split
column_names = ["Sample code number", "Clump Thickness", "Uniformity of of Cell Size",
    "Uniformity of Cell Shape", "Marginal Adhesion", "Single Epithelial Cell Size", 
    "Bare Nuclei", "Bland Chromatin", "Normal Nucleoli", "Mitoses", "Class"]
data = pandas.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
    names=column_names)
data = data.replace(to_replace='? ', value=numpy.nan)
data = data.dropna(how='any') 
print data.shape

x_train, x_test, y_train, y_test=train_test_split(data[column_names[1:10]], data[column_names[10]], 
    test_size=0.25, random_state=33)

print y_train.value_counts()
print y_test.value_counts()