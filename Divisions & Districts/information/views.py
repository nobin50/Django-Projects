from django.shortcuts import render
from .models import Districts, Divisions


def district_list(request):
    districts = Districts.objects.all()
    context = {
        'districts': districts,
    }
    return render(request, 'districts.html', context)



def division_list(request):
    divisions = Divisions.objects.all()
    context = {
        'divisions': divisions,
    }
    return render(request, 'divisions.html', context)



def dists_of_division(request, div_id):
    division = Divisions.objects.get(pk = div_id)
    districts = Districts.objects.filter(division = division)
    context = {
         'districts': districts,
         'division': division,
    }

    return render(request, 'dists_of_division.html', context)

"""
def district_list(request):
    div = Divisions.objects.get(name='Khulna')
    districts = Districts.objects.filter(division=div)
    return render(request, 'districts.html', {'districts':districts})
"""
