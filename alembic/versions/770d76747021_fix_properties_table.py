"""fix properties table

Revision ID: 770d76747021
Revises: 396fbc2db434
Create Date: 2025-08-16 02:56:38.700613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '770d76747021'
down_revision: Union[str, Sequence[str], None] = '396fbc2db434'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
