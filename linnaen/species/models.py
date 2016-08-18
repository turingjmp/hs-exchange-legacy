from django.db import models

class Discoverer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s, %s".format(self.last_name, self.first_name)

class Family(models.Model):
    name = models.CharField(max_length=30)
    discoverer = models.ForeignKey(Discoverer, blank=True)

    def __unicode__(self):
        return self.name


class Genus(models.Model):
    name = models.CharField(max_length=30)
    family = models.ForeignKey(Family)
    discoverer = models.ForeignKey(Discoverer, blank=True)

    def __unicode__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=30)
    genus = models.ForeignKey(Genus)
    discoverer = models.ForeignKey(Discoverer, blank=True)

    def __unicode__(self):
        return self.name
