"""

Message: null_user
Revision ID: 19aa1dbf7917
Revises: b8ca8f1637ba
Create Date: 2020-10-18 13:34:28.088180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19aa1dbf7917'
down_revision = 'b8ca8f1637ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo_lists', schema=None) as batch_op:
        batch_op.alter_column('owner', existing_type=sa.INTEGER(), nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo_lists', schema=None) as batch_op:
        batch_op.alter_column('owner', existing_type=sa.INTEGER(), nullable=False)

    # ### end Alembic commands ###
