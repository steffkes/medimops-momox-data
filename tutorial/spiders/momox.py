from datetime import datetime, timezone
import scrapy
import json


class MomoxSpider(scrapy.Spider):
    name = "momox"

    def start_requests(self):
        for isbn in self.settings["ISBNS"]:
            yield scrapy.http.Request(
                f"https://api.momox.de/api/v4/offer/?ean={isbn}",
                headers={
                    "X-API-TOKEN": "2231443b8fb511c7b6a0eb25a62577320bac69b6",
                    "X-MARKETPLACE-ID": "momox_de",
                },
            )

    def parse(self, response):
        try:
            result = json.loads(response.body)
            result["_fetched_at"] = datetime.now(timezone.utc).isoformat()
            result["_source"] = self.name
            yield result
        except json.decoder.JSONDecodeError as error:
            pass
