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

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.http.Request(
                url,
                headers={
                    "X-API-TOKEN": "2231443b8fb511c7b6a0eb25a62577320bac69b6",
                    "X-MARKETPLACE-ID": "momox_de",
                },
            )

    def parse(self, response):
        try:
            result = json.loads(response.body)
            result["_fetched_at"] = datetime.now(timezone.utc).isoformat()
            result["_source"] = "momox"
            yield result
        except json.decoder.JSONDecodeError as error:
            pass
