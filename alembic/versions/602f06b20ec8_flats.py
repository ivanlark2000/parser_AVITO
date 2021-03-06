"""flats

Revision ID: 602f06b20ec8
Revises: b0e122aff103
Create Date: 2022-07-24 15:57:04.599389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '602f06b20ec8'
down_revision = 'b0e122aff103'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('district',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_area', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('house',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area', sa.String(length=150), nullable=True),
    sa.Column('street', sa.String(length=200), nullable=False),
    sa.Column('number_of_house', sa.Integer(), nullable=True),
    sa.Column('new_building_name', sa.String(length=200), nullable=True),
    sa.Column('offical_builder', sa.String(length=200), nullable=True),
    sa.Column('year_of_construction', sa.Integer(), nullable=True),
    sa.Column('floors_in_the_hourse', sa.Integer(), nullable=True),
    sa.Column('passenger_bodice', sa.Boolean(), nullable=False),
    sa.Column('service_lift', sa.Boolean(), nullable=False),
    sa.Column('in_home', sa.String(length=200), nullable=True),
    sa.Column('pemolition_planned', sa.String(length=200), nullable=True),
    sa.Column('type_of_bilding', sa.String(length=200), nullable=True),
    sa.Column('yard', sa.String(length=200), nullable=True),
    sa.Column('parking', sa.String(length=200), nullable=True),
    sa.Column('deadline', sa.String(length=150), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_avito', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(precision=15, scale=2), nullable=False),
    sa.Column('qty_of_rooms', sa.Integer(), nullable=True),
    sa.Column('total_space', sa.Numeric(precision=3, scale=2), nullable=False),
    sa.Column('square_of_kitchen', sa.Numeric(precision=3, scale=2), nullable=False),
    sa.Column('living_space', sa.Numeric(precision=3, scale=2), nullable=False),
    sa.Column('floor', sa.Integer(), nullable=False),
    sa.Column('furniture', sa.String(length=200), nullable=True),
    sa.Column('technics', sa.String(length=200), nullable=True),
    sa.Column('balcony_or_loggia', sa.Boolean(), nullable=False),
    sa.Column('room_type', sa.String(length=120), nullable=True),
    sa.Column('ceiling_height', sa.Numeric(precision=3, scale=2), nullable=True),
    sa.Column('bathroom', sa.String(length=120), nullable=True),
    sa.Column('widow', sa.String(length=120), nullable=True),
    sa.Column('repair', sa.String(length=120), nullable=True),
    sa.Column('seilling_method', sa.String(length=120), nullable=True),
    sa.Column('transaction_type', sa.String(length=120), nullable=True),
    sa.Column('decorating', sa.String(length=120), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], ),
    sa.ForeignKeyConstraint(['house_id'], ['house.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flat')
    op.drop_table('house')
    op.drop_table('district')
    # ### end Alembic commands ###
