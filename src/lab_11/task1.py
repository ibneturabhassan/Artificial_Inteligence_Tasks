# using the standard implementation and storing comparsion results
for k in [3, 5, 7]:
    # making classifier object
    knn = KNeighborsClassifier(n_neighbors=k)
    # fitting with training data
    knn.fit(trainDF.drop(columns=['plant'], errors='ignore'), trainDF['plant'])
    # classifying test set
    start_time = time.clock()
    cls = knn.predict(testDF.drop(columns=['plant'], errors='ignore'))
    print("\n--- %s seconds --- \n" % round((time.clock() - start_time), 5))

    if k == 3:
        print("3-nn accuracy vs standard implementation :",
              str(metrics.accuracy_score(test3['plant'], cls) * 100) + "%")
    elif k == 5:
        print("5-nn accuracy vs standard implementation :",
              str(metrics.accuracy_score(test5['plant'], cls) * 100) + "%")
    else:
        print("7-nn accuracy vs standard implementation :",
              str(metrics.accuracy_score(test7['plant'], cls) * 100) + "%")
