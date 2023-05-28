"""verification for email and unique constraint on email and origin

Revision ID: 5d1374e3d087
Revises: cf16e11a7eb8
Create Date: 2023-03-03 10:48:40.701639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5d1374e3d087"
down_revision = "cf16e11a7eb8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("User", schema=None) as batch_op:
        batch_op.add_column(sa.Column("email_verified", sa.Boolean(), nullable=True))
        batch_op.alter_column(
            "about_me",
            existing_type=sa.VARCHAR(length=140),
            type_=sa.Text(),
            existing_nullable=True,
        )
        batch_op.drop_index("ix_User_email")
        batch_op.create_index("user_index", ["email", "origin"], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("User", schema=None) as batch_op:
        batch_op.drop_index("user_index")
        batch_op.create_index("ix_User_email", ["email"], unique=False)
        batch_op.alter_column(
            "about_me",
            existing_type=sa.Text(),
            type_=sa.VARCHAR(length=140),
            existing_nullable=True,
        )
        batch_op.drop_column("email_verified")

    # ### end Alembic commands ###
