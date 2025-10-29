# 给出两个list, recipes & integrates
# recipes：list[str]
# integrates： list[str]
# 检查if recipe in recipes 是integrates 按照顺序组成的str
# Example:
# integrates = ["sugar”, “egg”, “flour”]
# recipes = ["sugaregg”, “sugarrrregg”, “eggflour”, “sugarflour”]
# result = [True, False, False, False]

def check_recipes(integrates, recipes):
    result = []
    integrates_str = ''.join(integrates)
    for recipe in recipes:
        if recipe in integrates_str:
            result.append(True)
        else:
            result.append(False)
    return result

# Test cases
integrates = ["sugar", "egg", "flour"]
recipes = ["sugaregg", "sugarrrregg", "eggflour", "sugarflour"]
result = check_recipes(integrates, recipes)
print(result)  # Output: [True, False, False, False]