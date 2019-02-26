import scrapy
from random import randint

class BatdongsanTintucSpider(scrapy.Spider):
	name = "locatefamily"
	BASE_URL = 'https://www.locatefamily.com/'
	count = 1
	def start_requests(self):
		url = self.BASE_URL
		yield scrapy.Request(url=url, callback=self.parse)

	def parse(self,response):
		links = ['/Street-Lists/Vietnam/index-1.html']
		print('******************Links*******************')
		print(links)
		while self.count < 14237:
			self.count = self.count + 1
			link = '/Street-Lists/Vietnam/index-' + str(self.count) + '.html'
			links.append(link)

		for link in links:
			link = response.urljoin(link)
			print('***********link_update********************')
			print(link)
			yield scrapy.Request(link, callback=self.parse_content)
			print('*********yield_parse***********')

	def parse_content(self, response):
		print("***********Content**********")
		address = response.css('#1 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#1 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#1 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#2 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#2 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#2 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#3 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#3 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#3 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#4 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#4 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#4 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#5 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#5 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#5 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#6 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#6 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#6 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#7 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#7 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#7 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#8 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#8 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#8 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#9 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#9 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#9 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#10 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#10 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#10 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#11 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#11 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#11 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#12 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#12 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#12 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#13 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#13 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#13 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#14 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#14 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#14 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#15 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#15 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#15 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#16 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#16 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#16 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#17 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#17 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#17 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#18 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#18 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#18 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#19 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#19 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#19 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#20 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#20 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#20 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#21 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#21 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#21 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#22 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#22 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#22 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#23 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#23 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#23 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#24 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#24 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#24 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#25 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#25 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#25 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#26 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#26 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#26 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#27 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#27 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#27 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#28 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#28 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#28 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#29 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#29 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#29 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#30 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#30 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#30 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#31 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#31 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#31 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#32 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#32 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#32 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#33 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#33 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#33 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#34 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#34 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#34 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#35 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#35 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#35 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#36 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#36 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#36 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#37 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#37 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#37 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#38 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#38 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#38 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#39 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#39 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#39 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#40 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#40 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#40 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#41 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#41 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#41 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#42 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#42 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#42 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#43 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#43 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#43 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#44 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#44 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#44 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#45 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#45 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#45 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#46 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#46 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#46 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#47 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#47 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#47 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#48 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#48 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#48 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#49 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#49 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#49 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#50 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#50 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#50 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#51 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#51 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#51 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#52 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#52 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#52 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#53 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#53 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#53 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#54 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#54 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#54 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#55 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#55 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#55 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#56 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#56 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#56 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#57 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#57 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#57 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#58 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#58 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#58 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#59 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#59 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#59 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		address = response.css('#60 span::text').extract_first().lstrip().rstrip()
		phone_name = response.css('#60 a::text').extract()
		if len(phone_name) == 4:
			phone =phone_name[0].lstrip().rstrip()
			first_name = phone_name[1].lstrip().rstrip()
		else:
			phone = ''
			first_name = phone_name[0].lstrip().rstrip()
		last_name = response.css('#60 b::text').extract_first().lstrip().rstrip()
		name = first_name + ' ' + last_name
		yield {'name': name, 'phone': phone, 'address': address}

		print('********yield_parse_content*********')