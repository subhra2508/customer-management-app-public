"""crm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

from accounts.views import(
    registerPage,
    loginPage,
    logoutUser,
    userPage,
    accountSettings,
    home,
    products,
    customers,
    creatOrder,
    updateOrder,
    deleteOrder,
)
 
urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/',registerPage,name='register'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),

    path('user/',userPage,name='user-page'),
    path('account/',accountSettings,name="account"),
    
    path('',home,name="home"),
    path('products/',products,name="products"),
    path('customers/<str:pk>/',customers,name="customers"),
    path('create_order/<str:pk>/',creatOrder,name="create_order"),
    path('update_order/<str:pk>/',updateOrder,name="update_order"),
    path('delete_order/<str:pk>/',deleteOrder,name="delete_order"),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="password_reset"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

'''
1-submit email form                 //PasswordResetView.as_view()
2- Email sent success message       //PasswordResetDoneView.as_view()
3- link to password reset form in email //PasswordResetConfirmView.as_view()
4-password successfully changed message //PasswordResetCompleteView.as_view()

'''
 