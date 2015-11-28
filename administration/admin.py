from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from administration.models import Customer, University


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'university_name', 'university_code', )
    ordering = ('university_name', )


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
            raise forms.ValidationError('Passwords don not match !')
        return password2

    def save(self, commit=True):
        user = super(CustomerCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomerChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Customer
        fields = ('email', 'password', 'is_active', 'first_name', 'last_name', )

    def clean_password(self):
        return self.initial['password']


class CustomerAdmin(UserAdmin):
    form = CustomerChangeForm
    add_form = CustomerCreationForm

    list_display = ('email', 'is_active', 'is_admin', 'first_name', 'last_name', )
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ('email', 'password', ), }),
        # ('Personal info', {'fields': ('first_name', 'last_name', ), }),
        # ('Permissions', {'fields': ('is_admin', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', )
        }),
    )
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()

admin.site.register(University, UniversityAdmin)
admin.site.register(Customer, CustomerAdmin)
