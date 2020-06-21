import requests
import json
import datetime
import collections


def make_request(datetime_from, datetime_to):
    datetime_from = datetime_from.isoformat() + 'Z'
    datetime_to = datetime_to.isoformat() + 'Z'

    req_payload = {
        "aggs": {
            "2": {
                "date_histogram": {
                    "field": "@timestamp",
                    "fixed_interval": "60m",
                    "time_zone": "Europe/Warsaw",
                    "min_doc_count": 1
                },
                "aggs": {
                    "3": {
                        "terms": {
                            "field": "agent.hostname.keyword",
                            "order": {
                                "1": "desc"
                            },
                            "size": 100000
                        },
                        "aggs": {
                            "1": {
                                "avg": {
                                    "field": "data.adverts_average_per_second"
                                }
                            }
                        }
                    }
                }
            }
        },
        "size": 0,
        "stored_fields": ["*"],
        "script_fields": {},
        "docvalue_fields": [{
            "field": "@timestamp",
            "format": "date_time"
        }],
        "_source": {
            "excludes": []
        },
        "query": {
            "bool": {
                "must": [],
                "filter": [{
                    "range": {
                        "@timestamp": {
                            "gte": datetime_from,
                            # "gte": "2020-06-21T06:16:45.901Z",
                            "lte": datetime_to,
                            # "lte": "2020-06-21T16:16:45.901Z",
                            "format": "strict_date_optional_time"
                        }
                    }
                }],
                "should": [],
                "must_not": []
            }
        }
    }

    r = requests.post(
        "http://kibana.cow.test01.stermedia.eu:5601/elasticsearch/snifferbeat*/_search",
        params={
            "rest_total_hits_as_int": "true",
            "ignore_throttled": "true",
            # "preference": 1592756203029,
            "timeout": "30000ms",
        },
        headers={
            "Accept": "application/json, text/plain, */*",
            "kbn-version": "7.6.1",
            "content-type": "application/json",
        },
        data=json.dumps(req_payload)
    )

    return r


def get_matrix():
    datetime_to = datetime.datetime.utcnow()
    datetime_from = datetime_to - datetime.timedelta(hours=11)

    # print(datetime_from)
    # print(datetime_to)
    try:

        request = make_request(
            datetime_from=datetime_from, datetime_to=datetime_to)
        request.raise_for_status()

        matrix = process_request_data_to_matrix(request_data=request.json())
        return matrix
    except Exception as e:
        print(e)
        return None


def process_request_data_to_matrix(request_data):
    buckets = request_data["aggregations"]["2"]["buckets"][1:-1]
    print(len(buckets))

    wps = set()
    data = []
    for bucket in buckets:
        time_slice_data = collections.defaultdict(dict)
        for time_slice_bucket in bucket['3']['buckets']:
            wps.add(time_slice_bucket['key'])
            time_slice_data[time_slice_bucket['key']
                            ] = time_slice_bucket['1']['value']
        data.append(time_slice_data)

    combined_data = collections.defaultdict(list)

    for wp in wps:
        for time_slice_data in data:
            value = time_slice_data.get(wp, None)
            combined_data[wp].append(value)

    enriched_data = {}
    combined_data['test'] = []
    for wpname, values in combined_data.items():
        avg = sum(v if v is not None else 0 for v in values) / \
            len(values) if len(values) != 0 else 0

        enriched_data[wpname] = {
            'values': values,
            'avg': avg
        }

    res = sorted(enriched_data.values(), key=lambda k: -k['avg'])[:10]
    while len(res) < 10:
        res.append({'values': [None] * 10, 'avg': 0})

    # generate matrix
    matrix = []
    for p in res:
        values = [min(int(v//8), 9)
                  if v is not None else None for v in p['values']]
        matrix.append(values)

    return matrix


def main():
    matrix = get_matrix()
    print(matrix)


if __name__ == "__main__":
    main()
