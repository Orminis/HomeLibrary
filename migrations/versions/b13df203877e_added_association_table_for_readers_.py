"""Added association table for readers books many to many relations. Added Digital Books Model

Revision ID: b13df203877e
Revises: ff718a2b658a
Create Date: 2022-08-21 14:25:51.310346

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b13df203877e"
down_revision = "ff718a2b658a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "digital_books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("author_first_name", sa.String(length=35), nullable=False),
        sa.Column("author_last_name", sa.String(length=35), nullable=False),
        sa.Column("genre", sa.String(length=20), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("comments", sa.Text(), nullable=True),
        sa.Column("original_language", sa.String(length=20), nullable=True),
        sa.Column("publish_language", sa.String(length=20), nullable=False),
        sa.Column("edition", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "basic_users_books_associations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("reading_book_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["reading_book_id"],
            ["reading_books.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["standard_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_column("reading_books", "digital_format")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("reading_books_for_approval", "status")
    op.add_column(
        "reading_books",
        sa.Column("digital_format", sa.BOOLEAN(), autoincrement=False, nullable=False),
    )
    op.drop_column("audio_books_for_approval", "status")
    op.drop_table("basic_users_books_associations")
    op.drop_table("digital_books")
    # ### end Alembic commands ###
