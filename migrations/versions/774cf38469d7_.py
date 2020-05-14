"""empty message

Revision ID: 774cf38469d7
Revises: b8f8de0c1f59
Create Date: 2020-03-07 12:43:54.247573

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '774cf38469d7'
down_revision = 'b8f8de0c1f59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rainfalltotals')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rainfalltotals',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('amount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='rainfalltotals_pkey')
    )
    # ### end Alembic commands ###
