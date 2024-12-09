from django.db import models

class tycdata(models.Model):
    requested_part = models.CharField(max_length=255)
    te_internal_number = models.CharField(max_length=255)
    part_status = models.CharField(max_length=255)
    rohs_compliant_status = models.CharField(max_length=255)
    rohs_exemption_substance_info = models.TextField()
    reach_version_status = models.CharField(max_length=255)
    reach_compliant_status = models.CharField(max_length=255)
    reach_svhc_substance = models.TextField()

    def __str__(self):
        return self.requested_part
