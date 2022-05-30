from django.contrib import admin
from loan.models import DebtModel, LoanModel


admin.site.register(DebtModel)
admin.site.register(LoanModel)