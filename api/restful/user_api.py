from api.utils import *
from django.contrib.auth import logout as django_logout, login as django_login
from administration.forms import (UserAuthenticationForm, UserChangePasswordForm, UserResetPassword,
                                  GrantUserPermissionForm)


@api_view(['POST', ])
def login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            (user, token) = form.authenticate()
            if user:
                django_login(request, user)
                response_data = dict({'status': 'success', 'result': cache_user(user, token), })
                return Response(data=response_data, status=status.HTTP_200_OK)
        return Response(data={'result': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'result': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', ])
def customer_signup(request):
    return create_customer(request)


@api_view(['POST', ])
def logout(request):
    if request.method == 'POST':
        token = request.POST['token']
        user_cache = LMBCache()
        user_cache.delete(token)
        django_logout(request)
        return Response(data={}, status=status.HTTP_200_OK)
    return Response(data={'result': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


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


@api_view(['POST', ])
def grant_admin_permission_groups(request):
    # FIXME : Check if user login as president
    if request.method == 'POST':
        form = GrantUserPermissionForm(request.POST)
        permission_group_list = [int(i) for i in request.POST.getlist('permission_groups[]')]
        if form.is_valid() and permission_group_list:
            user = form.authenticate()
            if isinstance(user, OrgAdmin):
                update_admin_permission_group(user, permission_group_list)
                return Response(data={'result': 'success'}, status=status.HTTP_200_OK)
        return Response(data={'result': 'Invalid inputs'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'result': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
