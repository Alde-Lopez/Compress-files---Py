
import yfinance as yf
import calendar, os
from datetime import datetime, timedelta


def create_monthly_files(y: list,tr: range):
    year_range=y
    time_range=tr

    os.chdir('Compress-files---Py/UNIT_TESTING_DATA')
    print("Standing in : ",os.getcwd())
    print("Listing directories: ",os.listdir())

    for mon in time_range:
        start_date = datetime(year_range[0], mon, 1)
        last_day=int(calendar.monthrange(year_range[0],mon)[1])
        end_date = datetime(2024, mon, last_day) 
        aapl_data = yf.download("AAPL", start=start_date, end=end_date) 
        aapl_data.to_csv('AAPL_{0}.csv'.format(calendar.month_name[mon][:3].upper()),index=False)

    return "The monthly files for the {0} year have been created".format(str(year_range))


if __name__=='__main__':
    create_monthly_files([2023],range(1,13))