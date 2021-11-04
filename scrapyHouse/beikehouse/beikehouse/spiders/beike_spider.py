import scrapy
import re
import json


class BeikeSpider(scrapy.Spider):
    name = 'beike_spider'
    def start_requests(self):
        for i in range(1,21):
            url = "https://wh.ke.com/ershoufang/pg"+str(i)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                'Cookie': 'lianjia_uuid=a1b3cd58-a4a5-41e1-929e-6cfdc6a0e357; ke_uuid=d24006d3216c0a22704af242baf73b7a; login_ucid=2000000097647619; lianjia_token=2.0013db086b6f9399840276215a1b81bfcc; lianjia_token_secure=2.0013db086b6f9399840276215a1b81bfcc; security_ticket=dzyHCUhccnnVzlKyVLw9nQZnULSPvTqsV1xvAJdn+a68XUb6YTvRPMFUyQrFFiIdADJXZ94F6XENkkMhT8bGOu39cGeLTYnKStn2VP1HJioNXLf8/Majl27VEditOxlAnhsSO2lu2v9go6MFsrvmNMife92U0eIaRgtbwIzXa2s=; _ga=GA1.2.929676495.1627567741; __xsptplus788=788.1.1627567741.1627567741.1%234%7C%7C%7C%7C%7C%23%23r_2sRk8-x6fpuCG7GrBchRsbdTD4Gk4g%23; select_city=420100; digv_extends=%7B%22utmTrackId%22%3A%2280419593%22%7D; lianjia_ssid=41c94662-d0a2-416f-805c-b3b3391240c4; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1627563927,1627567752,1627799306,1627804368; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217a296d9349385-058c32df967836-4373266-1440000-17a296d934b4f%22%2C%22%24device_id%22%3A%2217a296d9349385-058c32df967836-4373266-1440000-17a296d934b4f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wywuhan%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1627804428; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMmU0ZTRiODRiMDQ2ZjhlMjVlZTMwMGUzZmQzMmZiYTk4N2UwOGQxNDUzMzIyYjEyOTEwMmMxYzc4NjUwMGU5NWVhYWM4ZmRhMjE2MzRlYmFlZWE1MWU0NzNmZDlkNmEyZTk1MDdiYmQwYjBiMTcyMzAyMmNjYTNkNDkyZTgwM2M5ZGM2MGQ4ZmUzNTI4YzlkODkxMWM3ZmE0NWEzNWEzZTEwNTUzZmQzMmM5Y2Y1YmUyMmQ4YzM2YzMzNjJiMjdkOGE3Y2M0NGQxOWFiOWI3MmRlMjM0MjkyYTVkNTRlZmE2Y2UyMTljYmI3MzJmYzBlMzU4ZGM4NzNlYTQ0YWM1YjZlMDNjMWFkOTcwZDNiNTIzZjdkOTgzMTZkOTg2ZWYzYjcxMDZmNGM1MTA0ZTNlNDRiNTIzMmNkZTBlYTI4ZTBcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiNjM5YzYzNWZcIn0iLCJyIjoiaHR0cHM6Ly93aC5rZS5jb20vZXJzaG91ZmFuZy9wZzEvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='
            }
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        title_list = response.xpath('//*[@class="VIEWDATA CLICKDATA maidian-detail"]/text()').extract()
        print(title_list)
        totalprice_list = response.xpath('//*[@class="totalPrice"]/span/text()').extract()
        for index,value in enumerate(totalprice_list):
            totalprice_list[index]=value.strip()
        print(totalprice_list)
        houseinfo_list=response.xpath('//*[@class="houseInfo"]/text()').extract()
        new_houseinfo_list=[]
        for i in range(1,60,2):
            new_houseinfo_list.append(houseinfo_list[i].strip())
        print(new_houseinfo_list)