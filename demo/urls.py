from django.conf.urls import url
from django.contrib import admin

from example_app_celery.views import FakeSendMailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', FakeSendMailView.as_view()),
]
