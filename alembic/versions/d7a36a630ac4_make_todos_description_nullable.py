"""make todos description nullable

Revision ID: d7a36a630ac4
Revises: 02d8e78fda85
Create Date: 2024-12-22 12:46:55.376057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7a36a630ac4'
down_revision: Union[str, None] = '02d8e78fda85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
