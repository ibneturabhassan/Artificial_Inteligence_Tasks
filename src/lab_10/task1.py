import numpy as np
from random import seed
from random import randrange
from csv import reader
from math import sqrt

eps = np.finfo(float).eps  # smallest possible number

# load csv files
def load_csv(filename):
    dataset = list()
    row = 1
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# string to float converter
def str2float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# string to integer converter
def str2int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


# Split a dataset on attribute and attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
    return gini


# Select the best split point
def get_split(dataset, n_features):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    features = list()
    while len(features) < n_features:
        index = randrange(len(dataset[0]) - 1)
        if index not in features:
            features.append(index)
    for index in features:
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}


# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


# child splits for a node or make terminal
def split(node, max_depth, min_size, n_features, depth):
    left, right = node['groups']
    del (node['groups'])
    # no split check
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # max depth check
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left, n_features)
        split(node['left'], max_depth, min_size, n_features, depth + 1)
    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right, n_features)
        split(node['right'], max_depth, min_size, n_features, depth + 1)


# Building decision tree
def build_tree(train, max_depth, min_size, n_features):
    root = get_split(train, n_features)
    split(root, max_depth, min_size, n_features, 1)
    return root


# Making prediction
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


# random subsample from the dataset with replacement
def subsample(dataset, ratio):
    sample = list()
    n_sample = round(len(dataset) * ratio)
    while len(sample) < n_sample:
        index = randrange(len(dataset))
        sample.append(dataset[index])
    return sample


# Make a prediction with a list of bagged trees
def bagging_predict(trees, row):
    predictions = [predict(tree, row) for tree in trees]
    return max(set(predictions), key=predictions.count)


# Random Forest Algorithm
def random_forest(train, test, max_depth, min_size, sample_size, n_trees, n_features):
    trees = list()
    for i in range(n_trees):
        sample = subsample(train, sample_size)
        tree = build_tree(sample, max_depth, min_size, n_features)
        trees.append(tree)
    predictions = [bagging_predict(trees, row) for row in test]
    return (predictions)


# Test the random forest algorithm
seed(2)

# loading the csv files into datasets
training_file = 'TrainingSet.csv'
test_file = 'TestSet1.csv'

training_dataset = load_csv(training_file)
test_dataset = load_csv(test_file)

# removing the headings row
training_dataset.pop(0)
test_dataset.pop(0)

# convert string attributes to integers in training set
for i in range(0, len(training_dataset[0]) - 1):
    str2float(training_dataset, i)

print("Following lookup table indicates what integer represents each class according to my labelling:\n")
# convert class col to int in training set
print(str2int(training_dataset, len(training_dataset[0]) - 1))
# converting str attr to float in test set
for i in range(0, len(test_dataset[0]) - 1):
    str2float(test_dataset, i)


# actual task
max_depth = 10
min_size = 1
sample_size = 1.0
n_features = int(sqrt(len(training_dataset[0]) - 1))

for n_trees in [100, 300, 500]:
    predictions = random_forest(training_dataset, test_dataset, max_depth, min_size, sample_size, n_trees, n_features)
    print(str(n_trees) + ' Trees Predictions: %s' % predictions)