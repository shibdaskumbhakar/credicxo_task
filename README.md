# credicxo_task


I am not done any admin user registration api because everyone register as a admin then everyone get the permission of all system.

############ Student And Teacher Registration Api 

For Registaration required filds are username, password, first_name,last_name,email, user_type=student or teacher

http://127.0.0.1:8000/api/register/
{   "username":"myusername",
    "password":"mypassword",
    "email":"myemail@email.com",
    "user_type":"student or teacher",
    .........
}

######## Login student see his own details only###########
if u login as a student then u only get the result
http://127.0.0.1:8000/api/student_details/

######## In this api admin do add teacher or student or get the all user list #########
if u login as a admin then you able to do add teacher or student and get the list of all user
http://127.0.0.1:8000/api/admin_user/

########## In This Api Teacher, add new student and get the list of all student ########
if u login using teacher id then you eligible to do action
http://127.0.0.1:8000/api/teacher_add_list/

######## Token api ###########
http://127.0.0.1:8000/api/token/
http://127.0.0.1:8000/api/token/refresh/

######## Password Reset Api #############
http://127.0.0.1:8000/api/password_reset/
send post request with your register email
then you get a token in terminal
like /api/password_reset/?token=67843jbxnve80fecxmn05e5ca9fc74799213f81a093d1f
Now copy that token which comes in email and and post token and password to /api/password_reset/confirm/ api url.

{
    "token":"67843jbxnve80fecxmn05e5ca9fc74799213f81a093d1f",
    "password":"mypassword"
}
