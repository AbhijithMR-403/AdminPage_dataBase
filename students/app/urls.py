from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.user_log_in_page,name='user_log_in_page'),
    path('sign_up/',views.user_sign_up_page,name='user_sign_up_page'),
    path('home/',views.user_home_page,name='home'),
    path('feature/',views.user_feature_page,name='feature'),
    path('price/',views.user_price_page,name='price'),
]
