from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationView
from .views import ChecklistItemViewSet

router = DefaultRouter()
router.register(r'checklist-items', ChecklistItemViewSet)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('api/', include(router.urls)),
]
