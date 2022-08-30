import numpy as np
import csv
from sklearn.utils import Bunch

def load_trolley_short():
    with open(r'TrolleyData.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        feature_names = next(data_reader)[:-1]
        data = []
        target = []
        for row in data_reader:
            features = row[:-1]
            label = row[-1]
            data.append([float(num) for num in features])
            target.append(int(label))
        
        data = np.array(data)
        target = np.array(target)
    return Bunch(data=data, target=target, feature_names=feature_names)