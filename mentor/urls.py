"""mentor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import *
from django.conf.urls import url
from m1 import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


# for registration DB coding
# from django.conf.urls import url
# from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('had/',views.had,name="had"),
    path('contact/',views.contact,name="contact"),
    path('business/',views.business,name="business"),
    # path('booking/',views.booking,name="booking"),
    path('student/',views.student,name="student"),
    path('login/',views.login,name="login"),
    path('meet/',views.meet,name="meet"),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('pricing/', views.pricing, name='pricing'),
    path('feedback/', views.feedback, name='feedback'),
    path('registration/', views.registration, name='registration'),
    path('order/', views.order, name='order'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('handlerequest/', views.handlerequest, name='handlerequest'),

    # path('password/', views.change_password, name='change_password'),





    


    #url(r'^activation/(?P<user_id>[0-9]+)/$', views.activation, name='activation'),
     # Change Password
    # path(
    #     'change-password/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='commons/change-password.html',
    #         success_url = '/'
    #     ),
    #     name='change_password'
    # ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset_form.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',
             #success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]


