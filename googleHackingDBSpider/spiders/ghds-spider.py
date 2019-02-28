import scrapy
from googleHackingDBSpider.items import GooglehackingdbspiderItem
class Googlehackingdbspider(scrapy.Spider):
    name = "ghds"

    def start_requests(self):
        urls = [
                'https://www.exploit-db.com/google-hacking-database/'
                ]
        for url in urls:
            yield scrapy.Request(url=url, headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36", "cookie": "_ga=GA1.3.285903915.1532398319; _gid=GA1.3.1544326454.1532398319; PHPSESSID=c4hn8c2025h9ohf4tp6atgh4j4; _gat=1"}, callback=self.parse)

    def parse(self, res):
        #next_page = res.css('div.pagination').css('a.color::attr(href)').extract()[1]
        table = res.css('table.category-list') 
        i = 0
        tbody = table.css('tbody')
        trs = tbody.css('tr')
        for tr in trs:
            item = GooglehackingdbspiderItem()
            tds = tr.css('td')
            i = i + 1
            item['date'] = tds[0].css('td::text').extract_first().strip()
            item['hackStr'] = tds[1].css('td').css('a::text').extract_first().strip()
            item['hackStrLink'] = tds[1].css('td').css('a::attr(href)').extract_first().strip()
            item['Category'] = tds[2].css('td').css('a::text').extract_first().strip()
            item['CategoryLink'] = tds[2].css('td').css('a::attr(href)').extract_first().strip()
            yield item
        print "cnt: ", i
       #print "next_page:", next_page
       # if next_page:
       #     print "netxt page..."
       #     #yield res.follow(next_page, self.parse) 
       #     next_page = res.urljoin(next_page)
