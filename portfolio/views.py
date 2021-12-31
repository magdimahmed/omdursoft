from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm
from.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'portfolio/file_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'portfolio/file_upload.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'magdimahmed@yahoo.com',
                          ['magdimahmed@yahoo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("portfolio:home")

    form = ContactForm()
    return render(request, "portfolio/contact.html", {'form': form})
