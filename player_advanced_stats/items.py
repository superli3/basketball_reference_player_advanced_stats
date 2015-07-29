# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PlayerAdvancedStatsItem(Item):
    Player = Field()
    Season = Field()
    Age = Field()
    Team = Field()
    League = Field()
    Position = Field()
    Games = Field()
    Minutes_Played = Field()
    PER = Field()
    TS_Perc = Field()
    ThreePAr = Field()
    FTr = Field()
    ORB_Perc = Field()
    DRB_Perc = Field()
    TRB_Perc = Field()
    AST_Perc = Field()
    Steal_Perc = Field()
    Block_Perc = Field()
    TO_Perc = Field()
    USG = Field()
    OWS = Field()
    DWS = Field()
    WS = Field()
    WS48 = Field()
    OBPM = Field()
    DBPM = Field()
    BPM = Field()
    VORP = Field()
    pass
