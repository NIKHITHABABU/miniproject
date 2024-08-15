from django.shortcuts import render,HttpResponse

# Create your views here.
def open(request):
    return render(request,'index.html')
def register(request):
    return render(request,'reg.html')
def adreg(request):
    return render(request,'adminreg.html')
def samp(request):
    return render(request,'sample.html')
def shome(request):
    return render(request,'studenthome.html')
# def bases(request):
    # return render(request,'base.html')