
from webscrip import wlog
from webscrip import wscrip

wlog.set_custom_log_info('html/error.log')

aljazeera_url = 'https://www.aljazeera.com/'

news_scrip = wscrip.NewsScraper(aljazeera_url, wlog)
#
news_scrip.retrieve_webpage()
news_scrip.write_webpage_as_html()

news_scrip.read_webpage_form_html()
news_scrip.convert_data_to_bs4()
news_scrip.print_data()
news_scrip.soup_to_convert_html()

