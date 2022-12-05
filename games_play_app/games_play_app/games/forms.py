from django import forms

from games_play_app.games.models import Profile, Game


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'profile_picture': 'Profile Picture'
        }


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_input()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Game.objects.all().delete()
        return self.instance

    def __set_hidden_input(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'max_level': 'Max Level'
        }


class GameCreateForm(GameBaseForm):
    pass


class GameDetailForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(GameBaseForm):
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

