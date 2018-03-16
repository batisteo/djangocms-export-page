from collections import namedtuple

FileFormat = namedtuple('FileFormat', ['name', 'ext', 'content_type'])

DOCX = 'docx'
DOCX_CONTENT_TYPE = (
    'application/vnd'
    '.openxmlformats-officedocument.wordprocessingml.document'
)

FILE_FORMATS = {
    DOCX: FileFormat(DOCX, ext='docx', content_type=DOCX_CONTENT_TYPE),
}
