"""create isbn column as BigInt and unique

Revision ID: 08e5b4a1f781
Revises: c61f4e8ad700
Create Date: 2022-08-24 23:54:31.792137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08e5b4a1f781'
down_revision = 'c61f4e8ad700'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('audio_books', sa.Column('isbn', sa.BigInteger(), nullable=False))
    op.create_unique_constraint(None, 'audio_books', ['isbn'])
    op.add_column('audio_books_for_approval', sa.Column('isbn', sa.BigInteger(), nullable=False))
    op.create_unique_constraint(None, 'audio_books_for_approval', ['isbn'])
    op.add_column('digital_books', sa.Column('isbn', sa.BigInteger(), nullable=False))
    op.create_unique_constraint(None, 'digital_books', ['isbn'])
    op.add_column('digital_books_for_approval', sa.Column('isbn', sa.BigInteger(), nullable=False))
    op.create_unique_constraint(None, 'digital_books_for_approval', ['isbn'])
    op.add_column('reading_books', sa.Column('isbn', sa.BigInteger(), nullable=False))
    op.create_unique_constraint(None, 'reading_books', ['isbn'])
    op.add_column('reading_books_for_approval', sa.Column('isbn', sa.BigInteger(), nullable=False))
    op.create_unique_constraint(None, 'reading_books_for_approval', ['isbn'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reading_books_for_approval', type_='unique')
    op.drop_column('reading_books_for_approval', 'isbn')
    op.drop_constraint(None, 'reading_books', type_='unique')
    op.drop_column('reading_books', 'isbn')
    op.drop_constraint(None, 'digital_books_for_approval', type_='unique')
    op.drop_column('digital_books_for_approval', 'isbn')
    op.drop_constraint(None, 'digital_books', type_='unique')
    op.drop_column('digital_books', 'isbn')
    op.drop_constraint(None, 'audio_books_for_approval', type_='unique')
    op.drop_column('audio_books_for_approval', 'isbn')
    op.drop_constraint(None, 'audio_books', type_='unique')
    op.drop_column('audio_books', 'isbn')
    # ### end Alembic commands ###
