from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
    # title = forms.CharField(max_length=150)
    # slug = forms.SlugField(max_length=150)
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'slug': forms.TextInput(attrs={'class': 'form-control'})
    }
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'create':
            raise ValidationError('Slug "create" not accepted')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'slug should be unique. "{new_slug}" already created.')
        return new_slug

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title = self.cleaned_data.get('title'),
    #         slug = self.cleaned_data.get('slug')
    #     )
    #     return new_tag