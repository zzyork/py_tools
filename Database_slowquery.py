# coding=utf-8
import re
from elasticsearch import Elasticsearch
import dingtalkchatbot.chatbot as cb
from bs4 import BeautifulSoup
import requests

es = Elasticsearch(["es.cp.qizuang.com"], http_auth=("elastic", "S8gl0c5kMPTOUEgthn8V"), port=80)
# start_time = (datetime.datetime.now()+datetime.timedelta(seconds=-2)).strftime("%Y-%m-%d"+"T"+"%H:%M:%S")

# end_time = (datetime.datetime.now()+datetime.timedelta(seconds=-1)).strftime("%Y-%m-%d"+"T"+"%H:%M:%S")

# elk_jump
response = es.search(
    index="filebeat-7.0.1",
    body={
        "aggs": {
            "2": {
                "terms": {
                    "field": "nginx.access.xff",
                    "size": 5,
                    "order": {
                        "_count": "desc"
                    }
                }
            }
        },
        "size": 0,
        "_source": {
            "excludes": []
        },
        "stored_fields": [
            "*"
        ],
        "script_fields": {},
        "query": {
            "bool": {
                "must": [
                    {
                        "query_string": {
                            "analyze_wildcard": "true",
                            "query": "event.dataset:nginx.access"
                        }
                    },
                    {
                        "match_phrase": {
                            "user_agent.device.name": {
                                "query": "Other"
                            }
                        }
                    },
                    {
                        "range": {
                            "@timestamp": {
                                "format": "strict_date_optional_time",
                                "gte": "now-10s"
                                # "lte": end_time
                            }
                        }
                    }
                ],
                "filter": [
                    {
                        "bool": {
                            "filter": [
                                {
                                    "bool": {
                                        "must_not": {
                                            "bool": {
                                                "should": [
                                                    {
                                                        "query_string": {
                                                            "fields": [
                                                                "url.original"
                                                            ],
                                                            "query": "*jpg*"
                                                        }
                                                    }
                                                ],
                                                "minimum_should_match": 1
                                            }
                                        }
                                    }
                                },
                                {
                                    "bool": {
                                        "filter": [
                                            {
                                                "bool": {
                                                    "must_not": {
                                                        "bool": {
                                                            "should": [
                                                                {
                                                                    "query_string": {
                                                                        "fields": [
                                                                            "url.original"
                                                                        ],
                                                                        "query": "*png*"
                                                                    }
                                                                }
                                                            ],
                                                            "minimum_should_match": 1
                                                        }
                                                    }
                                                }
                                            },
                                            {
                                                "bool": {
                                                    "filter": [
                                                        {
                                                            "bool": {
                                                                "must_not": {
                                                                    "bool": {
                                                                        "should": [
                                                                            {
                                                                                "query_string": {
                                                                                    "fields": [
                                                                                        "url.original"
                                                                                    ],
                                                                                    "query": "*gif*"
                                                                                }
                                                                            }
                                                                        ],
                                                                        "minimum_should_match": 1
                                                                    }
                                                                }
                                                            }
                                                        },
                                                        {
                                                            "bool": {
                                                                "filter": [
                                                                    {
                                                                        "bool": {
                                                                            "must_not": {
                                                                                "bool": {
                                                                                    "should": [
                                                                                        {
                                                                                            "query_string": {
                                                                                                "fields": [
                                                                                                    "url.original"
                                                                                                ],
                                                                                                "query": "*js*"
                                                                                            }
                                                                                        }
                                                                                    ],
                                                                                    "minimum_should_match": 1
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    {
                                                                        "bool": {
                                                                            "filter": [
                                                                                {
                                                                                    "bool": {
                                                                                        "must_not": {
                                                                                            "bool": {
                                                                                                "should": [
                                                                                                    {
                                                                                                        "query_string": {
                                                                                                            "fields": [
                                                                                                                "url.original"
                                                                                                            ],
                                                                                                            "query": "*css*"
                                                                                                        }
                                                                                                    }
                                                                                                ],
                                                                                                "minimum_should_match": 1
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "bool": {
                                                                                        "must_not": {
                                                                                            "bool": {
                                                                                                "should": [
                                                                                                    {
                                                                                                        "query_string": {
                                                                                                            "fields": [
                                                                                                                "url.original"
                                                                                                            ],
                                                                                                            "query": "*riji*"
                                                                                                        }
                                                                                                    }
                                                                                                ],
                                                                                                "minimum_should_match": 1
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            ]
                                                                        }
                                                                    }
                                                                ]
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "match_all": {}
                    }
                ],
                "should": [],
                "must_not": [
                    {
                        "match_phrase": {
                            "nginx.access.xff": {
                                "query": "-"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "nginx.access.xff": {
                                "query": "223.112.69.58"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "nginx.access.xff": {
                                "query": "112.28.67.42"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "nginx.access.xff": {
                                "query": "58.242.252.102"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "nginx.access.xff": {
                                "query": "112.81.16.122"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "nginx.access.xff": {
                                "query": "123.59.83.36"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "http.response.status_code": {
                                "query": "404"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "url.original": {
                                "query": "/orders/newnums"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "url.original": {
                                "query": "/assets/*"
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "url.original": {
                                "query": "/assets/*"
                            }
                        }
                    }
                ]
            }
        }
    }
)

url = 'http://m.ip138.com/ip.asp?ip='
kv = {'User-Agent': 'Mozilla/5.0'}

def IpQuery(ip):
    """查询IP地址并返回结果"""
    link = url + str(ip)
    try:
        r = requests.get(link, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'lxml')
        result = soup.select('p[class="result"]')[0].string
        return result
    except requests.HTTPError:
        print("查询失败")


def Es_Dingding(webhook):
    ding = cb.DingtalkChatbot(webhook)
    value = response.values()
    lists = re.findall(r".*?{'key': '(.*?)'.*?'doc_count': (.*?)}.*?", str(value), re.S)
    for item in lists:
        Attribution = IpQuery(item[0]).split('：')[-1]
        warning = '事件：%s  \n级别：%s  \nIP：%s \nIP归属地：%s \nIP查询: %s\n' % ("IP访问频次"+item[1], "严重", item[0], Attribution, "https://x.threatbook.cn/nodev4/ip/"+item[0])
        dangerous = '事件：%s  \n级别：%s  \nIP：%s \nIP归属地：%s \nIP查询: %s\n' % ("IP访问频次"+item[1], "较严重", item[0], Attribution, "https://x.threatbook.cn/nodev4/ip/"+item[0])
        very_dangerous = '事件：%s  \n级别：%s  \nIP：%s \nIP归属地：%s \nIP查询: %s\n' % ("IP访问频次"+item[1], "非常严重", item[0], Attribution, "https://x.threatbook.cn/nodev4/ip/"+item[0])
        if int(item[1]) >= int("100"):
            ding.send_text(msg=very_dangerous)
            print(very_dangerous)
        elif int("100") > int(item[1]) > int("50"):
            ding.send_text(msg=dangerous)
            print(dangerous)

# test
Es_Dingding('https://oapi.dingtalk.com/robot/send?access_token=0eddca58f77b5d110c7a93e1e7a7d911b2826feafe22f211a8494cd2d9c5f516')

# online
#Es_Dingding('https://oapi.dingtalk.com/robot/send?access_token=00dacc2e016cf4165af79132a237ca35d8fb1219c4997955a35c5256e56e388e')
