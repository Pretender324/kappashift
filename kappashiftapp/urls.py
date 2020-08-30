from django.urls import path, include
from .views import KappaLogin, topfunc, MemberView

urlpatterns = [
    path('login/', KappaLogin.as_view(), name='login'),
    path('', topfunc, name='top'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('member/', MemberView.as_view(), name='member')
]
