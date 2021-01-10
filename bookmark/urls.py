from django.urls import path
from .views import *
    
# BookmarkListView, BookmarkCreateView, BookmarkDetailView 다쓰기 싫어서 별로 바꿈

urlpatterns = [
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>", BookmarkDeleteView.as_view(), name='delete'),
]

# url을 list로 불러다 쓸 것이라는 말임
# <ink:pk>은 detail뒤에 해당북마트 글번호를 찾아내서 여기에 쓰면 보여주겠다는 뜻 
# PK는 Primary key를 나타냄