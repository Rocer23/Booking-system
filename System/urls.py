from django.urls import path
from django.contrib.auth import views as auth_views
from System import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms-list/", views.room_list, name="rooms-list"),
    path("book-room/", views.book_room, name="book-room"),
    path("booking-details/<int:pk>/", views.booking_details, name="booking-details"),
    path('booking-list/', views.booking_list, name="booking-list"),
    path("facilities-list/", views.facilities_list, name="facilities-list"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='booking/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
