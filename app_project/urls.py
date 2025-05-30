from django.urls import path
from .views import list_view, search_detail_view, detail_list_view, Post_omonim, Post_detail #DetailsApiView


urlpatterns = [
    path('', list_view, name='list'),
    path('details', detail_list_view, name='details'),
    path('search_detail', search_detail_view, name='search_detail'),
    path('post_omonim', Post_omonim.as_view()),
    path('post_detail', Post_detail.as_view())
    # path('checkng/', DetailsApiView.as_view()),
]
