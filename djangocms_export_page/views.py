from cms.models import Page
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.utils.translation import get_language
from django.views.generic import View

from .constants import DOCX, FILE_FORMATS
from .export import export_page


class PageExportView(View):
    response_class = HttpResponse
    file_format = FILE_FORMATS[DOCX]

    def get(self, request, *args, **kwargs):
        self.page = get_object_or_404(Page, pk=kwargs.pop('page_pk'))
        self.language = get_language()
        self.file_format = FILE_FORMATS.get(kwargs.pop('file_format'))
        return self.render_to_response()

    def render_to_response(self):
        export_file = export_page(self.page, self.language, self.file_format)
        content_type = self.file_format.content_type

        response = self.response_class(export_file, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            self.get_file_name()
        )
        return response

    def get_file_name(self):
        title = self.page.get_title(language=self.language)

        return '{name}_{lang}.{ext}'.format(
            name=slugify(title),
            lang=self.language,
            ext=self.file_format.ext,
        )
