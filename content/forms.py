from django import forms


class FileUploadForm(forms.Form):
    file_name = forms.CharField(max_length=50)
    file = forms.FileField(label='Please select a file')
    # TODO : specify which form need upload file
