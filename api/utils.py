from api.restful.administration_api import *
# from api.restful.content_api import *


def _get_user_permissions(user):
    response_data = dict()
    if isinstance(user, Customer):
        response_data['email'] = user.email
        response_data['role'] = 'customer'
        response_data['permission_groups'] = list()
        upg_list = CustomerUPG.customer_upg.all().filter(customer=user)
        for upg in upg_list:
            org_feature_permissions = [dict(permision_id=permission.pk,
                                            permission_type=permission.permission_type,
                                            feature_id=permission.feature.pk,
                                            feature_name=permission.feature.feature_name)
                                       for permission in upg.permission_group.permission.all()]
            response_data['permission_groups'].append(dict({'university_id': upg.university.pk,
                                                            'university_name': upg.university.university_name,
                                                            'permission_group_id': upg.permission_group.pk,
                                                            'feature_permissions': org_feature_permissions,
                                                            'grant_level': upg.grant_level, }))
    elif isinstance(user, OrgAdmin):
        response_data['username'] = user.username
        response_data['role'] = 'admin'
        response_data['university_id'] = user.university.pk
        response_data['university_name'] = user.university.university_name
        response_data['permission_groups'] = list()
        for group in user.permission_group.all():
            org_feature_permissions = [dict(permision_id=permission.pk,
                                            permission_type=permission.permission_type,
                                            feature_id=permission.feature.pk,
                                            feature_name=permission.feature.feature_name)
                                       for permission in group.permission.all()]
            response_data['permission_groups'].append(dict(permission_group_name=group.group_name,
                                                           permission_group_id=group.pk,
                                                           feature_permissions=org_feature_permissions))
    else:
        raise Exception(LMBError(content=user))
    return response_data


def cache_user_permissions(user):
    return _get_user_permissions(user)


def _response_message_handler(code, response_dict, name=''):

    status_code_map = {
        400: LMBBadRequest,
        405: LMBMethodNotAllowed,
    }

    return


class LMBError:

    message = u'Unknown error occurred. Response content: {content}'

    def __init__(self, url='', status_code='', content='None'):
        self.url = url
        self.status_code = status_code
        self.content = content

    def __str__(self):
        return self.message.format(content=self.content)

    def __unicode__(self):
        return self.__str__()


class LMBBadRequest(LMBError):

    message = u'Malformed request. Response content: {content}'


class LMBMethodNotAllowed(LMBError):

    def __str__(self):
        return u'HTTP METHOD IS NOT ALLOWED'
