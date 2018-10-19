import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy import stats
#from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import accuracy_score


def knn(X_train, y_train, X_test, k):
   X_dist = pd.DataFrame()
   for i in range(0, len(X_test)):
      for j in range(0, len(X_train)):
         X_dist.at[i,j] = np.linalg.norm(X_test[i] - X_train[j])
   #print X_dist
   #print len(X_dist)
   y_predicted =[]
   for i in range(0,len(X_dist)):
      X_sort=X_dist.sort_values(by=[i], axis=1)
      X_sorted_indices = X_sort.columns.values.tolist()
      #print X_sorted_indices
      knn_X_list = X_sorted_indices[:k]
      #print knn_X_list
      knn_y_list = [y_train[i][0] for i in knn_X_list]
      #print knn_y_list
      out,_ = stats.mode(knn_y_list)
      predicted = out.ravel()[0]
      y_predicted.append(predicted)
   return y_predicted
       
         
# Generate dummy data
X = np.random.randint(50, size=(100, 10))
Y = np.random.randint(2, size=(100, 1))
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
#print X_train
#print y_train

#print X_train[0][0]
#x_test = np.random.randint(50, size=(1000, 2))
#y_test = np.random.randint(2, size=(100, 1))
#print X_test[0]

for k in range(1,10):
   y_predicted = knn(X_train, y_train, X_test, k)
   #print "y_predicted..."
   #print y_predicted

   #print "y_test..."
   #print y_test

   print "k: %d Accuracy : %f " % (k, accuracy_score(y_test, y_predicted))

