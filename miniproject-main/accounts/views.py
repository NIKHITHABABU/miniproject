from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from .models import Registers, Grievance, feedbackforms
from .forms import GrievanceForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppealForm

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
        name = request.POST.get('name')
        department = request.POST.get('department')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        object=Registers(name=name, department=department, mail=mail, password=password)
        object.save()
        # Registers.objects.create(name=name, department=department, mail=mail, password=password)
        # messages.success(request, "Registration successful!")
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
    if 'user_id' in request.session:
        request.session.flush()  # Clear session data, including user_id
        messages.success(request, "Logged out successfully.")
    else:
        messages.info(request, "You are not logged in.")
    return redirect('index')


def addcomp(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            department = request.POST['department']
            complaint_title = request.POST['complaint_title']
            type_of_grievance = request.POST['type_of_grievance']
            complaint_description = request.POST['complaint_description']
            
            # Save the grievance
            Grievance.objects.create(
                name=name,
                department=department,
                complaint_title=complaint_title,
                type_of_grievance=type_of_grievance,
                complaint_description=complaint_description
            )
            
            return redirect('shome')  # Replace with the appropriate redirect
        
        return render(request, 'addcomplaint.html')
    else:
        return redirect('login')

def stdhome(request):
    return render(request, 'studenthome.html')

def stdfeedback(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        message = request.POST["message"]
        feedbackforms.objects.create(fname=fname, lname=lname, email=email, message=message)
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('feedbacktemplate')
    return render(request, 'feedbacktemplate.html')

def adminlogin(request):
    if request.method == "POST":
        uname = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=uname, password=password)
        if user is not None and user.is_staff and user.is_superuser:
            auth.login(request, user)
            return redirect('adminhome')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'adminlogin.html')

def ahome(request):
    return render(request, 'adminhome.html')

def ufeedbackform(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        message = request.POST["message"]
        feedbackforms.objects.create(fname=fname, lname=lname, email=email, message=message)
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('ufeedbackform')
    return render(request, 'feedbacktemplate.html')

# Admin Feedback Form Viewing
def admfeedbform(request):
    feedbacks = feedbackforms.objects.all()
    return render(request, 'adminfeedbackview.html', {'feedbacks': feedbacks})


def faculty_login(request):
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
    
    # Return the login form for GET requests
    return render(request, 'facultylogin.html')


def indexcontact(request):
    return render(request, 'contact.html')

def admingrievanceview(request):
    grievances = Grievance.objects.all()  # Fetch all grievances
    return render(request, 'admingrievanceview.html', {'grievances': grievances})



def admin_resolution_view(request):
    if request.method == 'POST':
        grievance_id = request.POST.get('grievance_id')
        resolution = request.POST.get('resolution')

        # Fetch the grievance and update its resolution
        grievance = Grievance.objects.get(id=grievance_id)
        grievance.resolution = resolution
        grievance.save()

        # Add success message
        messages.success(request, 'Resolution submitted successfully!')

        return redirect('admin_resolution')  # redirect to the same page to show updated data

    # Fetch all grievances
    grievances = Grievance.objects.all()

    return render(request, 'adminresolution.html', {'grievances': grievances})



def appeal_form(request):
    if request.method == 'POST':
        form = AppealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('shome')  # Redirect to a success page after submission
    else:
        form = AppealForm()

    return render(request, 'appealform.html', {'form': form})