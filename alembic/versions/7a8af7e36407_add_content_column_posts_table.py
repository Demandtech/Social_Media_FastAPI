"""add content column posts table

Revision ID: 7a8af7e36407
Revises: adaff5d20c6e
Create Date: 2023-10-28 03:35:55.957585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a8af7e36407'
down_revision: Union[str, None] = 'adaff5d20c6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
