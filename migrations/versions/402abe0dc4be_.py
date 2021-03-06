"""empty message

Revision ID: 402abe0dc4be
Revises: 774cf38469d7
Create Date: 2020-03-07 12:45:12.201550

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '402abe0dc4be'
down_revision = '774cf38469d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('compostpilehistories')
    op.drop_table('compostpiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('compostpiles',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('compostpiles_id_seq'::regclass)"), nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('finished', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('label', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('started', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='compostpiles_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('compostpilehistories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('compost_pile_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('temperature', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('moisture', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('turned', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('scraps_added', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['compost_pile_fk'], ['compostpiles.id'], name='compostpilehistories_compost_pile_fk_fkey'),
    sa.PrimaryKeyConstraint('id', name='compostpilehistories_pkey')
    )
    # ### end Alembic commands ###
