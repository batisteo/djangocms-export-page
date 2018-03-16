from django.conf.urls import url

from .constants import DOCX, FILE_FORMATS
from .views import PageExportView

app_name = 'export-page'

urlpatterns = [
    url(r'^(?P<page_pk>\d+)/(?P<file_format>\w+)/$', PageExportView.as_view(), name='export'),
]
