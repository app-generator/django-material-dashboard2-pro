from django.urls import path
from admin_material2_pro import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Dashboard
    path('', views.analytics, name="index"),
    path('discover/', views.discover, name="discover"),
    path('sales/', views.sales, name="sales"),
    path('automotive/', views.automotive, name="automotive"),
    path('smart-home/', views.smart_home, name="smart_home"),

    # Pages -> Profile
    path('pages/profile/profile-overview/', views.profile_overview, name="profile_overview"),
    path('pages/profile/projects/', views.all_projects, name="projects"),
    path('pages/profile/messages/', views.messages, name="messages"),
    # Pages -> Users
    path('pages/users/reports/', views.reports, name="reports"),
    path('pages/users/new-user/', views.new_user, name="new_user"),
    # Pages -> Accounts
    path('pages/accounts/settings/', views.settings, name="settings"),
    path('pages/accounts/billing/', views.billing, name="billing"),
    path('pages/accounts/invoice/', views.invoice, name="invoice"),
    path('pages/accounts/security/', views.security, name="security"),
    # Pages -> Projects
    path('pages/projects/general/', views.general, name="general"),
    path('pages/projects/timeline/', views.timeline, name="timeline"),
    path('pages/projects/new-project/', views.new_project, name="new_project"),
    # Pages -> VR
    path('pages/vr/vr-default/', views.vr_default, name="vr_default"),
    path('pages/vr/vr-info/', views.vr_info, name="vr_info"),
    # Pages
    path('pages/rtl/', views.rtl, name="rtl"),
    path('pages/pricing/', views.pricing, name="pricing"),
    path('pages/widgets/', views.widgets, name="widgets"),
    path('pages/charts/', views.charts, name="charts"),
    path('pages/sweet-alerts/', views.sweet_alerts, name="sweet_alerts"),
    path('pages/notifications/', views.notifications, name="notifications"),
    
    # Applications
    path('applications/crm/', views.crm, name="crm"),   
    path('applications/kanban/', views.kanban, name="kanban"),   
    path('applications/wizard/', views.wizard, name="wizard"),   
    path('applications/datatables/', views.datatables, name="datatables"),   
    path('applications/calendar/', views.calendar, name="calendar"),   
    path('applications/stats/', views.stats, name="stats"), 

    # Ecommerce -> Products
    path('ecommerce/products/new-product/', views.new_product, name="new_product"),  
    path('ecommerce/products/edit-product/', views.edit_product, name="edit_product"),  
    path('ecommerce/products/product-page/', views.product_page, name="product_page"),  
    path('ecommerce/products/products-list/', views.products_list, name="products_list"),  
    # Ecommerce -> Orders
    path('ecommerce/orders/list/', views.order_list, name="order_list"),  
    path('ecommerce/orders/details/', views.order_details, name="order_details"), 
    # Ecommerce -> Referral
    path('ecommerce/referral/', views.referral, name="referral"),  

    # Authentication -> Login
    path('accounts/basic-login/', views.BasicLoginView.as_view(), name="basic_login"),
    path('accounts/cover-login/', views.CoverLoginView.as_view(), name="cover_login"),
    path('accounts/illustration-login/', views.IllustrationLoginView.as_view(), name="illustration_login"),

    # Authentication -> Register
    path('accounts/basic-register/', views.basic_register, name="basic_register"),
    path('accounts/cover-register/', views.cover_register, name="cover_register"),
    path('accounts/illustration-register/', views.illustration_register, name="illustration_register"),

    # Authentication -> Reset
    path('accounts/basic-reset/', views.BasicPasswordResetView.as_view(), name="basic_reset"),
    path('accounts/cover-reset/', views.CoverPasswordResetView.as_view(), name="cover_reset"),
    path('accounts/illustration-reset/', views.IllustrationPasswordResetView.as_view(), name="illustration_reset"),

    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/done/change-done.html'
    ), name="password_change_done"),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/done/basic.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/complete/basic.html'
    ), name='password_reset_complete'),

    # Authentication -> Verification
    path('accounts/basic-verification/', views.basic_verification, name="basic_verification"),
    path('accounts/cover-verification/', views.cover_verification, name="cover_verification"),
    path('accounts/illustration-verification/', views.illustration_verification, name="illustration_verification"),

    # Authentication -> Lock
    path('accounts/basic-lock/', views.basic_lock, name="basic_lock"),
    path('accounts/cover-lock/', views.cover_lock, name="cover_lock"),
    path('accounts/illustration-lock/', views.illustration_lock, name="illustration_lock"),

    # Error
    path('error/404/', views.error_404, name="error_404"),
    path('error/500/', views.error_500, name="error_500"),

    # Logout
    path('accounts/logout/', views.logout_view, name='logout'),
]

