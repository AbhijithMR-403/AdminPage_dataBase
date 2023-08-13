from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.user_log_in_page,name='user_log_in_page'),
    path('sign_up/',views.user_sign_up_page,name='user_sign_up_page'),
    path('home/',views.user_home_page,name='home'),
    path('feature/',views.user_feature_page,name='feature'),
    path('price/',views.user_price_page,name='price'),
    path('logout/',views.user_log_out,name='logout'),
    path('logout_admin/',views.admin_log_out,name='admin_logout'),
    path('adminlog/',views.admin_login_page,name='admin_log_in_page'),
    path('admin_home/',views.admin_home_page,name='admin_home'),
    path('delete/<int:row_id>/', views.delete_row, name='delete_row'),
    path('edit/<int:row_id>/', views.admin_edit, name='edit_row'),
    path('edit_submit/<int:row_id>/', views.admin_edit_submit, name='edit_submit_row'),
    path("admin_search/",views.admin_search,name="admin_search")
]
