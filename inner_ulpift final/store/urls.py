from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.basiclink import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('', Index.as_view(), name='homepage'),
    path('podcas&books', store , name='podcas&books'),
#basic link  
    path('cources', courses_page, name='coursespage'),
    path('contact', contact_page, name='contactpage'),
    path('services',service_page,name="services_page"),
    path('about',aboutus_page,name="aboutus_page"),
    path('career',career_page,name="career_page"),
    path('jobs/list',job_list_page,name="joblist_page"),
    path('payments',payments_page,name="payments_page"),
#end basic link  
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
