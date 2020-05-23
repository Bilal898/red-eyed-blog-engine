from django.shortcuts import render, get_object_or_404
from .models import *

class DetailObjectMixin:
    model = None
    template = None
    def get(self, request, slug):   #post_detail renamed
        # post = self.model.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {
            self.model.__name__.lower(): obj
        }
        return render(request, self.template, context)



    
