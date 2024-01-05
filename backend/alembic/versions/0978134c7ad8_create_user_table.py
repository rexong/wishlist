"""Create User Table

Revision ID: 0978134c7ad8
Revises: 
Create Date: 2024-01-05 21:33:00.806247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0978134c7ad8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users', 
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('email', sa.String(), unique=True),
        sa.Column('hashed_password', sa.String())
    )

def downgrade() -> None:
    op.drop_table('users')
