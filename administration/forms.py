from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from administration.models import University, OrgAdmin, Customer, CustomerUPG


USER_BACKEND = 'django.contrib.auth.backends.ModelBackend'


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
        if CustomerUPG.customer_upg.all().filter(customer=customer, university=university).exists():
            return True
        return False

    def update_customer_university_group(self):
        customer = self.cleaned_data.get('customer')
        university = self.cleaned_data.get('university')
        permission_group = self.cleaned_data.get('permission_group')
        grant_level = self.cleaned_data.get('grant_level')
        customer_in_university = CustomerUPG.customer_upg.all().filter(customer=customer, university=university) or None
        if customer_in_university is None or customer_in_university.count() > 1:
            # TODO : write validation
            raise Exception('Duplicated object !')
        elif customer_in_university.count() == 1:
            customer_in_university[0].permission_group = permission_group
            customer_in_university[0].grant_level = grant_level
            customer_in_university[0].save()
        return customer_in_university[0]


class UserAuthenticationForm(forms.Form):
    username = forms.CharField(label='Username')
    user_role = forms.CharField(label='user_role')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def authenticate(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_role = self.cleaned_data.get('user_role')
        user = None
        if user_role == 'admin':
            user = OrgAdmin.org_admins.get_auth_admin(username)
        elif user_role == 'customer':
            user = Customer.customers.get_auth_customer(username)
        if user and user.check_password(password):
            user.backend = USER_BACKEND
            return user
        return None


class UserChangePasswordForm(forms.Form):
    username = forms.CharField(label='Username')
    user_role = forms.CharField(label='user_role')
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match !')
        return password2

    def authenticate(self):
        username = self.cleaned_data.get('username')
        old_password = self.cleaned_data.get('old_password')
        user_role = self.cleaned_data.get('user_role')
        user = None
        if user_role == 'admin':
            user = OrgAdmin.org_admins.get_auth_admin(username)
        elif user_role == 'customer':
            user = Customer.customers.get_auth_customer(username)
        if user and user.check_password(old_password):
            user.backend = USER_BACKEND
            return user
        return None

    def set_password(self):
        user = self.authenticate()
        password = self.clean_password2()
        if user and password:
            user.set_password(password)
            user.save()
            return user
        return None


class UserResetPassword(forms.Form):
    username = forms.CharField(label='Username')
    user_role = forms.CharField(label='user_role')
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match !')
        return password2

    def get_user(self):
        username = self.cleaned_data.get('username')
        user_role = self.cleaned_data.get('user_role')
        user = None
        if user_role == 'admin':
            user = OrgAdmin.org_admins.get_auth_admin(username)
        elif user_role == 'customer':
            user = Customer.customers.get_auth_customer(username)
        if user:
            user.backend = USER_BACKEND
            return user
        return None

    def reset_password(self):
        user = self.get_user()
        password = self.clean_password2()
        if user and password:
            user.set_password(password)
            user.save()
            return user
        return None
