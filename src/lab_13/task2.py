import pandas as pd
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier

print('Loading training set')
df = pd.read_excel('TestSet-withLabels.xlsx')
print(df)
labels = df.columns

# data preprocessing
le = preprocessing.LabelEncoder()
le.fit(df['plant'])
df['plant'] = le.transform(df['plant'])
print()
print('Preprocessed data:')
print(df)

test_sample = pd.read_excel('TestSet1.xlsx')
test = test_sample[['leaf.length', 'leaf.width', 'flower.length', 'flower.width']]
print()
print('Test samples to be classified:')
print(test)

# multi-class classification through MLP
clf = MLPClassifier(solver = 'lbfgs', alpha = 1e-5, hidden_layer_sizes=(5, 6), random_state=1)
clf.fit(df[['leaf.length', 'leaf.width', 'flower.length', 'flower.width']], df['plant'])

results = clf.predict(test)
print(results)

res_df = test
res_df['plant'] = le.inverse_transform(results)

print()
print('MLP classified test sample:')
print(res_df)

filename = 'MLP Classifier Results.xlsx'
res_df.to_excel(filename)