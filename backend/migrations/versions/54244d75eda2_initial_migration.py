"""Initial migration

Revision ID: 54244d75eda2
Revises: 
Create Date: 2024-08-24 21:40:48.739447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54244d75eda2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('safety_rating', sa.Integer(), nullable=True),
    sa.Column('use_case', sa.String(length=200), nullable=True),
    sa.Column('environmental_impact', sa.String(length=200), nullable=True),
    sa.Column('code', sa.String(length=20), nullable=True),
    sa.Column('cas_no', sa.String(length=20), nullable=True),
    sa.Column('definition_korean', sa.Text(), nullable=True),
    sa.Column('definition_english', sa.Text(), nullable=True),
    sa.Column('mixing_purpose_korean', sa.Text(), nullable=True),
    sa.Column('mixing_purpose_english', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ingredient')
    # ### end Alembic commands ###
