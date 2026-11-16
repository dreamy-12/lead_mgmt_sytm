"""
URL configuration for Lead_Mgmt_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from accounts.views import SignupView
from accounts.views import AuthUserDetailView

from rest_framework.authtoken.views import ObtainAuthToken

from leads.views import LeadCreateListView
from leads.views import LeadRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',SignupView.as_view()),

    path('accounts/login/',ObtainAuthToken.as_view()),# for creating token

    path('accounts/profile/',AuthUserDetailView.as_view()),

    path('leads/',LeadCreateListView.as_view()),

    path('leads/<int:pk>/',LeadRetrieveUpdateDeleteView.as_view()),


]
