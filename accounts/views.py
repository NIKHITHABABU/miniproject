# views.py
from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import Registers, Grievance, feedbackforms
from .forms import GrievanceForm

def open(request):
    return render(request, 'index.html')

# ... other existing views ...
def registeropen(request):
    return render(request, 'stdreg.html')

def adreg(request):
    return render(request, 'adminreg.html')

def samp(request):
    return render(request, 'sample.html')

def shome(request):
    return render(request, 'studenthome.html')

def indexabout(request):
    return render(request, 'about.html')

def facultyreg(request):
    return render(request, 'facreg.html')

def log(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        department = request.POST.get('department')
        mail = request.POST.get('mail')
        password = request.POST.get('password')

        Registers.objects.create(name=name, department=department, mail=mail, password=password)
        messages.success(request, "Registration successful!")
    return render(request, "index.html")

def student_login(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')

        try:
            user = Registers.objects.get(mail=mail, password=password)
            request.session['user_id'] = user.id
            messages.success(request, "Login successful!")
            return redirect('shome')
        except Registers.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')

def student_dashboard(request):
    if 'user_id' in request.session:
        return render(request, 'student_dashboard.html')
    else:
        return redirect('login')

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')

def addcomp(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Grievance submitted successfully!")
            return redirect('shome')  # Redirect to a page or return a success message
    else:
        form = GrievanceForm()

    return render(request, 'addcomplaint.html', {'form': form})

def stdhome(request):
    return render(request, 'studenthome.html')

def stdfeedback(request):

    if request.method=="POST":

        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        message=request.POST["message"]
        instance=feedbackforms.objects.create(fname=fname,lname=lname,email=email,message=message)
        # instance.save()
        # messages.info(request,'Feedback submitted successfully!')
        return render(request,'feedbacktemplate.html')

    return render(request,'feedbacktemplate.html')