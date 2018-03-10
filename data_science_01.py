from sklearn import tree

#[height, weight, shoe size]
x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37],
    [171, 75, 42], [195, 79, 45]]

y = ['male', 'male', 'female', 'female', 'female', 'male', 'female',
'male', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
prediction = clf.predict([[160, 45, 34]])
print(prediction)
