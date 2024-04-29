from model.Soccer import Criterias, Cup, Team


class Main:
	def __init__(self) -> None:
		pass

if __name__ == "__main__":
	sc = Cup("./src/soccer-brackets/view/ui/soccer-teams.ui")
	sc.get_ui().show()