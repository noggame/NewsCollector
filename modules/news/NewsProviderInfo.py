from enum import Enum
from modules.news.rss.MaeilRSS import MaeilNews


class URL(Enum):
    MEAIL   =   "https://www.mk.co.kr/rss/30100041/"

# matching service_name with (defined) provider_class
class RSS_PROVIDER(Enum):
    MEAIL   =   MaeilNews
