import os


def load_prompts_by_category(category: str, language: str) -> list[str]:
    path = f"data/prompts/{category}/{language}.txt"
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def list_categories() -> list[str]:
    base_path = "data/prompts/"
    return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]


def list_languages_in_category(category: str) -> list[str]:
    path = f"data/prompts/{category}"
    if not os.path.exists(path):
        return []
    return [
        f.split(".")[0]
        for f in os.listdir(path)
        if f.endswith(".txt")
    ]


def load_all_prompts(language: str) -> dict[str, list[str]]:
    prompts = {}
    categories = list_categories()
    for category in categories:
        prompts[category] = load_prompts_by_category(category, language)
    return prompts
