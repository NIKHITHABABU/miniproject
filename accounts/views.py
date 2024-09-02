from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Registers

# Existing views
def open(request):
    return render(request, 'index.html')

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
        name = request.POST.get('name')  # Field in table; variable to store
        # lastname = request.POST.get('lname')
        department = request.POST.get('department')
        # phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        password = request.POST.get('password')

        data = Registers.objects.create(name=name, department=department,mail=mail, password=password)
        data.save()
        messages.success(request, "Registration successful!")
    return render(request, "index.html")  # Function to access register fields

# New login view
def student_login(request):
    if request.method == 'POST':
        print("Form submitted")  # Debugging: Check if form is being submitted
        mail = request.POST.get('mail')  # Get email from form
        password = request.POST.get('password')  # Get password from form

        try:
            user = Registers.objects.get(mail=mail, password=password)
            request.session['user_id'] = user.id  # Store user ID in session
            messages.success(request, "Login successful!")
            return redirect('shome')  # Redirect to student home (change URL as needed)
        except Registers.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')

def student_dashboard(request):
    if 'user_id' in request.session:  # Check if the user is logged in
        return render(request, 'student_dashboard.html')  # Render the dashboard page
    else:
        return redirect('login')  # Redirect to login page if not logged in
    

# views.py
def logout(request):
    request.session.flush()  # Clear the session
    messages.success(request, "Logged out successfully.")
    return redirect('login')  # Redirect to login page


def addcomp(request):
    return render(request, 'addcomplaint.html')


def stdhome(request):
    return render(request, 'studenthome.html')

def complaint(request):
    if request.method == "POST":
        title = request.POST.get('ctitle')  # Field in table; variable to store
        # lastname = request.POST.get('lname')
        type= request.POST.get('ctype')
        # phone = request.POST.get('phone')
        description = request.POST.get('cdescription')
        # password = request.POST.get('password')

        data = complaints.objects.create(ctitle=title, ctype=type,cdescription=description)
        data.save()
        messages.success(request, "Registration successful!")
    return render(request, "index.html")