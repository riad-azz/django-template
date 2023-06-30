from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("contact/messages", views.ContactListView.as_view(), name="contact_list"),
    path("contact/contact-success", views.ContactSentView.as_view(), name="contact_success"),
    path("policies/", views.PolicyListView.as_view(), name="policy_list"),
    path("policies/<slug:slug>/", views.PolicyDetailView.as_view(), name="policy_detail"),
]
