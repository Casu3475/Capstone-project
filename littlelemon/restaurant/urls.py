# from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
]
