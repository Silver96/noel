# ----------------------------
#  Andrea Silvestroni 2019
#  Residual Noise Extraction and Smartphone Linking
#
# ----------------------------

from django.core.validators import RegexValidator
from django.db import models

# from main.logic.common.funcs import get_session_progress


class Session(models.Model):
    """
    Model that represents a Session on the system. It is created when the user submits their photos through the index's
    form, and is used throughout the process to keep track of the steps that need to be completed.
    """
    # TODO: consider adding an email field for completion notification
    # TODO: consider using Django's file managing instead of direct path access

    id = models.CharField(max_length=64, validators=[RegexValidator(regex='^.{64}$')], primary_key=True)
    status = models.CharField(max_length=50)
    progress = models.IntegerField(default=0)

    @property
    def session_dir(self):
        """
        :return: Path to the session's main directory
        """
        return 'storage/{}'.format(self.id)

    def update_and_log_status(self, new_status: str):
        """
        Updates session status and logs it to console

        :param new_status: The status to be set
        """
        self.status = new_status
        # self.progress = get_session_progress(new_status)
        self.save()
        print('[{}]: {}'.format(self.id, new_status))