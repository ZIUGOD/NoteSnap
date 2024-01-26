from django import forms
from .models import Note
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper


class NoteForm(forms.ModelForm):
    """
    A Django Form class for interacting with the 'Note' model. It extends
    forms.ModelForm, providing a convenient way to create or update Note
    instances through a web form.

    The form includes a 'title' field and a 'text' field with a CKEditor
    widget for rich text editing. The __init__ method is customized to set
    custom labels for the 'title' and 'text' fields.
    """

    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Note
        fields = ["title", "text"]

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_tag = False
        self.helper.label_class = "col-lg-2"
