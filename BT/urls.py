"""BT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app import views as MA_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map_view/', include("map_view.urls", namespace="map_view")),
    path('', MA_views.welcome, name = 'welcome'),

    #PersistantData
    path("<int:id>", MA_views.profile, name="profile"),
    path("create/", MA_views.create, name="create"),
    path('message-board/', MA_views.message_list, name='message_board'),
    path('add-message/', MA_views.add_message, name='add_message'),
    path('message-board/', MA_views.message_list, name='message_list'),

    #Drills
    path('drills/',MA_views.drills,name ='drills'),
    path('drills/Fundamentals', MA_views.Fundamentals,name ='Fundamentals'),
    path('drills/Shotmaking', MA_views.Shotmaking,name ='Shotmaking'),
    path('drills/Kicking', MA_views.Kicking,name ='Kicking'),
    path('drills/Banking', MA_views.Banking,name ='Banking'),
    path('drills/Safety', MA_views.Safety,name ='Safety'),
    path('drills/Jumping', MA_views.Jumping,name ='Jumping'),
    path('drills/fundamentals/stop', MA_views.stop,name ='stop'),
    path('drills/fundamentals/follow', MA_views.follow,name ='follow'),
    path('drills/fundamentals/draw', MA_views.draw,name ='draw'),
    path('drills/shotmaking/mill', MA_views.mill,name ='mill'),
    path('drills/shotmaking/everest', MA_views.everest,name ='everest'),
    path('drills/shotmaking/ladder', MA_views.ladder,name ='ladder'),
    path('drills/shotmaking/corner', MA_views.corner,name ='corner'),
    path('drills/shotmaking/train', MA_views.train,name ='train'),
    path('drills/shotmaking/follower', MA_views.follower,name ='follower')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
