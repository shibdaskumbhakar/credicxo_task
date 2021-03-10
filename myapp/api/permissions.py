from rest_framework.permissions import BasePermission

########## custom permission for Teacher auth....
class IsTeacher(BasePermission):
    """
    Allows access only to "IsTeacher" users.
    """

    def has_permission(self, request, view):
        is_teacher = False
        if request.user.groups.filter(name='teacher').exists():
            is_teacher = True
        return request.user and is_teacher

########## custom permission for student auth...
class IsStudent(BasePermission):
    """
    Allows access only to "IsStudent" users.
    """

    def has_permission(self, request, view):
        is_teacher = False
        if request.user.groups.filter(name='student').exists():
            is_teacher = True
        return request.user and is_teacher
