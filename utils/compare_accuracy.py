import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,fbeta_score
import numpy as np 

y_pred = pd.read_csv('batch_prediction.csv').values.astype(int)
print(y_pred)
y_true = pd.read_csv('../utils/merged_final_data_heavy_filtered.csv').values[:,-1].astype(int)
y_true = np.expand_dims(y_true, axis=1)
print(y_true.shape)
print(fbeta_score(y_true, y_pred, average='weighted', beta=0.5))
print(accuracy_score(y_true,y_pred))
print(confusion_matrix(y_true,y_pred))


