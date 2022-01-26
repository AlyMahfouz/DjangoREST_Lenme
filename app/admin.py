from django.contrib import admin

# Register your models here.

from .models import Borrower, Investor, Loan, Offer


admin.site.register(Borrower)
admin.site.register(Investor)
admin.site.register(Loan)
admin.site.register(Offer)
