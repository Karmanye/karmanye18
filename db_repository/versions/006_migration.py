from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
buyer = Table('buyer', post_meta,
    Column('bid', Integer, primary_key=True, nullable=False),
    Column('bfname', String(length=50)),
    Column('blname', String(length=50)),
    Column('bemail', String(length=100)),
    Column('bmobile', String(length=50)),
    Column('bstate', String(length=50)),
    Column('bcountry', String(length=50)),
    Column('timestamp', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buyer'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buyer'].drop()
