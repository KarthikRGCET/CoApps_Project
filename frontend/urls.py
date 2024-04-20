from django.urls import path

from frontend.views import home, job_list, about, contact, job_detail

urlpatterns = [

    path('', home, name='home'),
    path('job-list/', job_list, name='job_list'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('job-detail/', job_detail, name='job_detail'),
    path('job/<int:company_detail_id>/', job_detail, name='job_detail'),


]