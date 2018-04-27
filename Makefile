help:
	@printf "[-----  We'll help you :-)  -----]\n\n"
	@printf "ex-annealing  : Run an exemple of annealing optimization\n"
	@printf "ger-req       : Generate pip requirements\n"
	@printf "\n[-----  Done!  -----]\n"

ex-annealing:
	@printf "[----- Run annealing example -----]\n\n"
	@python -m exemples.test_annealing_glass
	@printf "\n[----- Done! -----]\n"
ger-req:
	@printf "[----- Generating pip requirements -----]\n\n"
	@pip freeze > requirements.txt
	@printf "\n[----- Done! -----]\n"
inst-req:
	@printf "[----- Installing pip requirements -----]\n\n"
	@pip install requirements.txt
	@printf "\n[----- Done! -----]\n"

