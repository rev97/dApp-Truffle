
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

from util import create_dataset
from util import data_preprocess

plt.style.use('ggplot')

class MLPmodel:
    def __init__(self, df):
        self.df = df

    def split_data(self,x_col, target,test_size):
        
        X = self.df[x_col]
        y = self.df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
        return X_train, X_test, y_train, y_test

    def model(self,X_train, X_test, y_train, y_test):
        model = MLPClassifier()
        model.fit(X_train, y_train)
        print(model)

        expected_y  = y_test
        predicted_y = model.predict(X_test)
        accuracy_score = model.score(X_test, predicted_y, sample_weight=None)
        X_test['expected_y'] = expected_y
        X_test['predicted_y'] = predicted_y

        

        print(metrics.classification_report(expected_y, predicted_y))
        print(metrics.confusion_matrix(expected_y, predicted_y))

        return X_test, accuracy_score

if __name__ == '__main__':
    df = create_dataset('/Users/revanthgottuparthy/Desktop/ABC/MLPclassifier/input_data.csv')
    df = data_preprocess(df)
    mlp_obj = MLPmodel(df)
    x_col = ['zone_R','zone_C','zone_I','PCN Number']
    target = 'Violation'
    test_size = 0.30
    X_train, X_test, y_train, y_test = mlp_obj.split_data(x_col, target, test_size)
    res, accuracy_score = mlp_obj.model(X_train, X_test, y_train, y_test)
    print(accuracy_score)
    res.to_csv('/Users/revanthgottuparthy/Desktop/ABC/MLPclassifier/output_data.csv')
