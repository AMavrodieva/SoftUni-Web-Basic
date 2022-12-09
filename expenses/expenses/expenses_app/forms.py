import os

from django import forms

from expenses.expenses_app.models import Profile, Expenses


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {
            'first_name': "First Name",
            'last_name': 'Last Name',
            'profile_image': "Profile Image"
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ()

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_input()

    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        self.instance.delete()
        os.remove(image_path)

        return self.instance

    def __set_hidden_input(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class ExpensesBaseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': "Link to Image",
        }


class ExpensesCreateForm(ExpensesBaseForm):
    class Meta:
        model = Expenses
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': "Link to Image",
        }


class ExpensesEditForm(ExpensesBaseForm):
    pass


class ExpensesDeleteForm(ExpensesBaseForm):
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
