from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from .constants import FILE_FORMATS


@toolbar_pool.register
class PollToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu('export-page', _('Export'))
        page = self.request.current_page

        for file_format in FILE_FORMATS.values():
            url = reverse('export-page:export', kwargs={
                'page_pk': page.pk,
                'file_format': file_format.name,
            })
            label = _('Export to .{ext}').format(ext=file_format.ext)
            menu.add_link_item(label, url=url)
