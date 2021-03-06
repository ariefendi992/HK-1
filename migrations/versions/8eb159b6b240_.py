"""empty message

Revision ID: 8eb159b6b240
Revises: ae62025a3cf8
Create Date: 2021-10-30 12:39:23.668266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eb159b6b240'
down_revision = 'ae62025a3cf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_antrian',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tanggal', sa.Date(), nullable=True),
    sa.Column('no_antrian', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('1', '0'), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'antrianp', 'pasien', ['id_pasien'], ['id'])
    op.create_foreign_key(None, 'antrianp', 'poli', ['id_poli'], ['id_poli'])
    op.create_foreign_key(None, 'pasien', 'user', ['id_user'], ['id'])
    op.create_foreign_key(None, 'pasien', 'gender', ['id_jk_p'], ['id'])
    op.add_column('user', sa.Column('status', sa.Enum('1', '0'), nullable=True))
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'status')
    op.drop_constraint(None, 'pasien', type_='foreignkey')
    op.drop_constraint(None, 'pasien', type_='foreignkey')
    op.drop_constraint(None, 'antrianp', type_='foreignkey')
    op.drop_constraint(None, 'antrianp', type_='foreignkey')
    op.drop_table('tbl_antrian')
    # ### end Alembic commands ###
