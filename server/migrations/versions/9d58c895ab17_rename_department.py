"""rename department

Revision ID: 9d58c895ab17
Revises: 0de8c00dee75
Create Date: 2024-04-05 14:07:12.686423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d58c895ab17'
down_revision = '0de8c00dee75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###


