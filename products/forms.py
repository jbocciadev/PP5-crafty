from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review

from pprint import pprint


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = '__all__'

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class ProductReviewForm(forms.ModelForm):

    class Meta:
            model = Review
            fields = ('rating', 'review')

            widgets = {
                'rating': forms.RadioSelect(attrs={'class':'yayayayaya'}),
            }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['rating'].widget.attrs.update({'class': 'yayayayayayaya'})
    #     print(self.fields['rating'])

            # for i in vars(self):
            #     pprint(i)
            # for i in self:
            #     for j in i:
            #         print(f"item in form: {j}")

            # for visible in self.visible_fields():
            #     visible.field.widget.attrs['class'] = 'form-control'
            # self.fields['rating'].widget.attrs.update({'class': 'rating-radio'})

        
             
        