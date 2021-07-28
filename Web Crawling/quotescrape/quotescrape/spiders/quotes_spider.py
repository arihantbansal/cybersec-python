import scrapy


class QuotesSpider(scrapy.Spider):
  name = "quotes"
  # start_urls = {
  #     'http://quotes.toscrape.com/page/1/',
  #     'http://quotes.toscrape.com/page/2/',
  # }

  # New start_urls for recursive crawling
  start_urls = [
      'http://quotes.toscrape.com/page/1/',
  ]

  # Parse the pages in the start_urls and save as html files
  # def parse(self, response):
  #   page = response.url.split("/")[-2]
  #   filename = f"quotes-{page}.html"
  #   with open(filename, 'wb') as f:
  #     f.write(response.body)
  #   self.log(f'Saved file {filename}')

  # Parse the pages in start_urls and create JSON objects
  # def parse(self, response):
  #   for quote in response.css('div.quote'):
  #     yield {
  #         'text': quote.css('span.text::text').extract_first(),
  #         'author': quote.css('small.author::text').extract_first(),
  #         'tags': quote.css('div.tags a.tag::text').extract(),
  #     }

  # Parse the pages in start_urls and create JSON objects recursively
  def parse(self, response):
    for quote in response.css('div.quote'):
      yield {
          'text': quote.css('span.text::text').extract_first(),
          'author': quote.css('small.author::text').extract_first(),
          'tags': quote.css('div.tags a.tag::text').extract(),
      }

    next_page = response.css('li.next a::attr(href)').get()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)
