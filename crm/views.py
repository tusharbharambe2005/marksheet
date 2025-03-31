from django.shortcuts import render
from .models import Student  

def search_marksheet(request):
    roll_number = request.GET.get('roll_number', '').strip()  # Ensure no leading/trailing spaces
    marksheet = None

    if roll_number:
        marksheet = Student.objects.filter(Roll_Number__iexact=roll_number).first()

    return render(request, 'search.html', {'marksheet': marksheet, 'roll_number': roll_number})
