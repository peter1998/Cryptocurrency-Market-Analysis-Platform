from sklearn import model_selection
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR


def compare_models(X_train, y_train):
    # prepare configuration for cross validation test harness
    seed = 7

    # prepare models
    models = []
    models.append(('LR', LinearRegression()))
    models.append(('DTR', DecisionTreeRegressor(random_state=seed)))
    models.append(('KNR', KNeighborsRegressor()))
    models.append(('SVR', SVR()))

    # evaluate each model in turn
    results = []
    names = []
    scoring = 'neg_mean_squared_error'
    for name, model in models:
        kfold = model_selection.KFold(
            n_splits=10, random_state=seed, shuffle=True)
        cv_results = model_selection.cross_val_score(
            model, X_train, y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)

    # boxplot algorithm comparison
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()


def train_and_predict(X_train, y_train, X_test):
    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    return predictions
