"""Add Owner ID Column to Wishes

Revision ID: 14148e5044e6
Revises: e13c0ae2a562
Create Date: 2024-01-06 00:54:43.787842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14148e5044e6'
down_revision: Union[str, None] = 'e13c0ae2a562'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'wishes',
        sa.Column('owner_id', sa.Integer(), sa.ForeignKey('users.id'))
    )


def downgrade() -> None:
    op.drop_column(
        'wishes',
        sa.Column('owner_id')
    )
