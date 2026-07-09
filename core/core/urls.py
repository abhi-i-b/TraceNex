from django.contrib import admin
from django.urls import path

from missingperson.views import (
    home,
    detect,
    surveillance,
    register,
    missing,
    video_feed,
    delete_person,
    update_person,
    locations,
    dashboard,
    register_police,
    register_individual
)

from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [

    path('', home, name='home'),

    path('detect/', detect, name='detect'),

    path('surveillance/', surveillance, name='surveillance'),

    path('register/', register, name='register'),

    path('missing/', missing, name='missing'),
    
    path('video_feed/', video_feed, name='video_feed'),

    path(
        'delete/<int:person_id>/',
        delete_person,
        name='delete_person'
    ),

    path(
        'update/<int:person_id>/',
        update_person,
        name='update_person'
    ),

    # New Pages

    path(
        'locations/',
        locations,
        name='locations'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'report/police/',
        register_police,
        name='register_police'
    ),

    path(
        'report/individual/',
        register_individual,
        name='register_individual'
    ),

    path('admin/', admin.site.urls),

]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )