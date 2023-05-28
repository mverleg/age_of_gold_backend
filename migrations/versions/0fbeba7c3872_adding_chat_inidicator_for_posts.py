"""adding chat inidicator for posts

Revision ID: 0fbeba7c3872
Revises: 5d1374e3d087
Create Date: 2023-03-22 20:40:10.470789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0fbeba7c3872"
down_revision = "5d1374e3d087"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("Post", schema=None) as batch_op:
        batch_op.add_column(sa.Column("chat_id", sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("Post", schema=None) as batch_op:
        batch_op.drop_column("chat_id")

    # ### end Alembic commands ###
