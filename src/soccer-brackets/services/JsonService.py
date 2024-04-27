import json

class JsonService:
	def __init__(self, verbose = False) -> None:
		self.verbose = verbose

	def save_json(cls, file_path: str, content: dict | list) -> None:
		with open(file_path, "w") as fp:
			json.dump(content, fp, indent=4)
			if cls.verbose:
				print(f"{file_path} written successfully!")
	
	def load_json(cls, file_path: str) -> any:
		with open(file_path, "r") as fp:
			data = json.loads(fp.read())
			if cls.verbose:
				print(f"{file_path} loaded successfully!")
			return data