from datetime import datetime, timezone
import scrapy
import json


class MedimopsSpider(scrapy.Spider):
    name = "medimops"

    def start_requests(self):
        for isbn in self.settings["ISBNS"]:
            yield scrapy.http.Request(
                f"https://www.medimops.de/produkte-C0/?fcIsSearch=1&searchparam={isbn}",
                meta={"isbn": isbn},
            )

    def parse(self, response):
        for variant in response.css("div.mxjs-variant-selector"):
            result = variant.attrib
            result["_isbn"] = response.meta["isbn"]
            result["_fetched_at"] = datetime.now(timezone.utc).isoformat()
            result["_source"] = self.name
            yield result
