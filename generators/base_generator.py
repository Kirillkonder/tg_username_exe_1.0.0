import random
from typing import List, Set
from . import category_generators as cg
from .utils import should_clear_memory
import os

def load_used_usernames(filename="used_usernames.txt"):
    """Загружает все использованные юзернеймы из файла"""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file.readlines())
    return set()

def save_used_usernames(usernames, filename="used_usernames.txt"):
    """Сохраняет все использованные юзернеймы в файл"""
    with open(filename, "a", encoding="utf-8") as file:
        for username in usernames:
            file.write(f"{username}\n")

class UsernameGenerator:
    def __init__(self):
        self.used_usernames = load_used_usernames()  # Загружаем использованные юзернеймы
        self.generation_attempts = 0
        self.max_attempts_per_batch = 3000

    def should_clear_memory(self) -> bool:
        return should_clear_memory(self.used_usernames, self.generation_attempts)

    def generate_batch(self, count: int, category: str = "4char", algorithm: str = "suffix_prefix") -> List[str]:
        """Генерация батча юзернеймов по категории и алгоритму"""
        if self.should_clear_memory():
            self.clear_used_usernames()

        # Основные генераторы
        primary_generators = {
            "4char": lambda c, u: cg.CategoryGenerators.generate_4char(c, u, algorithm),
            "5char": lambda c, u: cg.CategoryGenerators.generate_5char(c, u, algorithm),
            "english": lambda c, u: cg.CategoryGenerators.generate_english_words(c, u, algorithm),
            "scam": lambda c, u: cg.CategoryGenerators.generate_scam(c, u, algorithm),
            "nft": lambda c, u: cg.CategoryGenerators.generate_nft(c, u, algorithm),
            "telegram": lambda c, u: cg.CategoryGenerators.generate_telegram(c, u, algorithm),
            "humans": lambda c, u: cg.CategoryGenerators.generate_humans(c, u, algorithm),
            "gods": lambda c, u: cg.CategoryGenerators.generate_gods(c, u, algorithm),
            "rappers": lambda c, u: cg.CategoryGenerators.generate_rappers(c, u, algorithm),
            "actors": lambda c, u: cg.CategoryGenerators.generate_actors(c, u, algorithm),
            "brands": lambda c, u: cg.CategoryGenerators.generate_brands(c, u, algorithm),
            "games": lambda c, u: cg.CategoryGenerators.generate_games(c, u, algorithm),
            "memes": lambda c, u: cg.CategoryGenerators.generate_memes(c, u, algorithm),
            "crypto": lambda c, u: cg.CategoryGenerators.generate_crypto(c, u, algorithm)
        }
            
        # Креативные генераторы для бесконечной генерации
        creative_generators = {
            "4char": cg.CategoryGenerators.generate_creative_patterns,
            "5char": cg.CategoryGenerators.generate_creative_patterns,
            "english": cg.CategoryGenerators.generate_creative_words,
            "scam": cg.CategoryGenerators.generate_creative_scam,
            "nft": cg.CategoryGenerators.generate_creative_nft,
            "telegram": cg.CategoryGenerators.generate_creative_telegram,
            "humans": cg.CategoryGenerators.generate_creative_names,
            "gods": cg.CategoryGenerators.generate_creative_gods,
            "rappers": cg.CategoryGenerators.generate_creative_rappers,
            "actors": cg.CategoryGenerators.generate_creative_actors,
            "brands": cg.CategoryGenerators.generate_creative_brands,
            "games": cg.CategoryGenerators.generate_creative_games,
            "memes": cg.CategoryGenerators.generate_creative_memes,
            "crypto": cg.CategoryGenerators.generate_creative_crypto
        }

        # Сначала пробуем основной генератор
        primary_gen = primary_generators.get(category, cg.CategoryGenerators.generate_4char)
        usernames = primary_gen(count, self.used_usernames)
        
        # Если не хватило - используем креативный генератор
        if len(usernames) < count:
            remaining = count - len(usernames)
            creative_gen = creative_generators.get(category, cg.CategoryGenerators.generate_creative_patterns)
            creative_usernames = creative_gen(remaining, self.used_usernames)
            usernames.extend(creative_usernames)

        self.generation_attempts += count

        # Сохраняем новые юзернеймы в файл
        save_used_usernames(usernames)
        
        print(f"🎲 Сгенерировано {len(usernames)} юзернеймов (категория: {category})")
        if usernames:
            print(f"📋 Примеры: {', '.join(usernames[:3])}...")

        return usernames

    def clear_used_usernames(self):
        """Очистка истории использованных юзернеймов"""
        self.used_usernames.clear()
        self.generation_attempts = 0
        print("🧹 История юзернеймов очищена")
