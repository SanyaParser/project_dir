from django import forms
from django.core.exceptions import ValidationError

from .models import Product
# Если можно обойтись переопределением поля формы forms.CharField(min_length=20)
# лучше воспользоваться им. Если требуется проверить одно поле сложным образом,
# создайте для этого метод clean_fieldname. В случае необходимости использования нескольких полей
# одновременно воспользуйтесь методом clean.


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'price',
            'quantity',
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data
