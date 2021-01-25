from datetime import datetime, timezone
import scrapy
import json


class MomoxSpider(scrapy.Spider):
    name = "momox"
    start_urls = [
        f"https://api.momox.de/api/v4/offer/?ean={isbn}"
        for isbn in [
            "9783423209694",
            "9783527507993",
            "9783593398532",
            "9783958751750",
            "9781101886724",
            "9783734104091",
            "9783947188857",
            "9783446414396",
            "9783548289199",
            "9783548289212",
            "9783548289229",
            "9781101886694",
            "9781101904220",
            "9783548060224",
            "9781409168744",
            "9781409168799",
        ]
    ]

    def parse(self, response):
        try:
            result = json.loads(response.body)
            result["_fetched_at"] = datetime.now(timezone.utc).isoformat()
            result["_source"] = "momox"
            yield result
        except json.decoder.JSONDecodeError as error:
            print("%s | json oy" % response.status)
