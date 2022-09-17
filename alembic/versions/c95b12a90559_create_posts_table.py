"""create posts table

Revision ID: c95b12a90559
Revises: 
Create Date: 2022-09-15 12:14:49.762890

"""
from tkinter.tix import Tree
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c95b12a90559'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
