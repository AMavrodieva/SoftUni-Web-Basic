from django import forms

from library.online_library.models import Profile, Book


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': "First Name",
            'image_url': "Image URL",
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': "Last Name"}
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': "URL"}
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            # field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False



class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookAddForm(BookBaseForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': "Title"}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': "Descriptions"}
            ),
            'image': forms.URLInput(
                attrs={'placeholder': "Image"}
            ),
            'type': forms.TextInput(
                attrs={'placeholder': "Fiction, Novel, Crime.."}
            ),
        }


class BookEditForm(BookBaseForm):
    pass





