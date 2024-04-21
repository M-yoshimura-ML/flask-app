"""Modifying Post model

Revision ID: ea1ae4cab3ee
Revises: d67fbd10f39f
Create Date: 2024-04-21 19:39:46.364362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ea1ae4cab3ee'
down_revision = 'd67fbd10f39f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('slug', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('body',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=120),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=120),
               existing_nullable=False)
        batch_op.drop_column('updated_at')
        batch_op.drop_column('slug')
        batch_op.drop_column('author')

    # ### end Alembic commands ###
