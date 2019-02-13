from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name="send_email_to_users_task")
def send_email_to_users_task(email_list, message):
    """sends an email To PVR users """
    logger.info("Sent PVR email")
    # need to be defined
    for email in email_list:
        send_mail(email[0], message)
    
    return('Mail is sent to the user list')