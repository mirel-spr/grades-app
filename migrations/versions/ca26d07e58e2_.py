"""empty message

Revision ID: ca26d07e58e2
Revises: 83c6f6402f35
Create Date: 2021-08-31 16:36:15.943750

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ca26d07e58e2'
down_revision = '83c6f6402f35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class_student',
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], )
    )
    op.drop_table('class_archives')
    op.drop_table('student_archives')
    op.add_column('students', sa.Column('is_archived', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'is_archived')
    op.create_table('student_archives',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], name='student_archives_school_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='student_archives_pkey'),
    sa.UniqueConstraint('student_id', name='student_archives_student_id_key')
    )
    op.create_table('class_archives',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('class_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('class_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('colour_hex', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], name='class_archives_school_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='class_archives_pkey'),
    sa.UniqueConstraint('class_id', name='class_archives_class_id_key')
    )
    op.drop_table('class_student')
    # ### end Alembic commands ###
