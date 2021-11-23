from django.shortcuts import render

# Create your views here.


def homepage(request):
    message = ''

    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        if fullname == "" or phone == "":
            message = "Please fill both fields"
        else:
            message = fullname+phone
    context = {'message': message}
    return render(request, 'contactus/index.html', context)


def contactus(request):

    return render(request, 'contactus/contactus.html')
