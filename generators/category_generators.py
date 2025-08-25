import random
from typing import List
from .data import names_data as data
from .data import patterns
from .utils import generate_random_letters

class CategoryGenerators:
    
    # Основные методы генерации с поддержкой алгоритмов
    @staticmethod
    def generate_4char(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        """Генерация 4-символьных юзернеймов с выбором алгоритма"""
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, [''] * count)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, [''] * count)
        else:
            usernames = []
            patterns_list = ['cvcv', 'vcvc', 'cvc', 'vcv', 'vvcc', 'ccvv']
            vowels = 'aeiou'
            consonants = 'bcdfghjklmnpqrstvwxyz'
            
            for _ in range(count * 2):
                if len(usernames) >= count:
                    break
                    
                pattern = random.choice(patterns_list)
                username = ''
                
                for char in pattern:
                    if char == 'c':
                        username += random.choice(consonants)
                    elif char == 'v':
                        username += random.choice(vowels)
                    else:
                        username += char
                
                if username not in used_usernames:
                    usernames.append(username)
                    used_usernames.add(username)
            
            return usernames

    @staticmethod
    def generate_5char(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        """Генерация 5-символьных юзернеймов с выбором алгоритма"""
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, [''] * count)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, [''] * count)
        else:
            usernames = []
            patterns_list = ['cvcvc', 'vcvcv', 'cvccv', 'cvvcc', 'ccvvc']
            vowels = 'aeiou'
            consonants = 'bcdfghjklmnpqrstvwxyz'
            
            for _ in range(count * 2):
                if len(usernames) >= count:
                    break
                    
                pattern = random.choice(patterns_list)
                username = ''
                
                for char in pattern:
                    if char == 'c':
                        username += random.choice(consonants)
                    elif char == 'v':
                        username += random.choice(vowels)
                    else:
                        username += char
                
                if username not in used_usernames:
                    usernames.append(username)
                    used_usernames.add(username)
            
            return usernames

    @staticmethod
    def generate_english_words(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        """Генерация английских слов с выбором алгоритма"""
        all_words = (data.SCAM_WORDS + data.NFT_KEYWORDS + data.TELEGRAM_KEYWORDS +
                    data.HUMAN_NAMES + data.GOD_NAMES + data.RAPPER_NAMES + data.ACTOR_NAMES +
                    data.BRAND_NAMES + data.GAME_NAMES + data.MEME_NAMES + data.CRYPTO_NAMES)
        
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, all_words)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, all_words)
        else:
            valuable_words = [w for w in all_words if 4 <= len(w) <= 8]
            usernames = []
            
            for _ in range(count * 2):
                if len(usernames) >= count:
                    break
                    
                username = random.choice(valuable_words)
                
                if username not in used_usernames:
                    usernames.append(username)
                    used_usernames.add(username)
            
            return usernames

    # Основные методы для категорий с поддержкой алгоритмов
    @staticmethod
    def generate_scam(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.SCAM_WORDS)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.SCAM_WORDS)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.SCAM_WORDS)

    @staticmethod
    def generate_nft(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.NFT_KEYWORDS)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.NFT_KEYWORDS)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.NFT_KEYWORDS)

    @staticmethod
    def generate_telegram(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.TELEGRAM_KEYWORDS)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.TELEGRAM_KEYWORDS)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.TELEGRAM_KEYWORDS)

    @staticmethod
    def generate_humans(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.HUMAN_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.HUMAN_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.HUMAN_NAMES)

    @staticmethod
    def generate_gods(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.GOD_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.GOD_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.GOD_NAMES)

    @staticmethod
    def generate_rappers(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.RAPPER_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.RAPPER_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.RAPPER_NAMES)

    @staticmethod
    def generate_actors(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.ACTOR_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.ACTOR_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.ACTOR_NAMES)

    @staticmethod
    def generate_brands(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.BRAND_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.BRAND_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.BRAND_NAMES)

    @staticmethod
    def generate_games(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.GAME_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.GAME_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.GAME_NAMES)

    @staticmethod
    def generate_memes(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.MEME_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.MEME_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.MEME_NAMES)

    @staticmethod
    def generate_crypto(count: int, used_usernames: set, algorithm: str = "suffix_prefix") -> List[str]:
        if algorithm == "word_fusion":
            return CategoryGenerators.generate_word_fusion(count, used_usernames, data.CRYPTO_NAMES)
        elif algorithm == "premium":
            return CategoryGenerators.generate_premium_names(count, used_usernames, data.CRYPTO_NAMES)
        else:
            return CategoryGenerators._generate_single_words(count, used_usernames, data.CRYPTO_NAMES)

    @staticmethod
    def _generate_single_words(count: int, used_usernames: set, word_list: List[str]) -> List[str]:
        """Генерация только одиночных слов без комбинаций"""
        usernames = []
        filtered_words = [w for w in word_list if 4 <= len(w) <= 12]
        
        for _ in range(count * 3):
            if len(usernames) >= count:
                break
                
            username = random.choice(filtered_words)
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # НОВЫЕ АЛГОРИТМЫ ГЕНЕРАЦИИ
    @staticmethod
    def generate_word_fusion(count: int, used_usernames: set, word_list: List[str]) -> List[str]:
        """Алгоритм слияния слов (например: donaldroma)"""
        usernames = []
        filtered_words = [w for w in word_list if 3 <= len(w) <= 6]
        
        # Если список слов пустой, используем базовые паттерны
        if not filtered_words:
            vowels = 'aeiou'
            consonants = 'bcdfghjklmnpqrstvwxyz'
            filtered_words = [''.join([random.choice(consonants), random.choice(vowels), 
                                     random.choice(consonants)]) for _ in range(50)]
        
        for _ in range(count * 5):
            if len(usernames) >= count:
                break
                
            # Берем два случайных слова
            word1 = random.choice(filtered_words)
            word2 = random.choice(filtered_words)
            
            # Разные способы слияния
            fusion_methods = [
                lambda w1, w2: w1 + w2,  # простое соединение
                lambda w1, w2: w1 + w2[1:],  # убираем первую букву второго слова
                lambda w1, w2: w1[:-1] + w2,  # убираем последнюю букву первого слова
                lambda w1, w2: w1 + w2[2:],  # убираем первые две буквы второго слова
                lambda w1, w2: w1[:3] + w2,  # берем только первые 3 буквы первого
                lambda w1, w2: w1 + w2[-3:],  # берем только последние 3 буквы второго
                lambda w1, w2: w1[:2] + w2[1:],  # комбинированное
                lambda w1, w2: w1[:-2] + w2[2:]  # комбинированное
            ]
            
            username = random.choice(fusion_methods)(word1, word2).lower()
            
            # Ограничиваем длину
            if len(username) > 12:
                username = username[:12]
            
            if username not in used_usernames and 4 <= len(username) <= 12:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    @staticmethod
    def generate_premium_names(count: int, used_usernames: set, word_list: List[str]) -> List[str]:
        """Премиальный алгоритм для дорогих имен"""
        usernames = []
        
        # Отбираем только короткие слова (3-5 символов)
        premium_words = [w for w in word_list if 3 <= len(w) <= 5]
        
        # Если список слов пустой, создаем базовые короткие слова
        if not premium_words:
            vowels = 'aeiou'
            consonants = 'bcdfghjklmnpqrstvwxyz'
            premium_words = [''.join([random.choice(consonants), random.choice(vowels), 
                                    random.choice(consonants)]) for _ in range(30)]
            premium_words += [''.join([random.choice(consonants), random.choice(vowels), 
                                     random.choice(consonants), random.choice(vowels)]) for _ in range(20)]
        
        # Паттерны для премиальных имен
        patterns = ['cvc', 'vcv', 'cvcv', 'vcvc', 'cvcvc', 'vcvcv', 'cvvc', 'cvvv', 'vccv']
        
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        for _ in range(count * 10):
            if len(usernames) >= count:
                break
            
            # 50% chance использовать премиальное слово, 50% использовать паттерн
            if random.random() < 0.5 and premium_words:
                username = random.choice(premium_words)
                
                # Добавляем цифры или специальные символы для уникальности
                if random.random() < 0.3:
                    username += str(random.randint(1, 99))
            else:
                # Генерация по паттерну
                pattern = random.choice(patterns)
                username = ''
                
                for char in pattern:
                    if char == 'c':
                        username += random.choice(consonants)
                    elif char == 'v':
                        username += random.choice(vowels)
                    else:
                        username += char
            
            # Обеспечиваем короткую длину для премиальности
            if len(username) > 8:
                username = username[:8]
            
            if username not in used_usernames and 3 <= len(username) <= 8:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # КРЕАТИВНЫЕ МЕТОДЫ ДЛЯ БЕСКОНЕЧНОЙ ГЕНЕРАЦИИ (без двойных имен)
    @staticmethod
    def generate_creative_patterns(count: int, used_usernames: set) -> List[str]:
        """Бесконечная генерация по паттернам"""
        usernames = []
        patterns_list = ['cvcv', 'vcvc', 'cvc', 'vcv', 'vvcc', 'ccvv', 
                        'cvcvc', 'vcvcv', 'cvccv', 'cvvcc', 'ccvvc']
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        for _ in range(count * 3):
            if len(usernames) >= count:
                break
                
            pattern = random.choice(patterns_list)
            username = ''
            
            for char in pattern:
                if char == 'c':
                    username += random.choice(consonants)
                elif char == 'v':
                    username += random.choice(vowels)
                else:
                    username += char
            
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    @staticmethod
    def generate_creative_words(count: int, used_usernames: set) -> List[str]:
        """Креативная генерация слов без двойных имен"""
        usernames = []
        
        patterns_list = ['cvcvcv', 'vcvcvc', 'cvcvcv', 'vcvcvcv']
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        for _ in range(count * 4):
            if len(usernames) >= count:
                break
                
            pattern = random.choice(patterns_list)
            username = ''
            
            for char in pattern:
                if char == 'c':
                    username += random.choice(consonants)
                elif char == 'v':
                    username += random.choice(vowels)
                else:
                    username += char
            
            if random.random() < 0.3:
                suffix = random.choice(['er', 'or', 'ar', 'ist', 'ian', 'able', 'ible', 'ful', 'less', 'ness'])
                username = username + suffix
            
            if len(username) > 12:
                username = username[:12]
            
            if username not in used_usernames and 4 <= len(username) <= 12:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # Креативные методы для каждой категории (без двойных имен)
    @staticmethod
    def generate_creative_scam(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.SCAM_WORDS)

    @staticmethod
    def generate_creative_nft(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.NFT_KEYWORDS)

    @staticmethod
    def generate_creative_telegram(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.TELEGRAM_KEYWORDS)

    @staticmethod
    def generate_creative_names(count: int, used_usernames: set) -> List[str]:
        names = data.HUMAN_NAMES + data.GOD_NAMES + data.RAPPER_NAMES + data.ACTOR_NAMES
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, names)

    @staticmethod
    def generate_creative_gods(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.GOD_NAMES)

    @staticmethod
    def generate_creative_rappers(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.RAPPER_NAMES)

    @staticmethod
    def generate_creative_actors(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.ACTOR_NAMES)

    @staticmethod
    def generate_creative_brands(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.BRAND_NAMES)

    @staticmethod
    def generate_creative_games(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.GAME_NAMES)

    @staticmethod
    def generate_creative_memes(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.MEME_NAMES)

    @staticmethod
    def generate_creative_crypto(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.CRYPTO_NAMES)

    @staticmethod
    def _generate_creative_with_suffixes(count: int, used_usernames: set, word_list: List[str]) -> List[str]:
        """Генерация с дополнительными суффиксами и приставками"""
        usernames = []
        filtered_words = [w for w in word_list if 3 <= len(w) <= 8]
        
        prefixes = ['pre', 'un', 're', 'ex', 'in', 'dis', 'anti', 'bio', 'auto', 'inter', 'sub']
        suffixes = ['er', 'or', 'ist', 'ian', 'able', 'ible', 'ful', 'less', 'ness', 'ment', 'tion', 'sion', 'ity', 'ly']
        
        for _ in range(count * 4):
            if len(usernames) >= count:
                break
                
            base_word = random.choice(filtered_words)
            
            if random.random() < 0.6:
                suffix = random.choice(suffixes)
                username = base_word + suffix
            else:
                prefix = random.choice(prefixes)
                username = prefix + base_word
            
            if len(username) > 12:
                username = username[:12]
            
            if username not in used_usernames and 4 <= len(username) <= 12:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames