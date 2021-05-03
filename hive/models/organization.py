from logging import getLogger
from uuid import UUID

from sqlalchemy import text

from hive import db

from .mixins import GUID, TimeMixin, now

log = getLogger(__name__)

org_users = db.Table("orgs_users", db.metadata,
                     db.Column("org_id", GUID(), db.ForeignKey("orgs.id"), primary_key=True),
                     db.Column("user_id", GUID(), db.ForeignKey("users.id"), primary_key=True),
                     db.Column("privilege", db.Integer, default=0))


class Organization(TimeMixin, db.Model):
    __tablename__ = 'orgs'
    name = db.Column(db.String, nullable=False, unique=True)

    users = db.relationship("User", secondary="orgs_users", back_populates='organizations')

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return '<Org {}-{}>'.format(self.name, self.id)

    def add_user(self, user, privilege: int):

        query = text(f"select user_id from orgs_users where user_id='{user.id}' and org_id='{self.id}'")
        association = db.session.execute(query).first()
        if association is None:
            log.warning(f"Adding User {user} to Organization {self}")

        insert = org_users.insert().values(user_id=user.id, org_id=self.id, privilege=privilege)
        db.session.execute(insert)
        db.session.commit()

        #user.organizations.append(self)
        #self.users.append(user)

        #user.save()
        #self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
