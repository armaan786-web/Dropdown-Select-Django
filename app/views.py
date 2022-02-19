from django.shortcuts import render
from .models import Restaurant,Employee

# Create your views here.

def home(request):
    selected_region = None
    selected_region2 = None
    restaurants = Restaurant.objects.all()
    employee = Employee.objects.all()

    if request.method == "POST":
        # Filter restaurants by selected region, but only on a POST
        selected_region = request.POST.get("region")
        restaurants = restaurants.filter(region=selected_region)

        selected_region2 = request.POST.get("city")
        employee = employee.filter(city=selected_region2)

    # Get a list of all unique regions (group by region)  
    regions = Restaurant.objects.order_by('region').values_list('region', flat=True)
    regions2 = Employee.objects.order_by('city').values_list('city', flat=True)

    context = {
        'regions': regions,
        'restaurants': restaurants,
        'selected_region': selected_region,
        'regions2': regions2,
        'employee': employee,
        'selected_region2': selected_region2,
    }

    return render(request, 'index.html', context)
    # return render(request,'index.html')
