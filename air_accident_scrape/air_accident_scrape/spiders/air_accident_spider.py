import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AirAccidentSpider(CrawlSpider):
    name = "air_accident_reports"
    allowed_domains = ["gov.uk"]
    start_urls = ["https://www.gov.uk/aaib-reports?page=1"]

    rules = (
        Rule(
            LinkExtractor(
                allow=["www.gov.uk/aaib-reports/"],
            ),
            callback="parse_report_page",
            follow=True
        ),
        Rule(
            LinkExtractor(
                restrict_css=".govuk-pagination__next"
            ),
            follow=True
        )
    )

    def parse_report_page(self, response):
        title = response.css(".gem-c-title__text::text").get()
        description = response.css(".gem-c-lead-paragraph::text").get()
        pdf_link = response.css(".attachment-inline a::attr(href)").get()

        yield {
            "title": title,
            "description": description,
            "pdf_link": pdf_link
        }
