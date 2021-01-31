"""empty message

Revision ID: ac8f2dd5fd1e
Revises: 42e955648e47
Create Date: 2021-01-25 15:00:37.919863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac8f2dd5fd1e'
down_revision = '42e955648e47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plant_child_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_child_fk', sa.Integer(), nullable=True),
    sa.Column('note_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['note_fk'], ['note.id'], ),
    sa.ForeignKeyConstraint(['plant_child_fk'], ['plant_child.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plant_child_propagation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('propagation', sa.Text(), nullable=True),
    sa.Column('plant_child_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_child_fk'], ['plant_child.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plant_child_season',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_child_fk', sa.Integer(), nullable=True),
    sa.Column('season_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_child_fk'], ['plant_child.id'], ),
    sa.ForeignKeyConstraint(['season_fk'], ['season.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plant_child_use',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_child_fk', sa.Integer(), nullable=True),
    sa.Column('use_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_child_fk'], ['plant_child.id'], ),
    sa.ForeignKeyConstraint(['use_fk'], ['use.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plant_child_water_requirement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_child_fk', sa.Integer(), nullable=True),
    sa.Column('water_child_requirement_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_child_fk'], ['plant_child.id'], ),
    sa.ForeignKeyConstraint(['water_child_requirement_fk'], ['water_requirement.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plant_child_light_requirement_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_child_light_requirement_fk', sa.Integer(), nullable=True),
    sa.Column('note_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['note_fk'], ['note.id'], ),
    sa.ForeignKeyConstraint(['plant_child_light_requirement_fk'], ['plant_child_light_requirement.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plant_child_water_requirement_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_child_water_requirement_fk', sa.Integer(), nullable=True),
    sa.Column('note_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['note_fk'], ['note.id'], ),
    sa.ForeignKeyConstraint(['plant_child_water_requirement_fk'], ['plant_child_water_requirement.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plant_child_water_requirement_note')
    op.drop_table('plant_child_light_requirement_note')
    op.drop_table('plant_child_water_requirement')
    op.drop_table('plant_child_use')
    op.drop_table('plant_child_season')
    op.drop_table('plant_child_propagation')
    op.drop_table('plant_child_note')
    # ### end Alembic commands ###
