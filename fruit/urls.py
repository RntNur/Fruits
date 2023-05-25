from django.urls import path

from fruit.views import *

urlpatterns = [
    path('', index_template, name='index_Fruit'),
    path('list/', fruit_template, name='list_fruit'),
    path('httpresponse/', index),
    path('add/', fruit_add, name='add_fruit'),
    path('list/<int:fruit_id>/', fruit_detail, name='one_fruit'),

    # Supplier
    path('supplier/list/', supplier_list, name='list_supp'),
    path('supplier/add/', supplier_form, name='add_supp'),
    # Supplier class View
    # LISTVIEW
    path('supplier/view/list/', SupplierListView.as_view(), name='list_supp_view'),

    # Ключ supplier_id после переопределения атрибута pk_url_kwarg в SupplierDetailView (DetailView)
    path('supplier/view/<int:supplier_id>', SupplierDetailView.as_view(), name='info_supp_view'),
    # CREATEVIEW
    path('supplier/view/add/', SupplierCreateView.as_view(), name='add_supp_view'),
    # UPDATEVIEW
    path('supplier/view/edit/<int:pk>', SupplierUpdateView.as_view(), name='edit_supp_view'),
    # DELETEVIEW
    path('supplier/view/del/<int:pk>', SupplierDeleteView.as_view(), name='del_supp_view'),

    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),

    path('email/', contact_email, name='contact_email'),

    path('api/list/', fruit_api_list, name='fruit_api_list'),
    path('api/detail/<int:pk>', fruit_api_detail, name='fruit_api_detail'),
]
