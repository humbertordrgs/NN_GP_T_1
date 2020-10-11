import numpy as np
from sklearn.metrics import confusion_matrix

def calc_metrics(y_test, y_predict, current_cost):
    y_predict = np.argmax(y_predict,axis=1)
    y_test = np.argmax(y_test,axis=1)
    current_acc = sum(y_test == y_predict) / float(len(y_test)) * 100
    print(f" Accuracy: {current_acc:.2f}%\n Avg cost: {np.mean(current_cost):.5f}\n")
    print(f" Confusion Matrix:\n {confusion_matrix(y_test,y_predict)}")
    return current_acc

def metric_summary(historic_acc, historic_cost):
    print(f"Summary: \n\navg_acc: {np.mean(historic_acc):.2f}% std_acc: {np.std(historic_acc):.2f}% median_acc: {np.median(historic_acc):.2f}%")
    print(f"avg_cost: {np.mean(historic_cost):.5f} std_cost: {np.std(historic_cost):.5f} median_cost: {np.median(historic_cost):.5f}")