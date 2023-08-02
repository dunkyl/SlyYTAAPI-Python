import pytest, os
from datetime import date
from SlyYTAAPI import *

test_dir = os.path.dirname(__file__)

@pytest.mark.skip("needs credentials")
async def test_readme():

    auth = OAuth2(F'{test_dir}/app.json', F'{test_dir}/user.json')
    analytics = YouTubeAnalytics('UCxATMl-Cv8BEF0FtZMRvRgA', auth)

    result = await analytics.query(
        since=date(2020, 1, 1),
        end_date=date(2021, 1, 1),
        metrics=Metrics.SubsGained+Metrics.SubsLost+Metrics.WatchTime,
        dims=Dimensions.Day
        )

    result.saveCSV(F'{test_dir}/test.csv')