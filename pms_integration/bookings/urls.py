from django.urls import path
from .views import PMSBookingsView

urlpatterns = [
    path("api/integrations/pms/bookings/", PMSBookingsView.as_view()),
]