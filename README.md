# ![sly logo](https://raw.githubusercontent.com/dunkyl/SlyMeta/main/sly%20logo.svg) Sly YTAAPI for Python

> 🚧 **This library is an early work in progress! Breaking changes may be frequent.**

> 🐍 For Python 3.10+

## No boilerplate, _async_ and _typed_ Youtube Analytics API access. 😋

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
from SlyYTAAPI import *

async def main():

    analytics = await YouTubeAnalytics('UCxATMl-Cv8BEF0FtZMRvRgA', 'test/app.json', 'test/user.json')

    result = await analytics.query(
        since=date(2020, 1, 1),
        metrics=Metrics.SubsGained+Metrics.SubsLost+Metrics.WatchTime,
        dims=Dimensions.Day
        )

    result.saveCSV('test/test.csv')

asyncio.run(main())
```
