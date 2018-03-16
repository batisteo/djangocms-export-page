from collections import defaultdict

from django.db.models.fields import CharField, TextField

from ..constants import DOCX
from .docx import export_to_docx

export_to = {
    DOCX: export_to_docx,
}


def export_page(page, language, file_format):
    fields = defaultdict(dict)

    for ph in page.get_placeholders():
        for plugin in ph.get_plugins(language):
            instance, cls = plugin.get_plugin_instance()
            fields[ph][instance] = get_fields(instance)

    return export_to[file_format.name](fields)


def get_fields(instance):
    custom_fields = get_custom_fields(instance)
    return {field.name: field for field in custom_fields}


def get_custom_fields(instance):
    base_fields = get_base_fields(instance)
    fields = (f for f in instance._meta.fields if f.name not in base_fields)
    return filtered_fields(fields)


def filtered_fields(fields):
    return (
        f for f in fields
        if isinstance(f, (CharField, TextField))
    )


def get_base_fields(instance):
    for field in instance.cmsplugin_ptr._meta.fields:
        yield field.name
    yield 'cmsplugin_ptr'
