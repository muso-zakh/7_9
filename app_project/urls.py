from django.urls import path
from .views import (list_view, detail_id_view,
                    search_category_view, detail_list_view,
                    create_category_view, create_term_view,
                    detail_ordering)


urlpatterns = [
    path('', list_view, name='list'),
    path('details', detail_list_view, name='details'),
    path('search_detail', search_category_view, name='search_detail'),
    path('post_category', create_category_view),
    path('post_detail', create_term_view),
    path('detail_view/<int:pk>/', detail_id_view),
    path('detail_ordering', detail_ordering),
    # path('checkng/', DetailsApiView.as_view()),
]
