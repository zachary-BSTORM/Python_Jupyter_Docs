note = int(input("Entrez votre note : "))

if 0 <= note <= 20:
    match note:
        case _ if note > 18:
            print("TB")
        case _ if 15 < note <= 18:
            print("B")
        case _ if 13 < note < 15:
            print("S")
        case _ if 10 < note < 13:
            print("I")
        case _ if note < 10:
            print("IG")
    