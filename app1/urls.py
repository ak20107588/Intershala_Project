from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.login),
   path('dashboard',views.dashboard),
   path('doctor',views.doctor),
   path('messages',views.messages1),
   path('signup',views.signup_detail),
   path('login_detail',views.login_detail),
   path('logout',views.logout),
   path('navbar',views.navbar),
   path('base',views.base),
   path('blog',views.blog),
   path('allblogs',views.allblogs),
   path('nodata',views.nodata),
   path('blogdata',views.NewBlog),
   path('blogdetail/<int:id>',views.blogdetail),
   path('draftblog',views.draftblog),
   path('patientdetail',views.patientdetail),
   path('post_list',views.post_list),
   path('filter_items',views.filter_items)
   
  
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                                 document_root=settings.MEDIA_ROOT)

