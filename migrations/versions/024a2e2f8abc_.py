"""empty message

Revision ID: 024a2e2f8abc
Revises: 6eab96b714c1
Create Date: 2021-10-16 13:40:38.514903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '024a2e2f8abc'
down_revision = '6eab96b714c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'pasien', 'user', ['id_user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pasien', type_='foreignkey')
    # ### end Alembic commands ###