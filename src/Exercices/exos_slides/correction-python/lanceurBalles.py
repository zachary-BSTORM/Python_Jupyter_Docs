balls : int = 0
ready = False

answer_ready = input("Etes vous prêt ? y - n")

answer_balls = int(input("Combien de balles sont dans la machine ? "))


if answer_ready and answer_balls > 0:
    print("c'est parti !")
elif answer_ready and answer_balls < 0:
    print("vous devez mettre des balles ")
elif not answer_ready and answer_balls > 0:
    print("Revenez quand vous serez prêt ")