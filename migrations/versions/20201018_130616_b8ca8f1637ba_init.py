"""

Message: init
Revision ID: b8ca8f1637ba
Revises: 
Create Date: 2020-10-18 13:06:16.792679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8ca8f1637ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('password', sa.String(length=60), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'todo_lists',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('owner', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['owner'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('todolist', sa.Integer(), nullable=False),
        sa.Column('value', sa.String(length=100), nullable=False),
        sa.Column('status', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ['todolist'],
            ['todo_lists.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('todo_lists')
    op.drop_table('users')
    # ### end Alembic commands ###
