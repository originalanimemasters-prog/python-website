from django.urls import path

from apps.subscriptions.views import MySubscriptionAPIView

app_name = "subscriptions"

urlpatterns = [
    path(
        "me/",
        MySubscriptionAPIView.as_view(),
        name="my-subscription",
    ),
]