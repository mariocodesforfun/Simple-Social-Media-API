"""add user table

Revision ID: 29da8adb353b
Revises: f7ab3a0ffe88
Create Date: 2022-09-16 09:39:40.834790

"""
from xmlrpc.client import NOT_WELLFORMED_ERROR
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29da8adb353b'
down_revision = 'f7ab3a0ffe88'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('email', sa.String, nullable=False),
                sa.Column('password', sa.String(), nullable=False),
                sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                server_default=sa.text('now()'), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('email')
                )
    pass


def downgrade():
    op.drop_table('users')
    pass
