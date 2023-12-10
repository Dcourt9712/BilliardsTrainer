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
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('map_view/', include("map_view.urls", namespace="map_view")),
    path('', MA_views.welcome, name = 'welcome'),

    #User Profile
    path("profile/", MA_views.profile, name="profile"),
    #Create User account
    path("create/", MA_views.create, name="create"),
    #User Login
    path('login/', MA_views.user_login, name='login'),
    #User Logout
    path('logout/', MA_views.user_logout, name='logout'),

    #PersistantData
    path("<int:id>", MA_views.profile, name="profile"),
    path("create/", MA_views.create, name="create"),
    path('message-board/', MA_views.message_list, name='message_board'),
    path('add-message/', MA_views.add_message, name='add_message'),
    path('message/<int:message_id>/delete/', MA_views.delete_message, name='delete_message'),
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
    path('drills/fundamentals/mightyx_stun', MA_views.mightyx_stun,name ='mightyx_stun'),
    path('drills/fundamentals/mightyx_follow', MA_views.mightyx_follow,name ='mightyx_follow'),
    path('drills/fundamentals/mightyx_draw', MA_views.mightyx_draw,name ='mightyx_draw'),
    
    path('drills/shotmaking/mill', MA_views.mill,name ='mill'),
    path('drills/shotmaking/everest', MA_views.everest,name ='everest'),
    path('drills/shotmaking/ladder', MA_views.ladder,name ='ladder'),
    path('drills/shotmaking/corner', MA_views.corner,name ='corner'),
    path('drills/shotmaking/train', MA_views.train,name ='train'),
    path('drills/shotmaking/follower', MA_views.follower,name ='follower'),

    path('drills/kicking/one_rail_kick', MA_views.one_rail_kick,name ='one_rail_kick'),
    path('drills/kicking/two_rail_kick', MA_views.two_rail_kick,name ='two_rail_kick'),
    path('drills/kicking/three_rail_kick', MA_views.three_rail_kick,name ='three_rail_kick'),
    path('drills/kicking/kicking1', MA_views.kicking1,name ='kicking1'),
    path('drills/kicking/kicking2', MA_views.kicking2,name ='kicking2'),
    path('drills/kicking/kicking3', MA_views.kicking3,name ='kicking3'),

    path('drills/banking/one_rail_bank', MA_views.one_rail_bank,name ='one_rail_bank'),
    path('drills/banking/two_rail_bank', MA_views.two_rail_bank,name ='two_rail_bank'),
    path('drills/banking/three_rail_bank', MA_views.three_rail_bank,name ='three_rail_bank'),
    path('drills/banking/four_rail_bank', MA_views.four_rail_bank,name ='four_rail_bank'),
    path('drills/banking/banking1', MA_views.banking1,name ='banking1'),
    path('drills/banking/banking2', MA_views.banking2,name ='banking2'),

    path('drills/safety/safety1', MA_views.safety1,name ='safety1'),
    path('drills/safety/safety2', MA_views.safety2,name ='safety2'),
    path('drills/safety/safety3', MA_views.safety3,name ='safety3'),
    path('drills/safety/safety4', MA_views.safety4,name ='safety4'),
    path('drills/safety/safety5', MA_views.safety5,name ='safety5'),
    path('drills/safety/safety6', MA_views.safety6,name ='safety6'),

    path('drills/jumping/jumping1', MA_views.jumping1,name ='jumping1'),
    path('drills/jumping/jumping2', MA_views.jumping2,name ='jumping2'),
    path('drills/jumping/jumping3', MA_views.jumping3,name ='jumping3'),
    path('drills/jumping/jumping4', MA_views.jumping4,name ='jumping4'),
    path('drills/jumping/jumping5', MA_views.jumping5,name ='jumping5'),
    path('drills/jumping/jumping6', MA_views.jumping6,name ='jumping6'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
