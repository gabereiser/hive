from typing import List, Any

from flask import render_template_string
from flask_mail import Message

import re

from hive import mail
from hive.config import Config

regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"


def validate(email):
    return re.search(regex, email)


def send_email(emails: List, subject: str, template_name: str, context: Any):
    with mail.connect() as conn:
        for email in emails:
            msg = Message(html=render_template_string(template_name, context=context),
                          recipients=[email],
                          sender=Config.SUPPORT_EMAIL,
                          subject=subject)
            msg.send(conn)
