from datetime import date
from SlyYTAAPI import *

async def test_readme():

    analytics = await YouTubeAnalytics('UCxATMl-Cv8BEF0FtZMRvRgA', 'test/app.json', 'test/user.json')

    result = await analytics.query(
        since=date(2020, 1, 1),
        metrics=Metrics.SubsGained+Metrics.SubsLost+Metrics.WatchTime,
        dims=Dimensions.Day
        )

    result.saveCSV('test/test.csv')