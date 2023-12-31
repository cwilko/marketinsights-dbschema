"""Add updated_on column

Revision ID: 6966c38a8909
Revises: 8a0e725e025e
Create Date: 2023-07-21 10:00:07.985010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6966c38a8909"
down_revision = "8a0e725e025e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("houses", sa.Column("updated_on", sa.DateTime()))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("houses", "updated_on")
    # ### end Alembic commands ###
