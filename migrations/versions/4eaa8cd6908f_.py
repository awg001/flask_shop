"""empty message

Revision ID: 4eaa8cd6908f
Revises: 16417b3aaa7d
Create Date: 2021-11-20 11:16:03.405465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eaa8cd6908f'
down_revision = '16417b3aaa7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emal', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('isAdmin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('emal'),
    sa.UniqueConstraint('password')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
