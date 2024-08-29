from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Registers

# Existing views
def open(request):
    return render(request, 'index.html')

def registeropen(request):
    return render(request, 'reg.html')

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
        firstname = request.POST.get('fname')  # Field in table; variable to store
        lastname = request.POST.get('lname')
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        password = request.POST.get('password')

        data = Registers.objects.create(fname=firstname, lname=lastname, department=department, phone=phone, mail=mail, password=password)
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
def student_login(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')  # Get email from form
        password = request.POST.get('password')  # Get password from form

        try:
            user = Registers.objects.get(mail=mail, password=password)
            request.session['user_id'] = user.id  # Store user ID in session
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to the student dashboard
        except Registers.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')

# views.py
def logout(request):
    request.session.flush()  # Clear the session
    messages.success(request, "Logged out successfully.")
    return redirect('login')  # Redirect to login page


def addcomp(request):
    return render(request, 'addcomplaint.html')