# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:48:08 2016

"""

from matplotlib import pyplot as plt

# We load the data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]

for t, marker, c in zip(range(3), ">ox", "rgb"):
 plt.scatter(features[target == t, 0],
            features[target == t, 1],
            marker = marker,
            c=c)


plength = features[:,2]
is_setosa = (labels == 'setosa')
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

print ('maximum of setosa:{0}'.format(max_setosa))
print ('minimum of non-setosa:{0}'.format(min_non_setosa))

features = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica')

best_acc = -1.0
best_fi = -1.0
best_t = -1.0

#print (features.shape[1])

for fi in range(features.shape[1]):  # shape は array （配列）の次元を返す
    threash = features[:,fi].copy()
    threash.sort()
    
    for t in threash:
        pred = (features[:,fi] > t)
        acc =  (labels[pred] == 'virginica').mean()
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t
            
        
#print (threash)
     
