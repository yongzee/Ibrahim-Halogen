from django.shortcuts import render
import pickle
import numpy as np

# Create your views here.s
def HomePage(request):
    return render(request, 'home.html')


def resultpredict(request):
    cls = pickle.load(open('fraud.pkl', 'rb'))

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
    print = (ans)

    
    return render(request, 'result.html', {'ans': ans})