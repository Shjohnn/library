
from django.contrib import admin
from django.urls import path
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('info/', info_view),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('kutubxonachilar/',kutubxonachilar_view, name='kutubxonachilar'),
    path('talabalar/<int:student_id>/', talaba_view),
    path('mualliflar/',mualliflar_view , name='mualliflar'),
    path('kitoblar/',kitoblar_view ,name='kitoblar'),
    path('kitoblar/<int:kitob_id>/',kitob_view),
    path('mualliflar/<int:muallif_id>/',muallif_view),
    path('records/',records_view, name='records'),
    path('recordlar/<int:record_id>/delete/',record_del_view ,name='recordlar'),
    path('talabalar/<int:student_id>/delete/', talaba_del_view),
    path('talabalar/<int:student_id>/update/', talaba_update_view),
    path('kitoblar/<int:kitob_id>/delete/', kitob_del_view),
    path('mualliflar/<int:muallif_id>/delete/', muallif_del_view, name='mualliflar'),
    path('kitoblar/<int:kitob_id>/update/',kitoblar_update_view ),


]
