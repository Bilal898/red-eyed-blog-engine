from django.shortcuts import render, get_object_or_404, redirect
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


class CreateObjectMixin:
    model = None
    template = None

    def get(self, request):
        form = self.model
        context = {
            'form': form
        }
        return render(request, self.template, context)

    def post(self, request):
        bound_form = self.model(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        return render(request, self.template, context={'form': bound_form})

    
