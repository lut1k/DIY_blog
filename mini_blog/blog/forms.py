from django import forms


class BlogListForm(forms.Form):
    CHOICE = (
        ('id', 'ID'),
        ('publication_date', u'Дата публикации'),
        ('author', 'Автор'),
        ('title', 'Название')
    )

    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=CHOICE, required=False)