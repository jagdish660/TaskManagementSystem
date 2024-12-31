from django.contrib import admin
from django.urls import path
from taskApp.views import addtask,task_list,deletetask,updatetask,register,aboutus,loginpage,logoutpage,task_detail,search_tasks,change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addtask/',addtask,name='addtask'),
    path('',task_list,name='tasklist'),
    path('deletetask/<int:id>/', deletetask, name='deletetask'),
    path('updatetask/<int:id>/', updatetask, name='updatetask'),
    path('register/', register, name='register'),
    path('accounts/login/', loginpage, name='loginpage'),
    path('logout/', logoutpage, name='logoutpage'),
    path('search_tasks/',search_tasks,name='search_tasks'),
    path('change_password/',change_password,name='change_password'),
    path('task_detail/<int:id>',task_detail,name='task_detail'),
    path('aboutus/',aboutus,name='aboutus'),
]
