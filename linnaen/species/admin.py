from django.contrib import admin

from species.models import Family, Genus, Species

admin.site.register(Family)
admin.site.register(Genus)
admin.site.register(Species)
# Register your models here.
