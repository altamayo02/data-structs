from model.Cup import Cup


def main():
	sc = Cup("./src/soccer-brackets/view/ui/soccer-teams.ui")
	sc.get_ui().show()

if __name__ == "__main__":
	main()