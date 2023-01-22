from database import session as db,create_table
from datetime import datetime

import models

def create_dummy():
    db_dummy = models.Announcement(company_name="ABC",description="Dunmy Description",time = datetime(2023,1,13,22,43,23))
    create_table()
    db.add(db_dummy)
    db.commit()




