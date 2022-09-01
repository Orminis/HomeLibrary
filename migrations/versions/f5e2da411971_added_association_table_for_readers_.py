"""Second attempt. Added association table for readers books many-to-many relations.

Revision ID: f5e2da411971
Revises: b13df203877e
Create Date: 2022-08-21 14:40:18.641058

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f5e2da411971'
down_revision = 'b13df203877e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_reading_books_associations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('reading_book_id', sa.Integer(), nullable=True),
    sa.Column('user_comments', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['reading_book_id'], ['reading_books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['standard_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('basic_users_books_associations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basic_users_books_associations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('reading_book_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['reading_book_id'], ['reading_books.id'], name='basic_users_books_associations_reading_book_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['standard_user.id'], name='basic_users_books_associations_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='basic_users_books_associations_pkey')
    )
    op.drop_table('users_reading_books_associations')
    # ### end Alembic commands ###
