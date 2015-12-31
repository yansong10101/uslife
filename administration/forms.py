from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from administration.models import University, OrgAdmin, Customer, CustomerUPG


class UniversityForm(forms.ModelForm):

    class Meta:
        model = University
        fields = ('university_name', 'university_code', )


class CustomerCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email', 'first_name', 'last_name', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match !')
        return password2

    def save(self, commit=True):
        user = super(CustomerCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# class CustomerChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = Customer
#         fields = ('email', 'password', 'is_active', 'first_name', 'last_name', )
#
#     def clean_password(self):
#         return self.initial['password']


class OrgAdminCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = OrgAdmin
        fields = ('university', 'username', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match !')
        return password2

    def save(self, commit=True):
        user = super(OrgAdminCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomerUPGForm(forms.ModelForm):

    class Meta:
        model = CustomerUPG
        fields = ('customer', 'university', 'permission_group', 'grant_level', )

    def validate_existing(self):
        customer = self.cleaned_data.get('customer')
        university = self.cleaned_data.get('university')
        permission_group = self.cleaned_data.get('permission_group')
        if CustomerUPG.customer_upg.all().filter(customer=customer, permission_group=permission_group,
                                                 university=university).exists():
            return True
        return False
