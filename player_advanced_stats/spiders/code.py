__author__ = 'Jeff'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from player_advanced_stats.items import PlayerAdvancedStatsItem

class BaseSpider(BaseSpider):
    name = "players_advanced_stats"
    allowed_domains = ["basketball-reference.com"]
    start_urls = [l.strip() for l in open("allplayers.txt", "rw+").readlines()]
    download_delay = 4
    randomize_download_delay = True
    retry_times = 30
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//table[@id="advanced"]/tbody/tr')
        items = []
        for titles in titles:
            item = PlayerAdvancedStatsItem()
            item ["Player"] = hxs.select("//h1/text()").extract()
            item ["Season"] = titles.select("td[1]//text()").extract()
            item ["Age"] = titles.select("td[2]/text()").extract()
            item ["Team"] = titles.select("td[3]/a/text()").extract()
            item ["League"] = titles.select("td[4]/a/text()").extract()
            item ["Position"] = titles.select("td[5]/text()").extract()
            item ["Games"] = titles.select("td[6]/text()").extract()
            item ["Minutes_Played"] = titles.select("td[7]/text()").extract()
            item ["PER"] = titles.select("td[8]/text()").extract()
            item ["TS_Perc"] = titles.select("td[9]/text()").extract()
            item ["ThreePAr"] = titles.select("td[10]/text()").extract()
            item ["FTr"] = titles.select("td[11]/text()").extract()
            item ["ORB_Perc"] = titles.select("td[12]/text()").extract()
            item ["DRB_Perc"] = titles.select("td[13]/text()").extract()
            item ["TRB_Perc"] = titles.select("td[14]/text()").extract()
            item ["AST_Perc"] = titles.select("td[15]/text()").extract()
            item ["Steal_Perc"] = titles.select("td[16]/text()").extract()
            item ["Block_Perc"] = titles.select("td[17]/text()").extract()
            item ["TO_Perc"] = titles.select("td[18]/text()").extract()
            item ["USG"] = titles.select("td[19]/text()").extract()
            item ["OWS"] = titles.select("td[21]/text()").extract()
            item ["DWS"] = titles.select("td[22]/text()").extract()
            item ["WS"] = titles.select("td[23]/text()").extract()
            item ["WS48"] = titles.select("td[24]/text()").extract()
            item ["OBPM"] = titles.select("td[26]/text()").extract()
            item ["DBPM"] = titles.select("td[26]/text()").extract()
            item ["BPM"] = titles.select("td[28]/text()").extract()
            item ["VORP"] = titles.select("td[29]/text()").extract()
            items.append(item)
        return items
