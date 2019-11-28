	from bs4 import BeautifulSoup as html_parser
  soup = html_parser('<html>'+html_source+'</html>', 'html.parser')
	new_table_tags = soup.findAll(et)
