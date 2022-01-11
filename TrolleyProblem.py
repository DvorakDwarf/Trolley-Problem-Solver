import sklearn 
import csvTranslator

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data_set = csvTranslator.load_trolley_short()

X_train, X_test, y_train, y_test = train_test_split(data_set.data, data_set.target, random_state=0)
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(forest.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(forest.score(X_test, y_test)))
