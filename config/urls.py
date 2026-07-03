from django.contrib import admin
from django.urls import path
from reports.views import report, login_view, logout_view, save_report, view_reports, edit_report, delete_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', report, name='report'),
    path('save-report/', save_report, name='save_report'),
    path('reports/', view_reports, name='view_reports'),
    path('edit-report/<int:report_id>/', edit_report, name='edit_report'),
    path('delete-report/<int:report_id>/', delete_report, name='delete_report'),
]