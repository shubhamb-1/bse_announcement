from datetime import datetime,timedelta
from database import get_db_session
import models


def add_to_db(insert_list:list):

    #unique_id,company_name,company_id,announcement,announcement_type,announcement_link,time
    session = get_db_session()
    try:
        for data in insert_list:
            is_present = session.query(models.Announcement).filter_by(unique_id=data['unique_id']).first()
            if not is_present:
                to_add = models.Announcement(unique_id=data['unique_id'],company_name=data['company_name'],company_id=data['company_id'],
                        announcement=data['announcement'],announcement_type=data['announcement_type'],
                        announcement_link=data['announcement_link'],time =data['announcement_time'])
                print(to_add)
                session.add(to_add)
                session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise e
    finally:
        session.close()
