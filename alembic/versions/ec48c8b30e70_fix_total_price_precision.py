"""fix total_price precision

Revision ID: ec48c8b30e70
Revises: 770d76747021
Create Date: 2025-08-16 16:19:01.962317

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec48c8b30e70'
down_revision: Union[str, Sequence[str], None] = '770d76747021'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('reservations', 'total_price',
        type_=sa.Numeric(10, 2),
        existing_nullable=False,
        existing_server_default='0.0'
    )


def downgrade() -> None:
    op.alter_column('reservations', 'total_price',
        type_=sa.Float(),
        existing_nullable=False,
        existing_server_default='0.0'
    )
