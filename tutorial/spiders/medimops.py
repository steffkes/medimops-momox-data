from datetime import datetime, timezone
import scrapy
import json


class MedimopsSpider(scrapy.Spider):
    name = "medimops"
    isbns = [
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

    def start_requests(self):
        for isbn in self.isbns:
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
