"""empty message

Revision ID: 95f4711ff324
Revises: 1e689b8593d9
Create Date: 2021-03-23 13:48:05.438708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95f4711ff324'
down_revision = '1e689b8593d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('is_tolerant', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plant', 'is_tolerant')
    # ### end Alembic commands ###
