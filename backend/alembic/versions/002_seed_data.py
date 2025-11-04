"""Add seed data

Revision ID: 002_seed_data
Create Date: 2025-11-03 17:01:00.000000

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from app.core.security import get_password_hash

# revision identifiers, used by Alembic.
revision = '002_seed_data'
down_revision = '001_create_users'
branch_labels = None
depends_on = None

def upgrade():
    # Create an admin user
    op.execute(
        """
        INSERT INTO users (email, hashed_password, full_name, is_active, is_superuser)
        VALUES (
            'admin@example.com',
            '{}',
            'Admin User',
            TRUE,
            TRUE
        )
        """.format(get_password_hash('admin123'))  # In production, use env vars for passwords
    )

def downgrade():
    op.execute("DELETE FROM users WHERE email = 'admin@example.com'")