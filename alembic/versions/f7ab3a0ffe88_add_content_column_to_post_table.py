"""add content column to post table

Revision ID: f7ab3a0ffe88
Revises: c95b12a90559
Create Date: 2022-09-16 09:33:41.580107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7ab3a0ffe88'
down_revision = 'c95b12a90559'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
