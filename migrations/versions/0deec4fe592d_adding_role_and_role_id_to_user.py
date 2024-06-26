"""Adding Role and role_id to User

Revision ID: 0deec4fe592d
Revises: 
Create Date: 2024-05-19 20:34:07.648704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0deec4fe592d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'role', ['role_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('role_id')

    # ### end Alembic commands ###
