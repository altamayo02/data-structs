from model.Cup import Cup
from view.PyGameGraph import PyGameGraph


def main():
	c = Cup("./src/soccer-brackets/view/ui/soccer-teams.ui")
	c.get_ui().show()
	pgg = PyGameGraph(c)
	pgg.run()

if __name__ == "__main__":
	main()