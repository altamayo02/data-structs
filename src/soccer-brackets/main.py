from model.Soccer import Criterias, SoccerCup, SoccerTeam

class Main:
	def __init__(self) -> None:
		pass

if __name__ == "__main__":
	sc = SoccerCup("./src/soccer-brackets/view/ui/soccer-teams.ui")
	sc.get_ui().show()
	print(sc.faceoff(SoccerTeam("A"), SoccerTeam("A"), Criterias.ACCURACY))