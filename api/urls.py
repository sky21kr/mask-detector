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
    path('mask-history', views.maskHistory, name='maskHistory'),
    path('is-with-mask', views.maskHistory, name='isWithMask'),
    # path('main/', include(main_patterns)),
]