from models.role import Role
from models import db
from app import app

def seed_roles():
    roles = ['Admin', 'Staff']

    for role_name in roles:
        existing_role = Role.query.filter_by(role_name=role_name).first()
        if not existing_role:
            new_role = Role(role_name=role_name)
            db.session.add(new_role)
            print(f"Added role: {role_name}")
        else:
            print(f"Role '{role_name}' already exists")

    db.session.commit()
    print("Seeding completed.")

if __name__ == '__main__':
    with app.app_context():
        seed_roles()
