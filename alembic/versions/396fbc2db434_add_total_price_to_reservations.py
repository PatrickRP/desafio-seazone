"""add total_price to reservations

Revision ID: 396fbc2db434
Revises: 7143b660af7a
Create Date: 2025-08-16 02:24:39.288543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '396fbc2db434'
down_revision: Union[str, Sequence[str], None] = '7143b660af7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('reservations', sa.Column('total_price', sa.Float(10, 2), nullable=False, server_default='0.0'))


def downgrade() -> None:
    op.drop_column('reservations', 'total_price')