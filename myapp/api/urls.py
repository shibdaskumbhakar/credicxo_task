from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
urlpatterns = [
    ############ Student And Teacher Registration Api #############
    # For Registaration required filds are 'username', 'password', 'id', 'first_name',
    # 'last_name', 'email', user_type=student or teacher
    path('register/', SignupForStudentOrTeacher.as_view()),


    ######## Login student see his own details only###########
    path('student_details/', StudentDetailsView.as_view()),

    ######## In this api admin do add teacher or student or get the all user list #########
    path('admin_user/', AdminUserView.as_view()),

    ########## In This Api Teacher, add new student and get the list of all student ########
    path('teacher_add_list/', TeacherActionAddListView.as_view()),

    ######## Token api ###########
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ######## Password Reset Api #############
    ############# I'M not use any mail service thats why EMAIL_BACKEND in Setting.py ##########
    path('password_reset/', include('django_rest_passwordreset.urls')),
    path('password_reset/confirm/', include('django_rest_passwordreset.urls')),

]
