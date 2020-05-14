"""empty message

Revision ID: a180a7417fa9
Revises: c7f493a65e68
Create Date: 2020-03-07 13:07:36.939566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a180a7417fa9'
down_revision = 'c7f493a65e68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plants', sa.Column('common_name', sa.String(), nullable=True))
    op.drop_column('plants', 'friendly_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plants', sa.Column('friendly_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('plants', 'common_name')
    # ### end Alembic commands ###