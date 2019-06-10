from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''allow user to edit their own profiles'''

    def has_object_permission(self, request, view, obj):
        '''check user is tryin gto edit their own profile'''

        if request.method in permissions.SAFE_METHODS:
            return True
        '''the following comparision is chenking that the object(obj) the user is try ing to change has 
        the same id that the user curruntily authanticating in the system i.e request.user.id
        if both same then permission is True
        and if not then permisin is denied
        '''
        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    '''Allow user to update you rown status'''

    def has_object_permission(self, request, view, obj):
        '''check user is trying to update their own status'''

        if request.method in permissions.SAFE_METHODS:
            return True
        '''
        it will check that the user profile id of the status item they are trying to
         update matches the request.user.id which is the same the user that is logind in   right now 
        '''
        return obj.user_profile.id == request.user.id