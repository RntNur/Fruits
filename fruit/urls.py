from django.urls import path

from fruit.views import *

urlpatterns = [
    path('', index_template, name = 'index_Fruit'),
    path('login/', user_login, name='log in'),
    path('httpresponse/', index),

    path('fruitslist/', FruitsList.as_view(), name = 'list_fruit'),
    path('list/<int:pk>/', FruitsDetail.as_view(), name = 'one_fruit'),
    path('list/<int:pk>/edit', FruitsUpdate.as_view(), name = 'fruit_edit'),
    path('add/', FruitsAdd.as_view(), name = 'add_fruit'),

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

    path('logout/', user_logout, name='log out'),

    path('email/', contact_email, name='contact_email'),

    path('api/list/', fruit_api_list, name='fruit_api_list'),
    path('api/detail/<int:pk>', fruit_api_detail, name='fruit_api_detail'),
]
