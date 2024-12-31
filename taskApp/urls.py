from django.urls import path
from taskApp import views

urlpatterns=[
    path('url',views.addtask,name='addtask'),
    path('url',views.updatetask,name="udatetask"),
    path('url',views.deletetask,name="deletetask"),
    path('url',views.loginpage,name="loginpage"),
    path('url',views.logout,name="logoutpage"),
    path('url',views.register,name="register"),
    path('url',views.updatetask,name="udatetask"),
    path('url',views.task_list,name="tasklist"),
    path('url',views.search_tasks,name="search_tasks"),
    path('url',views.change_password,name="change_password"),
    path('url',views.aboutus,name="aboutus"),
    
]