from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# ML
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neural_network import MLPClassifier

# DB
import sqlite3
from .models import Dataset
from .models import Attribute
from .models import Content


### this variables can be changed
# dataset model storage path (pickle)
pickle_path = 'data_models/'

# different arguments templates storage path
num_args = 'num_args/'


### Import CSV
# main page
def index(request):
    return render(request, 'index.html')

# selecting the name of the imported dataset
def import_dataset(request):
    return render(request, 'import_dataset.html')

def import_csv(request):
    dataset_name = request.GET.get('dataset_name')
    model_name = request.GET.get('model_name')
    con = sqlite3.connect("db.sqlite3")
    
    items = Dataset.objects.values_list()
    items_values = []
    for f in items.values():
        items_values.append(f['name'])
    if dataset_name in items_values:
        return render(request, 'import_csv_error.html')

    if request.method == 'POST':
        new_csv = request.FILES['importData']
        df = pd.read_csv(new_csv)
        dfcolumns = list(df.columns)
        z = Dataset(name=dataset_name)
        z.save()

        for i in range(len(dfcolumns)):
            a = Attribute(id_dataset=z, name=dfcolumns[i])
            a.save()

        if len(dfcolumns) == 3:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2])
                d.save()

        if len(dfcolumns) == 4:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3])
                d.save()

        if len(dfcolumns) == 5:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4])
                d.save()

        if len(dfcolumns) == 6:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5])
                d.save()

        if len(dfcolumns) == 7:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6])
                d.save()
        
        if len(dfcolumns) == 8:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6],
                    a7=df.values[row][7])
                d.save()

        if len(dfcolumns) == 9:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6],
                    a7=df.values[row][7],
                    a8=df.values[row][8])
                d.save()

        if len(dfcolumns) == 10:
            for row in range(len(df.values)):
                d = Content(id_dataset=z, 
                    c=df.values[row][0],
                    a1=df.values[row][1],
                    a2=df.values[row][2],
                    a3=df.values[row][3],
                    a4=df.values[row][4],
                    a5=df.values[row][5],
                    a6=df.values[row][6],
                    a7=df.values[row][7],
                    a8=df.values[row][8],
                    a9=df.values[row][9])
                d.save()

        col_names = []
        for (columnName, columnData) in df.iteritems():
            col_names.append(columnName)

        col_namesX = col_names[1:]
        col_namesY = col_names[0]
        X = df[col_namesX]
        y = df[col_namesY]
        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

        if model_name == 'svm':
            model = SVC(gamma='auto')
        elif model_name == 'knn':
            model = KNeighborsClassifier(n_neighbors=3)
        elif model_name == 'nb':
            model = GaussianNB()
        elif model_name == 'tree':
            model = tree.DecisionTreeClassifier()
        elif model_name == 'nn':
            model = MLPClassifier()
        else:
            model = SVC(gamma='auto')

        model.fit(X_train, Y_train)
        pickle_name = pickle_path+ str(dataset_name) + '_model.pickle'
        pd.to_pickle(model,pickle_name)

        con.close()
    return render(request, 'import_csv.html')



### Datasets
# list of available datasets
def datasets(request):
    x = Dataset.objects.all()
    lst = []
    for i in x:
        lst.append(i)
    data = {"dataset1": lst}
    return render(request, 'datasets.html', {'data':data})


def approval(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name

    model_name = int(str(model_name).split('.')[0])
    attributes = Attribute.objects.filter(id_dataset=model_name)
    lst1 = []
    for i in attributes[1:]:
        lst1.append(i)

    lst1_len = len(lst1)
    name = Dataset.objects.filter(id_dataset=model_name).first()
    name = str(name).split('. ')[1]

    if lst1_len == 2:
        link = "/args2/"
    elif lst1_len == 3:
        link = "/args3/"
    elif lst1_len == 4:
        link = "/args4/"
    elif lst1_len == 5:
        link = "/args5/"
    elif lst1_len == 6:
        link = "/args6/"
    elif lst1_len == 7:
        link = "/args7/"
    elif lst1_len == 8:
        link = "/args8/"
    elif lst1_len == 9:
        link = "/args9/"
    data = {"name": name, "lst1_len": lst1_len, "link": link}
    return render(request, 'approval.html', {'data':data})
    

def args2(request):
    #?model_name=
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1]}
    return render(request, num_args+'args2.html',{'data':data})

def args2_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path+model_name+'_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2},safe=False)


def args3(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2]}
    return render(request, num_args+'args3.html',{'data':data})

def args3_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path+model_name+'_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2, a3]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3},safe=False)


def args4(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3]}
    return render(request, num_args+'args4.html',{'data':data})

def args4_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path + model_name + '_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2, a3, a4]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4},safe=False)


def args5(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4]}
    return render(request, num_args+'args5.html',{'data':data})

def args5_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path+model_name+'_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2, a3, a4, a5]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5},safe=False)


def args6(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5]}
    return render(request, num_args+'args6.html',{'data':data})

def args6_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path+model_name+'_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2, a3, a4, a5, a6]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6},safe=False)

def args7(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5],"a7":args_lst[6]}
    return render(request, num_args+'args7.html',{'data':data})

def args7_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path+model_name+'_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))
        a7 = float(request.POST.get('a7'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2, a3, a4, a5, a6, a7]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6,'a7':a7},safe=False)


def args8(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5],"a7":args_lst[6],"a8":args_lst[7]}
    return render(request, num_args+'args8.html',{'data':data})

def args8_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path+model_name+'_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))
        a7 = float(request.POST.get('a7'))
        a8 = float(request.POST.get('a8'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2, a3, a4, a5, a6, a7, a8]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6,'a7':a7,'a8':a8},safe=False)


def args9(request):
    model_name = request.GET.get('model_name')
    request.session['model_name'] = model_name
    what_id_of_dataset = Dataset.objects.filter(name=model_name).values_list(flat = True)
    dataset1 = Attribute.objects.filter(id_dataset=what_id_of_dataset[0])
    args_lst = []
    for i in dataset1[1:]:
        args_lst.append(i)
    data = {"model_name": model_name, "a1":args_lst[0], "a2":args_lst[1],"a3":args_lst[2],"a4":args_lst[3],"a5":args_lst[4],"a6":args_lst[5],"a7":args_lst[6],"a8":args_lst[7],"a9":args_lst[8]}
    return render(request, num_args+'args9.html',{'data':data})

def args9_chances(request):
    model_name = request.session.get('model_name')
    model_name1 = pickle_path+model_name+'_model.pickle'
    if request.POST.get('action') == 'post':
        a1 = float(request.POST.get('a1'))
        a2 = float(request.POST.get('a2'))
        a3 = float(request.POST.get('a3'))
        a4 = float(request.POST.get('a4'))
        a5 = float(request.POST.get('a5'))
        a6 = float(request.POST.get('a6'))
        a7 = float(request.POST.get('a7'))
        a8 = float(request.POST.get('a8'))
        a9 = float(request.POST.get('a9'))
        model = pd.read_pickle(model_name1)
        result = model.predict([[a1, a2, a3, a4, a5, a6, a7, a8, a9]])
        classification = result[0]
        return JsonResponse({'result': classification, 'a1': a1,'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6':a6,'a7':a7,'a8':a8,'a9':a9},safe=False)



### Database List
def database_list(request):
    data = {"dataset1": Dataset.objects.all().iterator(),
            "dataset2": Content.objects.all().iterator(),
            "dataset3": Attribute.objects.all().iterator()}
    return render(request, "database_list.html",{'data':data})

