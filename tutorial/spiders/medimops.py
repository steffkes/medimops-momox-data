from datetime import datetime, timezone
import scrapy
import json


class MedimopsSpider(scrapy.Spider):
    name = "medimops"
    start_urls = [
        f"https://www.medimops.de/produkte-C0/?fcIsSearch=1&searchparam={isbn}"
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
        product = None
        for data in response.css("script[type='application/ld+json']::text").getall():
            parsed = json.loads(data)
            if parsed["@type"] == "Product":
                product = parsed

        for variant in response.css("div.mxjs-variant-selector"):
            result = variant.attrib
            result["_isbn"] = product["gtin13"]
            result["_fetched_at"] = datetime.now(timezone.utc).isoformat()
            result["_source"] = "medimops"
            yield result
