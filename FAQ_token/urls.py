from django.contrib import admin
from django.urls import path, include
from FAQ_model import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('api/', TemplateView.as_view(template_name="api.html")),
    path('FAQ_model/faqtest/', views.FaqData.as_view()),
    path('FAQ_model/faqtest/<int:pk>', views.FaqDataDetail.as_view()),
]

