from requests import Session

class MetaphorpSum:
	def __init__(self) -> None:
		self.api = "http://metaphorpsum.com"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_sentences(self, count: int) -> str:
		return self.session.get(
			f"{self.api}/sentences/{count}").text

	def get_paragraphs(self, count: int) -> str:
		return self.session.get(
			f"{self.api}/paragraphs/{count}").text

	def get_paragraphs_with_sentences(
			self,
			paragraphs_count: int,
			sentences_count: int) -> str:
		return self.session.get(
			f"{self.api}/paragraphs/{paragraphs_count}/sentences_count").text
