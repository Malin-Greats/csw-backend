from email.mime import base
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

from django.urls import path

from .serializers import CswSerializer
# from csw import views
from . import views
from django.contrib.auth import views as auth_view
from .views import *

router = DefaultRouter()
router.register(r'csw_list', CswList)
router.register(r'csw_detail', CswDetail)
router.register(r'work_contactList', Work_contactList)
router.register(r'work_contactDetail', Work_contactDetail)
router.register(r'member_list', CustomerList)
router.register(r'member_detail', CustomerDetail)
router.register(r'education_and_trainingList', education_and_trainingList)
router.register(r'education_and_trainingDetail', education_and_trainingDetail)
router.register(r'pst_five_workList', pst_five_workList)
router.register(r'pst_five_workDetail', pst_five_workDetail)
router.register(r'practise_outsideList', practise_outsideList)
router.register(r'practise_outsideDetail', practise_outsideDetail)
router.register(r'character_refList', character_refList)
router.register(r'character_refDetail', character_refDetail)
router.register(r'rivate_practiceList', rivate_practiceList)
router.register(r'rivate_practiceDetail', rivate_practiceDetail)
router.register(r'user_list', UserList)
router.register(r'user_detail', UserDetail)


schema_view = get_schema_view(
    openapi.Info(
        title='Council of Social Workers Portal API',
        default_version='v1',
        description='RESTFUL API for Council of Social Workers Portal',
        contact=openapi.Contact(email=settings.FROM_EMAIL),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=[AllowAny]
)
urlpatterns = [
    # serializers
    path('Person/', CswList.as_view()),
    path('Person/', CswDetail.as_view()),
    path('Work_contact1/', Work_contactList.as_view()),
    path('Work_contact1/', Work_contactDetail.as_view()),
    path('Contact/', CustomerList.as_view()),
    path('Contact/', CustomerDetail.as_view()),
    path('education_and_training/', education_and_trainingList.as_view()),
    path('education_and_training/', education_and_trainingDetail.as_view()),
    path('pst_five_work/', pst_five_workList.as_view()),
    path('pst_five_work/', pst_five_workDetail.as_view()),
    path('practise_outside/', practise_outsideList.as_view()),
    path('practise_outside/', practise_outsideDetail.as_view()),
    path('character_ref/', character_refList.as_view()),
    path('character_ref/', character_refDetail.as_view()),
    path('rivate_practice/', rivate_practiceList.as_view()),
    path('rivate_practice/', rivate_practiceDetail.as_view()),
    path('User/', UserList.as_view()),
    path('User/', UserDetail.as_view()),
    path('browsable-api-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    # path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
   
]
