from datetime import date
from SlyYTAAPI import *

async def test_readme():

    auth = OAuth2('test/app.json', 'test/user.json')
    analytics = YouTubeAnalytics('UCxATMl-Cv8BEF0FtZMRvRgA', auth)

    result = await analytics.query(
        since=date(2020, 1, 1),
        end_date=date(2021, 1, 1),
        metrics=Metrics.SubsGained+Metrics.SubsLost+Metrics.WatchTime,
        dims=Dimensions.Day
        )

    result.saveCSV('test/test.csv')