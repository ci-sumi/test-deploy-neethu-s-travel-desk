from django.shortcuts import render, redirect
from .forms import BudgetCalculatorForm
from .models import BudgetCalculator

#Allow user to calculate their budget
def budget_calculator(request):
    total_cost = None

    if request.method == 'POST':
        form = BudgetCalculatorForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            total_cost = budget.total_cost()
            budget.save()

    else:
        form = BudgetCalculatorForm()

    return render(request, 'budget.html', {
        'form': form,
        'total_cost': total_cost
    })
