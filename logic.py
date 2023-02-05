from datetime import datetime,timedelta
from database import session
import models

# def in_chache(unique_id):
#     result = session.query(models.Cache).filter_by(unique_id=unique_id).first()
#     return result



# def add_to_cache(unique_id,company_name,company_id,announcement,announcement_type,announcement_link,time):
#     if not in_chache(unique_id):
#         first_col = session.query(models.Cache).filter_by(id=1).first()
#         if first_col:
#             to_add = models.Announcement(company_name=first_col.company_name,company_id=first_col.company_id,
#             announcement=first_col.announcement,announcement_type=first_col.announcement_type,
#             announcement_link=first_col.announcement_link,time =first_col.time)
#             session.delete(first_col)
#             session.add(to_add)
#         else:
#             to_add = models.Cache(unique_id=unique_id,company_name=company_name,company_id=company_id,
#             announcement=announcement,announcement_type=announcement_type,
#             announcement_link=announcement_link,time =time)
#             session.add(to_add)
#         session.commit()

def add_to_cache(unique_id,company_name,company_id,announcement,announcement_type,announcement_link,time):
    to_add = models.Cache(unique_id=unique_id,company_name=company_name,company_id=company_id,
            announcement=announcement,announcement_type=announcement_type,
            announcement_link=announcement_link,time =time)
    session.add(to_add)
    session.commit()

def move_from_cache():

    unique_data = (session.query(models.Cache).filter(models.Cache.time > datetime.now() - timedelta(hours=1)).distinct(models.Cache.unique_id))

    for data in unique_data:
        session.add(models.Announcement(company_name=data.company_name,company_id=data.company_id,announcement=data.announcement,announcement_type=data.announcement_type,announcement_link=data.announcement_link,time=data.time))
        session.commit()

    session.query(models.Cache).delete()
    session.commit()
