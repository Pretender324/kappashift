from django.urls import path, include
from .views import KappaLogin, topfunc, MemberView, MemberCreate, MemberUpdate, MemberDelete

urlpatterns = [
    path('login/', KappaLogin.as_view(), name='login'),
    path('', topfunc, name='top'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('member/', MemberView.as_view(), name='member'),
    path('create/', MemberCreate.as_view(), name='create'),
    path('edit/<int:pk>', MemberUpdate.as_view(), name='update'),
    path('delete/<int:pk>', MemberDelete.as_view(), name='delete')
]
