'''
https://adventofcode.com/2020/day/21
'''
DAY = 21

from utils import *
import regex as re
from collections import namedtuple, defaultdict


def parser(test=False):
    Recipe = namedtuple('Recipe',['ingredients', 'allergens'])
    input_raw = Input(DAY, 2020, test=test) 
    matcher = re.compile(r"(?:(\w+) )+\(contains (?:(\w+),? ?)+\)")
    recipes = []
    for line in input_raw:
        m = matcher.search(line)
        ingredients = set( m.captures(1) )
        allergens = set( m.captures(2) )
        # print(f'ingredients={ingredients}')
        # print(f'allergens={allergens}')
        recipes.append(Recipe(ingredients, allergens))

    return recipes


def match_allergens(input):
    found_ingredients = set([])
    found_allergens = set([])
    all_ingredients = set([])
    all_allergens = set([])

    for r, recipe in enumerate(input):
        all_ingredients.update(recipe.ingredients)
        all_allergens.update(recipe.allergens)

    possible_allergens = {allergen: all_ingredients.copy() for allergen in all_allergens}
    while True:
        for r, recipe in enumerate(input):
            for allergen in recipe.allergens:
                if allergen in found_allergens:
                    continue
                possible_allergens[allergen] = possible_allergens[allergen].intersection(recipe.ingredients) - found_ingredients
                if len(possible_allergens[allergen]) == 1: # Unique alergen found
                    found_ingredients.update(possible_allergens[allergen])
                    found_allergens.add(allergen)

        if len(found_allergens) == len(all_allergens):
            break

    return {allergen: ingredients.pop() for allergen, ingredients in possible_allergens.items()}


def part1(input):
    all_ingredients = set([])
    all_allergens = set([])
    for r, recipe in enumerate(input):
        all_ingredients.update(recipe.ingredients)
        all_allergens.update(recipe.allergens)

    allergen_list = match_allergens(input)

    # Count safe ingredients
    safe_ingredients = all_ingredients - set(allergen_list.values())
    counter = 0
    for r, recipe in enumerate(input):
        counter += len(recipe.ingredients.intersection(safe_ingredients))

    return counter


def part2(input):
    allergen_list = match_allergens(input)
    sorted_allergens = sorted(allergen_list.keys())
    dangerous_ingredients = [allergen_list[a] for a in sorted_allergens]
    return ','.join(dangerous_ingredients)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [5], part2, ['mxmxvkd,sqjhc,fvjkl'])
    main() 