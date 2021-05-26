# Command File for generate nse report for all the clients with their respective Chain
from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from nsepython import nse_optionchain_scrapper
import pandas as pd
from nse.models import NseSettings, NseReport
from nse.utils.utils import *


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        res = NseSettings.objects.all()
        self.stdout.write("Process start time %s" % time)
        for i in res:
            print(i.client)
            a = nse_optionchain_scrapper(i.nse_list)

            res_ce = []
            res_pe = []
            filter_ce = []
            filter_pe = []

            for data in a['records']['data']:
                res_ce.append(form_res(data.get('CE')))
                res_pe.append(form_res(data.get('PE')))

            for data in a['filtered']['data']:
                filter_ce.append(form_res(data.get('CE')))
                filter_pe.append(form_res(data.get('PE')))

            ce = pd.DataFrame(res_ce)
            pe = pd.DataFrame(res_pe)
            fil_ce = pd.DataFrame(filter_ce)
            fil_pe = pd.DataFrame(filter_pe)
            file_path = i.path
            date_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            file_name = str(file_path) + '/' + str(i.client) + '_' + str(date_time) + '.xlsx'
            print(file_name)
            with pd.ExcelWriter(file_name) as writer:
                ce.to_excel(writer, sheet_name='CE')
                pe.to_excel(writer, sheet_name='PE')
                fil_ce.to_excel(writer, sheet_name='FILTERED_CE')
                fil_pe.to_excel(writer, sheet_name='FILTERED_PE')

            if i:
                NseReport.objects.create(nse=i, file_path=file_name, generate_date=datetime.datetime.now())
            print('Completed')
        self.stdout.write("Process end time %s" % time)