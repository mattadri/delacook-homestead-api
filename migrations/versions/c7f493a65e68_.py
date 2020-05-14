"""empty message

Revision ID: c7f493a65e68
Revises: 7e209076b8c4
Create Date: 2020-03-07 13:07:07.642500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7f493a65e68'
down_revision = '7e209076b8c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plants', 'friendly_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plants', 'friendly_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
