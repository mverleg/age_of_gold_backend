"""adding unique to username

Revision ID: 01ffd9ee8d7c
Revises: 48d22f822768
Create Date: 2022-10-11 10:20:38.908227

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "01ffd9ee8d7c"
down_revision = "48d22f822768"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_User_username", table_name="User")
    op.create_index(op.f("ix_User_username"), "User", ["username"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_User_username"), table_name="User")
    op.create_index("ix_User_username", "User", ["username"], unique=False)
    # ### end Alembic commands ###
