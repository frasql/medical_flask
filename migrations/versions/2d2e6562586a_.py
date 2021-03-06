"""empty message

Revision ID: 2d2e6562586a
Revises: 414435e9d35c
Create Date: 2021-03-29 19:13:06.115247

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d2e6562586a'
down_revision = '414435e9d35c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('roles', 'name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_index('name', table_name='roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'roles', ['name'], unique=True)
    op.alter_column('roles', 'name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###
