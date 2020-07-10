from wtforms import Form, StringField, TextAreaField, validators
from wtforms import IntegerField
from wtforms.widgets import HiddenInput
from wtforms import IntegerField, PasswordField


def strip_filter(x): return x.strip() if x else None


class BlogCreateForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    body = TextAreaField('Contents', [validators.Length(min=1)],
                         filters=[strip_filter])


class BlogUpdateForm(BlogCreateForm):
    id = IntegerField(widget=HiddenInput())


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=255)],
                           filters=[strip_filter])
    password = PasswordField('Password', [validators.Length(min=3)])
