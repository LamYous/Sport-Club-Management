from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('boxing/', views.boxing_page, name="boxing"),
    path('kickboxing/', views.kickboxing_page, name="kickboxing"),
    path('MMA/', views.mma_page, name="MMA"),
    path('fitness/', views.fitness_page, name="fitness"),

    path('member_info/<int:member_id>/', views.member_detail, name="detail"),
    path('create_member/', views.create_member, name="create_member"),
    path('update_member/<int:member_id>/', views.update_member_info, name="update_member"),
    path('delete_member/<int:member_id>/', views.delete_momber, name="delete"),

    path('coachs/', views.coachs_page, name="coachs"),
    path('add_coach/', views.add_coach, name="create_coach"),
    path('update_coach/<int:coach_id>/', views.update_coach, name="update_coach"),
    path('delete_coach/<int:coach_id>/', views.delete_coach, name="delete_coach"),

    path('login/', views.login_page, name='login'),
    path('logout/', views.log_out, name='logout')
]