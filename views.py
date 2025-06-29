from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def demo(request):
    
#  return render(request,"forms.html")
from django.shortcuts import render
from datetime import date

def demo(request):
    output = ""
    if request.method == "POST":
        day = int(request.POST.get("bday"))
        month = int(request.POST.get("bmonth"))
        year = int(request.POST.get("byear"))

        today = date.today()
        age_year = today.year - year
        age_month = today.month - month
        age_day = today.day - day

        if age_day < 0:
            age_month -= 1
            previous_month = today.month - 1 if today.month > 1 else 12
            previous_year = today.year if today.month > 1 else today.year - 1
            days_in_prev_month = (date(previous_year, previous_month + 1, 1) - date(previous_year, previous_month, 1)).days
            age_day += days_in_prev_month

        if age_month < 0:
            age_year -= 1
            age_month += 12

        output = f"Your age is {age_year} years, {age_month} months, and {age_day} days."
        
    return render(request, "forms.html", {"o": output})
