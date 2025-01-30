from django.contrib import admin
from django.urls import path
from .import views
from .views import CustomLogoutView
from django.conf.urls import handler404

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('accounts/login',views.login,name='login'),
    path('logout',CustomLogoutView.as_view(),name='logout'),
    path('profile_view',views.profile_view,name='profile_view'),
    path('accounts/update_profile',views.update_profile,name='update_profile'),
    path('delete_profile',views.delete_profile,name='delete_profile'),
    path('contact',views.contact,name='contact'),
   
    
] 



handler404 = 'accounts.views.custom_404'