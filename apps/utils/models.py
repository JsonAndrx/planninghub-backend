from django.db import models

class PlanningModel(models.Model):

    created = models.DateTimeField(
        'created_at',
        auto_now_add = True,
        help_text = 'Date time which the object  was created'
    )
    modified = models.DateTimeField(
        'modified_at',
        auto_now= True,
    )

    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']