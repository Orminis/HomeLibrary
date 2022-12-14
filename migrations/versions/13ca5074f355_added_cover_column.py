"""added cover column

Revision ID: 13ca5074f355
Revises: 08e5b4a1f781
Create Date: 2022-08-31 19:46:16.007200

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "13ca5074f355"
down_revision = "08e5b4a1f781"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "audio_books", sa.Column("cover", sa.String(length=255), nullable=False)
    )
    op.alter_column("audio_books", "isbn", existing_type=sa.BIGINT(), nullable=False)
    op.add_column(
        "audio_books_for_approval",
        sa.Column("cover", sa.String(length=255), nullable=False),
    )
    op.alter_column(
        "audio_books_for_approval", "isbn", existing_type=sa.BIGINT(), nullable=False
    )
    op.add_column(
        "digital_books", sa.Column("cover", sa.String(length=255), nullable=False)
    )
    op.alter_column("digital_books", "isbn", existing_type=sa.BIGINT(), nullable=False)
    op.add_column(
        "digital_books_for_approval",
        sa.Column("cover", sa.String(length=255), nullable=False),
    )
    op.alter_column(
        "digital_books_for_approval", "isbn", existing_type=sa.BIGINT(), nullable=False
    )
    op.add_column(
        "reading_books", sa.Column("cover", sa.String(length=255), nullable=False)
    )
    op.alter_column("reading_books", "isbn", existing_type=sa.BIGINT(), nullable=False)
    op.add_column(
        "reading_books_for_approval",
        sa.Column("cover", sa.String(length=255), nullable=False),
    )
    op.alter_column(
        "reading_books_for_approval", "isbn", existing_type=sa.BIGINT(), nullable=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "reading_books_for_approval", "isbn", existing_type=sa.BIGINT(), nullable=True
    )
    op.drop_column("reading_books_for_approval", "cover")
    op.alter_column("reading_books", "isbn", existing_type=sa.BIGINT(), nullable=True)
    op.drop_column("reading_books", "cover")
    op.alter_column(
        "digital_books_for_approval", "isbn", existing_type=sa.BIGINT(), nullable=True
    )
    op.drop_column("digital_books_for_approval", "cover")
    op.alter_column("digital_books", "isbn", existing_type=sa.BIGINT(), nullable=True)
    op.drop_column("digital_books", "cover")
    op.alter_column(
        "audio_books_for_approval", "isbn", existing_type=sa.BIGINT(), nullable=True
    )
    op.drop_column("audio_books_for_approval", "cover")
    op.alter_column("audio_books", "isbn", existing_type=sa.BIGINT(), nullable=True)
    op.drop_column("audio_books", "cover")
    # ### end Alembic commands ###
