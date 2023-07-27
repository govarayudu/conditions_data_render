from django.shortcuts import render

# Create your views here.
def data_render1(request):
    d={'name':'Satish','age': 25}
    return render(request,'data_render1.html',context=d)