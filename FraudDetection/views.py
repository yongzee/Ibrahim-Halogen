from django.shortcuts import render
import joblib
import numpy as np

# Create your views here.s
def HomePage(request):
    return render(request, 'home.html')


def resultpredict(request):
    cls = joblib.load('fraud_model.sav')

    lis = []
    lis.append(request.GET['step'])
    lis.append(request.GET['type'])
    lis.append(request.GET['amount'])
    lis.append(request.GET['oldbalanceOrig'])
    lis.append(request.GET['newbalanceOrig'])
    lis.append(request.GET['oldbalanceDest'])
    lis.append(request.GET['newbalanceDest'])
    lis.append(request.GET['isFlaggedFraud'])
    lis.append(request.GET['errorBalanceOrig'])
    lis.append(request.GET['errorBalanceDest'])


    data_array = np.array(lis, dtype=object)
    arr = data_array.reshape(1, -1)
    ans = cls.predict(arr)

    final_ans = ''
    if ans == 1:
        final_ans = 'Fraud'
    elif ans == 0:
        final_ans = 'Not Fraud'
    else:
        final_ans = 'Error'
    return render(request, 'result.html', {'ans': final_ans})