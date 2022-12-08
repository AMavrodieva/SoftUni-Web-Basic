from django import forms

from notes.notes_app.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')


class NoteCreateForm(NoteBaseForm):
    pass


class NoteEditForm(NoteBaseForm):
    pass


class NoteDeleteForm(NoteBaseForm):
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


