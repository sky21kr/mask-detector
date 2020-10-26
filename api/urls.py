from django.urls import path, include
from . import views
# /main 으로 시작하는 하위 url 설정
#main_patterns = [
#    path('',main_views.main),
#    path('signup/', main_views.signup, name='signup'),
#    path('signin/', main_views.signin, name='signin'),
#]

# 변수로 설정한 값을 include함.
urlpatterns = [
    path('article/get-list', views.getArticle, name='getArticle'),
    # path('main/', include(main_patterns)),
]