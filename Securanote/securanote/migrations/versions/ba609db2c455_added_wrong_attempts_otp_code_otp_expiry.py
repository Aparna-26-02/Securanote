"""Added wrong_attempts, otp_code, otp_expiry

Revision ID: ba609db2c455
Revises: 4fe3d61a0e53
Create Date: 2025-06-20 15:35:44.117457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba609db2c455'
down_revision = '4fe3d61a0e53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('wrong_attempts', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('otp_code', sa.String(length=6), nullable=True))
        batch_op.add_column(sa.Column('otp_expiry', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.drop_column('otp_expiry')
        batch_op.drop_column('otp_code')
        batch_op.drop_column('wrong_attempts')

    # ### end Alembic commands ###
