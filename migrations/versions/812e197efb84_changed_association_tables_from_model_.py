"""changed association tables from model to table

Revision ID: 812e197efb84
Revises: bfbf1586baa3
Create Date: 2022-08-23 13:34:46.732917

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "812e197efb84"
down_revision = "bfbf1586baa3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_audio_books_associations")
    op.drop_table("users_digital_books_associations")
    op.drop_table("users_reading_books_associations")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users_reading_books_associations",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("reading_book_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("user_comments", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("user_rating", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "user_condition",
            postgresql.ENUM(
                "mint",
                "fine",
                "very_good",
                "good",
                "fair",
                "poor",
                name="user_condition",
            ),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["reading_book_id"],
            ["reading_books.id"],
            name="users_reading_books_associations_reading_book_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["standard_user.id"],
            name="users_reading_books_associations_user_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id", name="users_reading_books_associations_pkey"),
    )
    op.create_table(
        "users_digital_books_associations",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("digital_book_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("user_comments", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("user_rating", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["digital_book_id"],
            ["digital_books.id"],
            name="users_digital_books_associations_digital_book_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["standard_user.id"],
            name="users_digital_books_associations_user_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id", name="users_digital_books_associations_pkey"),
    )
    op.create_table(
        "users_audio_books_associations",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("audio_book_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("user_comments", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("user_rating", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["audio_book_id"],
            ["audio_books.id"],
            name="users_audio_books_associations_audio_book_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["standard_user.id"],
            name="users_audio_books_associations_user_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id", name="users_audio_books_associations_pkey"),
    )
    # ### end Alembic commands ###
