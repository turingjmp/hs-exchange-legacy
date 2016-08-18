from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
import json

from linnaen.models import Genus, Species

not_allowed = HttpResponseNotAllowed(json.dumps({'error': "Method not allowed"}))

# Family #

def family_list(request):

    if request.method == 'GET':
        all_families = Family.objects.order_by('name')
        return HttpResponse(json.dumps([x for x in all_families]),
                content_type="application/json")

    elif request.method == 'POST':
        new = Family(**request.raw_post_data)
        new.save()
        return HttpResponse("")

    else:
        return not_allowed

# Genus #

def genus_list(request):

    if request.method == 'GET':
        all_genuses = Genus.objects.order_by('name')
        return HttpResponse(json.dumps([x for x in all_genuses]),
                content_type="application/json")

    elif request.method == 'POST':
        new = Genus(**request.raw_post_data)
        new.save()
        return HttpResponse("")

    else:
        return not_allowed

# Species #

def species_list(request):

    if request.method == 'GET':
        discoverer = request.GET.get("discovere")    # oops!
        if discoverer:
            all_species = Species.objects.order_by('name').filter(
                    discoverer__last_name=discoverer)
        else:
            all_species = Species.objects.order_by('name')
        return HttpResponse(json.dumps([x for x in all_species]),
                content_type="application/json")

    elif request.method == 'POST':
        new = Species(**request.raw_post_data)
        new.save()
        return HttpResponse("")

    else:
        return not_allowed

def species(request, name):

    if request.method == 'GET':
        result = Species.objects.filter(name=name)
        if result:
            return HttpResponse(json.dumps([x for x in result]),
                    content_type="application/json")
        else:
            return HttpResponseNotFound("{}", content_type="application/json")

    else:
        return not_allowed
