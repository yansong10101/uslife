from api.restful.administration_api import *
from django.contrib.auth import logout as django_logout, login as django_login
from administration.forms import UserAuthenticationForm, UserChangePasswordForm, UserResetPassword


@api_view(['POST', ])
def login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
            if user:
                django_login(request, user)
                request.session['user_role'] = request.POST['user_role']
                return Response(data={'result': 'success'}, status=status.HTTP_200_OK)
        return Response(data={'result': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'result': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', ])
def customer_signup(request):
    create_customer(request)


@api_view(['POST', ])
def logout(request):
    django_logout(request)
    return Response(data={}, status=status.HTTP_200_OK)


@api_view(['POST', ])
def change_password(request):
    if request.method == 'POST':
        form = UserChangePasswordForm(request.POST)
        if form.is_valid():
            user = form.set_password()
            if user:
                django_login(request, user)
                return Response(data={'result': 'success'}, status=status.HTTP_200_OK)
        return Response(data={'result': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'result': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', ])
def reset_password(request):
    if request.method == 'POST':
        form = UserResetPassword(request.POST)
        if form.is_valid():
            user = form.reset_password()
            if user:
                django_login(request, user)
                return Response(data={'result': 'success'}, status=status.HTTP_200_OK)
        return Response(data={'result': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'result': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)