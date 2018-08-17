help:
	@printf "[-----  We'll help you :-)  -----]\n\n"
	@printf "ex-annealing  : Run an exemple of annealing optimization\n"
	@printf "ger-req       : Generate pip requirements\n"
	@printf "inst-req      : Install the requirements file with pip\n"
	@printf "gui           : Starting the Glass Generator GUI\n"
	@printf "gui-db        : Starting the Glass Generator GUI in debug mode\n"
	@printf "\n[-----  Done!  -----]\n"

ex-annealing:
	@printf "[----- Run annealing example -----]\n\n"
	@python -m examples.test_annealing_glass
	@printf "\n[----- Done! -----]\n"
ger-req:
	@printf "[----- Generating pip requirements -----]\n\n"
	@pip freeze > requirements.txt
	@printf "\n[----- Done! -----]\n"
inst-req:
	@printf "[----- Installing pip requirements -----]\n\n"
	@pip install requirements.txt
	@printf "\n[----- Done! -----]\n"
gui:	
	@printf "[----- Starting GUI -----]\n\n"
	@cd gg_gui/ ; python main.py
	@printf "\n[----- Done! -----]\n"
gui-db:	
	@printf "[----- Starting GUI (debug) -----]\n\n"
	@cd gg_gui/ ; python -v main.py
	@printf "\n[----- Done! -----]\n"
run-exp:
	@python3.6 -m experiments.testing_pso_ann_rand.main > experiments/testing_pso_ann_rand/out.txt
