"""First commit

Revision ID: 7c67a7c1c98a
Revises: 78950ad6e8ea
Create Date: 2024-03-25 14:53:19.873367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c67a7c1c98a'
down_revision: Union[str, None] = '78950ad6e8ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
