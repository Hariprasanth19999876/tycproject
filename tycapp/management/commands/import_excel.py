import pandas as pd
from django.core.management.base import BaseCommand
from tycapp.models import tycdata

class Command(BaseCommand):
    help = "Import compliance data from Excel file"

    def handle(self, *args, **kwargs):
        file_path = "C:/Users/Welcome/Downloads/wholetycdata.xlsx"
        data = pd.read_excel(file_path)

        for _, row in data.iterrows():
            tycdata.objects.create(
                requested_part=row['REQUESTED_PART'],
                te_internal_number=row['TE_INTERNAL_NUMBER'],
                part_status=row['PART_STATUS'],
                rohs_compliant_status=row['ROHS_COMPLIANT_STATUS'],
                rohs_exemption_substance_info=row['ROHS_EXEMPTION_SUBSTANCE_INFO'],
                reach_version_status=row['REACH_VERSION_STATUS'],
                reach_compliant_status=row['REACH_COMPLIANT_STATUS'],
                reach_svhc_substance=row['REACH_SVHC_SUBSTANCE']
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
