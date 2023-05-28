"""adding some authentication columns on the user

Revision ID: e1cc800f23f8
Revises: 14e880e9a774
Create Date: 2022-11-26 12:46:46.338629

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e1cc800f23f8"
down_revision = "14e880e9a774"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("User", sa.Column("token", sa.Text(), nullable=True))
    op.add_column("User", sa.Column("token_expiration", sa.Integer(), nullable=True))
    op.drop_index("ix_User_email", table_name="User")
    op.create_index(op.f("ix_User_email"), "User", ["email"], unique=False)
    op.create_index(op.f("ix_User_token"), "User", ["token"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_User_token"), table_name="User")
    op.drop_index(op.f("ix_User_email"), table_name="User")
    op.create_index("ix_User_email", "User", ["email"], unique=False)
    op.drop_column("User", "token_expiration")
    op.drop_column("User", "token")
    # ### end Alembic commands ###
