from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.

def upload_to(instance, filename):
    return f'{instance.id}. {instance.filename}/{filename}'

class CandidateDatabase(models.Model):

    filename = models.CharField(_("Enter Filename"), max_length=50)
    database = models.FileField(_("Database"), upload_to=None, max_length=100)
    assigned_to = models.ForeignKey(User, verbose_name=_("Assigned To"), on_delete=models.DO_NOTHING, blank=True, null=True)
    db_for = models.CharField(_("Database of"), max_length=50)
    database_size = models.IntegerField(_("Database Size"))

    class Meta:
        verbose_name = _("CandidateDatabase")
        verbose_name_plural = _("CandidateDatabases")

    def __str__(self):
        return self.filename

    def get_absolute_url(self):
        return reverse("CandidateDatabase_detail", kwargs={"pk": self.pk})


class TaskDone(models.Model):
    database = models.ForeignKey(CandidateDatabase, verbose_name=_("Database"), related_name="tasks", on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(_("Date"), auto_now_add=True, blank=True, null=True)
    activity = models.CharField(_("Activity Done"), max_length=50, blank=True, null=True)
    quantity = models.IntegerField(_("Activity Quantity"), blank=True, null=True)
    activity_range = models.CharField(_("Activity Range"), max_length=50, blank=True, null=True)
    content = models.TextField(_("Content"), blank=True, null=True)
    output = models.CharField(_("Output"), max_length=50, blank=True, null=True)   

    class Meta:
        verbose_name = _("TaskDone")
        verbose_name_plural = _("TasksDone")

    # def __str__(self):
    #     return self.activity

    def get_absolute_url(self):
        return reverse("TaskDone_detail", kwargs={"pk": self.pk})
