from dataclasses import dataclass, asdict
from datetime import date, timedelta
import json, csv
from enum import Enum
from typing import Any, TypeVar
from SlyAPI import *

def makeFilters(filters: dict[str, Any]) -> str:
    out: list[str] = []
    for key, value in filters.items():
        out.append(F"{key}=={value}")
    return ';'.join(out)

_T = TypeVar('_T')
class _AddOperator_Set(set[_T]):
    '''set with + operator. Workaround for backwards compatibility with
    EnumParams (type removed from SlyAPI)'''
    def __add__(self, other: _T|set[_T]) -> '_AddOperator_Set[_T]':
        if isinstance(other, set):
            return _AddOperator_Set((*self, *other))
        return _AddOperator_Set((*self, other))

class Dimensions(Enum):
    'From https://developers.google.com/youtube/analytics/dimensions'
    Day             = 'day'
    Month           = 'month'
    #Week            = '7DayTotals' # deprecated, valid until April 15, 2020
    Country         = 'country'
    Video           = 'video'
    # ...

    def __add__(self: 'Dimensions', other: 'Dimensions|set[Dimensions]') -> _AddOperator_Set['Dimensions']:
        return _AddOperator_Set((self,)) + other

class Metrics(Enum):
    'From https://developers.google.com/youtube/reporting#metrics'
    #Revenue         = 'estimated_partner_revenue' 
    Views           = 'views'
    #TrafficSource   = 'traffic_source_detail'
    Likes           = 'likes'
    Dislikes        = 'dislikes'
    WatchTime       = 'estimatedMinutesWatched'
    #EstimatedCPM    = 'estimated_cpm'
    SubsGained      = 'subscribersGained'
    SubsLost        = 'subscribersLost'
    # ...

    def __add__(self: 'Metrics', other: 'Metrics|set[Metrics]') -> _AddOperator_Set['Metrics']:
        return _AddOperator_Set((self,)) + other

@dataclass
class QueryResult:
    kind: str
    columnHeaders: list[dict[str, str]] # { "name": ..., "columnType": ..., "dataType": ... }
    rows: list[list[Any]]

    def saveJSON(self, path: str):
        with open(path, mode='w', encoding='utf8') as f:
            json.dump(asdict(self), f)

    def saveCSV(self, path: str):
        with open(path, mode='w', newline='', encoding='utf8') as f:
            # UTF-8 BOM for Excel
            f.write('\ufeff')
            writer = csv.writer(f)
            headers = [header['name'] for header in self.columnHeaders]
            writer.writerow(headers)
            writer.writerows(self.rows)

class Scope:
    Analytics       = 'https://www.googleapis.com/auth/yt-analytics.readonly'
    Monetary        = 'https://www.googleapis.com/auth/yt-analytics-monetary.readonly'
    YouTube         = 'https://www.googleapis.com/auth/youtube'
    YouTubePartner  = 'https://www.googleapis.com/auth/youtubepartner'
    YouTubeReadOnly = 'https://www.googleapis.com/auth/youtube.readonly'

class YouTubeAnalytics(WebAPI):
    base_url = 'https://youtubeanalytics.googleapis.com/v2'
    DEFAULT_SCOPES = Scope.Analytics + ' ' + Scope.Monetary + ' ' + Scope.YouTubeReadOnly 

    channel_id: str

    def __init__(self, channel_id: str, auth: OAuth2):
        super().__init__(auth)
        self.channel_id = channel_id

    # Backwards compatibility with SlyAPI < 0.4.0
    # Do nothing when awaited
    def __await__(self):
        async def delay(): return self
        return delay().__await__()

    async def video(self, video_id: str, since: date, metrics: Metrics|set[Metrics], 
        dims: Dimensions|set[Dimensions], end_date: date|None=None) -> QueryResult:
        return await self.query(since, metrics, dims, end_date, {'video': video_id})

    async def query(self, since: date, metrics: Metrics|set[Metrics],
        dims: Dimensions|set[Dimensions], end_date: date|None=None, filters:dict[str, Any]|None=None) -> QueryResult:
        if end_date is None:
            end_date = date.today()
        if dims == Dimensions.Month: # month requires end date as first day of next month
            end_date = end_date - timedelta(days=end_date.day-1)
        # normalize to sets
        if isinstance(metrics, Metrics): metrics = {metrics}
        if isinstance(dims, Dimensions): dims = {dims}

        result = await self._reports_query(since, end_date , metrics, dims, filters)
        return QueryResult(**result)

    async def _reports_query(self, start_date: date, end_date: date, metrics: set[Metrics], dims: set[Dimensions], filters: dict[str, Any]|None=None) -> dict[str, Any]:
        params = {
            'startDate': start_date.isoformat(),
            'endDate': end_date.isoformat(),
            'ids': F"channel=={self.channel_id}",
            'metrics': ','.join(metric.value for metric in metrics)
        }
        if filters:
            params['filters'] = makeFilters(filters)
        if dims:
            params['dimensions'] = ','.join(dim.value for dim in dims)

        return await self.get_json(F"/reports", params)
    