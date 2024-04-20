from django.urls import path

from backend.views import Dashboard, CountryList, CountryUpdate, CountryCreate, CountryDelete, StateList, StateCreate, \
    StateUpdate, StateDelete, CityList, CityCreate, CityUpdate, CityDelete, Job_categoryCreate, Job_categoryList, \
    Job_categoryUpdate, Job_categoryDelete, Company_detailsList, Company_detailsCreate, Company_detailsUpdate, \
    Company_detailsDelete, Job_applyList, Job_applyCreate, Job_applyDelete, Job_applyUpdate, job_apply_count_month_wise

urlpatterns = [
    # dashboard
    path('', Dashboard.as_view(), name="dashboard"),

    # country
    path('country/', CountryList.as_view(), name='country_list'),
    path('country/create/', CountryCreate.as_view(), name='country_create'),
    path('country/update/<pk>/', CountryUpdate.as_view(), name='country_update'),
    path('country/delete/<pk>/', CountryDelete.as_view(), name='country_delete'),

    # state
    path('state/', StateList.as_view(), name='state_list'),
    path('state/create/', StateCreate.as_view(), name='state_create'),
    path('state/update/<pk>/', StateUpdate.as_view(), name='state_update'),
    path('state/delete/<pk>/', StateDelete.as_view(), name='state_delete'),

    # city
    path('city/', CityList.as_view(), name='city_list'),
    path('city/create/', CityCreate.as_view(), name='city_create'),
    path('city/update/<pk>/', CityUpdate.as_view(), name='city_update'),
    path('city/delete/<pk>/', CityDelete.as_view(), name='city_delete'),

    # Job_Category
    path('job_category/', Job_categoryList.as_view(), name='job_category_list'),
    path('job_category/create/', Job_categoryCreate.as_view(), name='job_category_create'),
    path('job_category/update/<pk>/', Job_categoryUpdate.as_view(), name='job_category_update'),
    path('job_category/delete/<pk>/', Job_categoryDelete.as_view(), name='job_category_delete'),

    # company
    path('company_details/', Company_detailsList.as_view(), name='company_details_list'),
    path('company_details/create/', Company_detailsCreate.as_view(), name='company_details_create'),
    path('company_details/update/<pk>/', Company_detailsUpdate.as_view(), name='company_details_update'),
    path('company_details/delete/<pk>/', Company_detailsDelete.as_view(), name='company_details_delete'),

    # job_apply
    path('job_apply/', Job_applyList.as_view(), name='job_apply_list'),
    path('job_apply/create/', Job_applyCreate.as_view(), name='job_apply_create'),
    path('job_apply/update/<pk>/', Job_applyUpdate.as_view(), name='job_apply_update'),
    path('job_apply/delete/<pk>/', Job_applyDelete.as_view(), name='job_apply_delete'),

    path('job-apply-count-month-wise/', job_apply_count_month_wise, name='job_apply_count_month_wise'),

]