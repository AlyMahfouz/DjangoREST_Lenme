"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# Create your urls here.

import app.views as func

urlpatterns = [
    path('admin/', admin.site.urls),

    path('create_borrower', func.create_borrower),
    path('create_investor', func.create_investor),

    path('view_borrowers', func.view_borrowers),
    path('view_investors', func.view_investors),

    path('loan_request', func.loan_request),
    path('offer_request', func.offer_request),
    path('accept_offer', func.accept_offer),
    
    path('monthly_payment', func.monthly_payment)
]