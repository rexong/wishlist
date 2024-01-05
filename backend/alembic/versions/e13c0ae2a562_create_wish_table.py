"""Create Wish Table

Revision ID: e13c0ae2a562
Revises: 0978134c7ad8
Create Date: 2024-01-06 00:42:38.543814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e13c0ae2a562'
down_revision: Union[str, None] = '0978134c7ad8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'wishes',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.Column('link', sa.String()),
        sa.Column('is_hidden', sa.Boolean(), nullable=False, default=False)
    )


def downgrade() -> None:
    op.drop_table('wishes')
