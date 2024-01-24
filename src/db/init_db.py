from sqlalchemy.orm import Session
from src import crud, schemas

def init_users(db: Session) -> None:
    users = [
        schemas.CreateUser(
            first_name="admin",
            last_name="admin",
            email="admin@admin.com",
            is_webadmin=True,
            function="admin",
            password="zaq12wsx",
        )
    ]

    for user in users:
        crud.create_user(db, user=user)