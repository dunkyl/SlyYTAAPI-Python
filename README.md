# ![sly logo](https://raw.githubusercontent.com/dunkyl/SlyMeta/main/sly%20logo.svg) Sly YTAAPI for Python

> 🐍 For Python 3.10+

## No boilerplate, *async* and *typed* Youtube Analytics API access. 😋

```shell
pip install slyytaapi
```

This library does not have full coverage.
Currently, the following topics are supported:

* Targeted queries for channels and videos

You can directly grant user tokens using the command line, covering the whole OAuth 2 grant process.

---

Example usage:

```python
import asyncio
from datetime import date
from SlyYTAAPI import *

async def main():

    auth = OAuth2('test/app.json', 'test/user.json')
    analytics = YouTubeAnalytics('UCxATMl-Cv8BEF0FtZMRvRgA', auth)

    result = await analytics.query(
        since=date(2020, 1, 1),
        end_date=date(2021, 1, 1),
        metrics=Metrics.SubsGained+Metrics.SubsLost+Metrics.WatchTime,
        dims=Dimensions.Day
        )

    result.saveCSV('test/test.csv')

asyncio.run(main())
```

---

Example CLI usage for getting authorized:

```sh
# WINDOWS
py -m SlyYTAAPI grant
# MacOS or Linux
python3 -m SlyYTAAPI grant
```

Granting credentials requires a Google Cloud Console account and JSON file.
Please see https://docs.dunkyl.net/SlyAPI-Python/tutorial/oauth2.html for more information.