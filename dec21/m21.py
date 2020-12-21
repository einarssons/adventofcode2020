from dataclasses import dataclass
import re

line_pattern = re.compile(r"(?P<ingredients>[\w+ ]+) " +
                          r"\(contains (?P<allergenes>(\w+, )*\w+)\)$")


@dataclass
class Food:
    ingr_u: set()  # unknown ingredients
    allg_u: set()  # unknown allergenes
    ingr_k: set()  # known ingredients
    allg_k: set()  # known allergenes


def _analyze_food(line):

    match_obj = line_pattern.match(line)
    if match_obj is None:
        raise ValueError(f"Bad line {line}")
    gd = match_obj.groupdict()
    ingredients = set(gd['ingredients'].split())
    allergenes = {a.strip() for a in gd['allergenes'].split(",")}
    return Food(ingredients, allergenes, set(), set())


def parse_foods(data: str):
    return [_analyze_food(line) for line in data.splitlines()]


def reduce_foods(foods: [Food]):
    allg_map = {}  # Map allg to ingr
    all_ingr_u = set()
    all_allg_u = set()
    all_ingr_k = set()
    all_allg_k = set()

    for food in foods:
        all_ingr_u.update(food.ingr_u)
        all_allg_u.update(food.allg_u)

    while True:
        for allg in all_allg_u:
            rel_foods = []
            poss_ingr = set()
            for food in foods:
                if allg in food.allg_u:
                    rel_foods.append(food)
                    if poss_ingr == set():
                        poss_ingr = food.ingr_u.copy()
                    else:
                        poss_ingr.intersection_update(food.ingr_u)
            if len(poss_ingr) == 1:
                ingr = poss_ingr.pop()
                allg_map[allg] = ingr
                all_allg_u.remove(allg)
                all_allg_k.add(allg)
                all_ingr_u.remove(ingr)
                all_ingr_k.add(ingr)
                for food in foods:
                    if allg in food.allg_u:
                        food.allg_u.remove(allg)
                        food.allg_k.add(allg)
                    if ingr in food.ingr_u:
                        food.ingr_u.remove(ingr)
                        food.ingr_k.add(ingr)
                break
        else:
            break
        if len(all_allg_u) == 0:
            break
    nr_good_ingr = 0
    for food in foods:
        nr_good_ingr += len(food.ingr_u)
    return nr_good_ingr, allg_map


def main():
    data = open('foods.txt').read()
    foods = parse_foods(data)
    nr_good_ingr, allg_map = reduce_foods(foods)
    print(f"Nr good ingredients = {nr_good_ingr}")
    allg_sorted = list(allg_map.keys())
    allg_sorted.sort()
    ingredient_list = ",".join([allg_map[k] for k in allg_sorted])
    print("The ingredient list is:")
    print(ingredient_list)


if __name__ == "__main__":
    main()
