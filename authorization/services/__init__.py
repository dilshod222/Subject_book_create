from django.contrib.auth.models import User
from django.db import transaction

from authorization.forms import RegisterForm
# from authorization.models import Employe

from uploads_app.utils import write_file


@transaction.atomic
def save_user(form: RegisterForm):
    user = User()
    data = form.cleaned_data
    user.username = data.get('username')
    user.email = data.get('email')
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.is_active = 1
    user.is_superuser = 0
    user.set_password(raw_password=data.get('password'))
    user.save()
    # employee = Employe()
    # employee.user = user
    # employee.picture = write_file(data.get('picture'))
    # employee.save()

def taken_username(username: str) -> bool:
    return User.objects.filter(username=username).exists()
