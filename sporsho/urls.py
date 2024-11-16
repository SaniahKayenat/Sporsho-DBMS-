
from django.contrib import admin
from django.urls import path
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from entrepreneur import views as entrepreneur_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # ---------------LOGIN---------------
    path('',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    # ------------------ENTREPRENEUR-----------------
    path('entrepreneur/',entrepreneur_views.entrepreneur, name = 'entrepreneur'),
    path('add_entrepreneur/',entrepreneur_views.add_entrepreneur, name = 'add_entrepreneur'),
    path('edit_entrepreneur/<int:id>/',entrepreneur_views.edit_entrepreneur, name ='edit_entrepreneur'),
    path('view_entrepreneur/<int:id>/',entrepreneur_views.view_entrepreneur, name ='view_entrepreneur'),
    path('search/', entrepreneur_views.search, name='search'),
    path('view_entrepreneur/<int:id>/search_entrepreneur_cow',entrepreneur_views.search_entrepreneur_cow,name='search_entrepreneur_cow'),
    #------------------------COW---------------------------

    path('view_entrepreneur/<int:id>/add_cow/',entrepreneur_views.add_cow, name = 'add_cow'),
    path('cow/',entrepreneur_views.cow,name='cow'),
    path('edit_cow/<int:id>/',entrepreneur_views.edit_cow, name ='edit_cow'),
    path('view_cow/<int:id>/',entrepreneur_views.view_cow, name ='view_cow'),
    path('search_cow/', entrepreneur_views.search_cow, name='search_cow'),
    path('update_cow/<int:id>',entrepreneur_views.update_cow , name = 'update_cow')
    ]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





