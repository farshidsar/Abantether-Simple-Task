from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class BaseRepository:
    def __init__(self, model: models.Model):
        self._model = model

    def get_by_id(self, id):
        return self._model.objects.get(id=id)

    def get(self, **kwargs):
        try:
            return self._model.objects.get(**kwargs)
        except self._model.DoesNotExist:
            raise ObjectDoesNotExist('not found')

    def filter(self, **kwargs):
        return self._model.objects.filter(**kwargs)

    def create(self, **kwargs):
        return self._model.objects.create(**kwargs)

    def update(self, instance, **kwargs):
        for field, value in kwargs.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def get_or_create(self, **kwargs):
        return self._model.objects.get_or_create(**kwargs)
