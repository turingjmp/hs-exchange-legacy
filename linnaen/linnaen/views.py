from django.http import HttpResponse

from linnaen.models import Species

def species_list(request):
    all_species = Species.objects.order_by('name')
    return HttpResponse("hi")

def species(request, name):

    return
