from django.shortcuts import render
from .models import Expense

def my_expense(request):
    expenses = Expense.objects.all()

    return render(request, 'expenses.html', {'expenses': expenses})
