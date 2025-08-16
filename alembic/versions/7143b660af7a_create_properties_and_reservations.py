"""create properties and reservations

Revision ID: 7143b660af7a
Revises: 9a5282989f12
Create Date: 2025-08-16 01:03:21.856682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7143b660af7a'
down_revision: Union[str, Sequence[str], None] = '9a5282989f12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criar tabela de propriedades
    op.create_table(
        'properties',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('address_street', sa.String(255), nullable=True),
        sa.Column('address_number', sa.String(50), nullable=True),
        sa.Column('address_neighborhood', sa.String(100), nullable=True),
        sa.Column('address_city', sa.String(100), nullable=False),
        sa.Column('address_state', sa.String(50), nullable=False),
        sa.Column('country', sa.String(50), nullable=False, server_default="BRA"),
        sa.Column('rooms', sa.Integer, nullable=False),
        sa.Column('capacity', sa.Integer, nullable=False),
        sa.Column('price_per_night', sa.Numeric(10, 2), nullable=False),
    )

    # Criar tabela de reservas
    op.create_table(
        'reservations',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('client_name', sa.String(255), nullable=False),
        sa.Column('client_email', sa.String(255), nullable=False, index=True),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('end_date', sa.Date, nullable=False),
        sa.Column('guests_quantity', sa.Integer, nullable=False),
        sa.Column('property_id', sa.Integer, sa.ForeignKey('properties.id', ondelete="CASCADE"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('reservations')
    op.drop_table('properties')
