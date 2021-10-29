from rest_framework import routers
from core import views

app_name = 'core'

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('answers', views.AnswerViewSet)

urlpatterns = router.urls