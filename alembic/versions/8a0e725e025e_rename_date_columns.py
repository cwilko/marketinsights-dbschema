"""Rename date columns

Revision ID: 8a0e725e025e
Revises: cc5ed79f88e8
Create Date: 2023-07-20 21:40:40.801516

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8a0e725e025e"
down_revision = "cc5ed79f88e8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("houses", "date", new_column_name="created_on")
    op.alter_column("houses", "datesold", new_column_name="sold_on")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("houses", "created_on", new_column_name="date")
    op.alter_column("houses", "sold_on", new_column_name="datesold")
    # ### end Alembic commands ###