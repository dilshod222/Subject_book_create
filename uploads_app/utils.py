from time import time_ns
from uuid import uuid4
from os.path import join as join_path

from subject_book.settings import MEDIA_ROOT



def uploads_url_with_instance(obj, name: str):
    return uploads_url(name)


def uploads_url(name: str):
    ext: str = name.split('.')[-1]
    return "{0}.{1}".format(str(time_ns())[:9], ext)


def gen_uuid():
    return str(uuid4()).replace("-", "")


def write_file(f):
    new_name = uploads_url(f.name)
    from uploads_app.models import Uploads
    with open(join_path(MEDIA_ROOT, 'upload', new_name), mode="wb+") as file:
        for chunk in f.chunks():
            file.write(chunk)

    file = Uploads(
        media_url=f'media/upload/{new_name}',
        original_name=f.name,
        content_type=f.content_type,
        size=f.size,
        generated_name=new_name,
        code=gen_uuid()
    )
    file.save()
    return file
