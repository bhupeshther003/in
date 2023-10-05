from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from django.core.mail import send_mail

class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            send_mail(
                subject=f'Message from InnerUplift - Account Create Successfully',
                message=f'Dear {first_name} {last_name},\n\n'
                        f'We are thrilled to have you as a member of our community. With your new account, you can access a wide range of exciting features, including:\n\n'
                        f'Your account details:'
                        f'Email: {email}\n'
                        f'First Name: {first_name} {last_name}\n'
                        f'Mobile Number: {phone}\n\n\n\nIf you have any questions or need assistance, please feel free to contact our support team at bhupeshther5@gmail.com \n We are delighted to have you as a member of our community. \n\n\n\n Best regards, \n Inner Uplift \n bhupeshther5@gmail.com \n +91 7378417908 \n',
                from_email='bhupeshther5@gmail.com',  # Replace with your email
                recipient_list={email},
                fail_silently=False,
               )   
            return redirect ('home_page')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
