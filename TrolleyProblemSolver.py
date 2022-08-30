import sklearn 
import csvTranslator
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data_set = csvTranslator.load_trolley_short()

X_train, X_test, y_train, y_test = train_test_split(data_set.data, data_set.target, random_state=0)
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(forest.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(forest.score(X_test, y_test)))

keep_going = "y"

print("gender: -1 = male, 0 = female, 1 = other\nage: 1-100\ncriminal: 1 = criminal, 0 = not\nfamily: 1 = has, 0 = doesn't\nrich: 1 = rich, 0 = average, -1 = poor\nimportant: 1 = important job, 0 = unimportant\nspecies: 0 = human, -1 = cat, 1 = dog\ncount = -1 = 2, 0 = 1, 1 = 3\nevil = 1 = evil, 0 = not")

while keep_going == "y":
    sides = np.array([[input("Person 1 gender\n"), input("Person 1 age\n"), input("Person 1 criminal\n"), input("Person 1 family\n"), input("Person 1 rich\n"), 
                     input("Person 1 important\n"), input("Person 1 species\n"), input("Person 1 count\n"), input("Person 1 evil\n"), input("Person 2 gender\n"), 
                     input("Person 2 age\n"), input("Person 2 criminal\n"), input("Person 2 family\n"), input("Person 2 rich\n"), input("Person 2 important\n"), 
                     input("Person 2 species\n"), input("Person 2 count\n"), input("Person 2 evil\n")]])
    
    j = 0
    for i in sides[0]:
        if i == '':
            sides[0][j] = 0
        else: 
            sides[0][j] = int(sides[0][j]) 
        j += 1
    
    print(sides)
    
    prediction = forest.predict(sides)
    
    if prediction == 1:
        print("Side 1 died")
    else:
        print("Side 2 died")
        
    keep_going = input('Enter "y" to try again\n')
        