"""Initial migration

Revision ID: b06c578cc911
Revises: 
Create Date: 2023-07-01 00:06:37.518928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b06c578cc911'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('marriage_status', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('sexual_orientation', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=sa.String(length=20),
               type_=sa.DATE(),
               existing_nullable=True)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###
