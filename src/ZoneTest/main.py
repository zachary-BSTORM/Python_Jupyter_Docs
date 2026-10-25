# from random import randint
# import tools

# def main():
#     print(randint(1,10))
#     tools.get_number()
#     tools.get_string()


# if __name__ == '__main__':
#     print("\033[31mTexte rouge\033[0m")
#     print("\033[32mTexte vert\033[0m")
#     print("\033[34mTexte bleu\033[0m")
#     main()


# list_values = [{name:"bob",age:30},{name:"boba",age:31},{name:"bobc",age:32}]

# list_values.sort(key=lambda v: v[age] )

# def divide(dividend : int, divisor : int)-> int:
#         # 50 / 25 = 2
#         v = divisor # 25
#         count = 1
#         while v <= dividend:
#             count += 1 # 2
#             v += divisor # 50
#             if v > dividend:
#                 count -= 1
#                 v -= divisor
#                 return count
#             else:
#                 return count # 2


# print(divide(75,3))

# class Map:
#     """Plateau de jeu représenté par une grille (liste de listes)."""

#     def __init__(self,):
#         self.grid: list[list[str]] = []

#     def create_map(self) -> None:
#         """Génère la grille : des murs '#' sur les bords, du sol '.' à l'intérieur."""
#         self.grid = []
#         for y in range(10):
#             row = []
#             for x in range(30):
#                 row.append("#")
#             self.grid.append(row)

#     def show_map(self) -> None:
#         """Affiche la grille dans la console, une ligne par rangée."""
#         for row in self.grid:
#             print("".join(row))


# if __name__ == "__main__":
#     game_map = Map()        # 10 lignes x 30 colonnes par défaut
#     game_map.create_map()
#     game_map.show_map()

from collections import deque
import timeit


# --- Pile (LIFO) avec une liste ---
stack = list(range(50000))

def test_stack(stack):
    return stack.pop()  # dépile le dernier

temps = timeit.timeit(lambda: test_stack(stack), number=50_000)
print(f"Pile  list.pop()      : {temps:.4f}s")


def test_stack_first(stack):
    return stack.pop(1)  # dépile le dernier
temps = timeit.timeit(lambda: test_stack(stack), number=50_000)
print(f"Pile  list.pop()      : {temps:.4f}s")



# --- File (FIFO) avec une liste ---
queue_list = list(range(50_000))

def test_queue_list(queue):
    return queue.pop(0)  # défile le premier, tout est décalé

temps = timeit.timeit(lambda: test_queue_list(queue_list), number=50_000)
print(f"File  list.pop(0)     : {temps:.4f}s")


# --- File (FIFO) avec une deque ---
queue = deque(range(50000))

def test_queue(queue):
    return queue.popleft()  # défile le premier, sans décalage

temps = timeit.timeit(lambda: test_queue(queue), number=50_000)
print(f"File  deque.popleft() : {temps:.4f}s")