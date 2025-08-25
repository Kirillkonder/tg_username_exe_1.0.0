import time
import threading
import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext
from generators.base_generator import UsernameGenerator
from parser import FragmentParser
import sys
import os

class UsernameCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Username Checker")
        self.root.geometry("900x700")
        
        self.generator = UsernameGenerator()
        self.parser = FragmentParser()
        self.running = False
        self.available_usernames = []
        self.total_checked = 0
        self.total_found = 0
        self.start_time = None
        self.current_category = "4char"  # Категория по умолчанию
        self.current_algorithm = "suffix_prefix"  # ← ДОБАВЬТЕ ЭТУ СТРОЧКУ!
        self.batch_count = 0
        self.total_checked_since_restart = 0
        
        self.setup_ui()
   
    def setup_ui(self):
        # Create the tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Tab 1: Main (buttons and logs)
        self.main_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.main_frame, text="Main")
        
        # Tab 2: Available Usernames
        self.results_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.results_frame, text="Available Usernames")
        
        self.setup_main_tab()
        self.setup_results_tab()


    

    def setup_main_tab(self):
        # Top panel with buttons and category selection
        control_frame = ttk.Frame(self.main_frame)
        control_frame.pack(fill='x', padx=10, pady=10)
        
        # Create category selection frame
        category_frame = ttk.LabelFrame(control_frame, text="Select Category")
        category_frame.pack(side='left', fill='y', padx=5)
        
        self.category_var = tk.StringVar(value="4char")  # Default category
        
        algorithm_frame = ttk.LabelFrame(control_frame, text="Generation Algorithm")
        algorithm_frame.pack(side='left', fill='y', padx=5)
        
        self.algorithm_var = tk.StringVar(value="suffix_prefix")  # Алгоритм по умолчанию
        
        # Создать радиокнопки для выбора алгоритма
        ttk.Radiobutton(algorithm_frame, text="Suffix/Prefix", variable=self.algorithm_var, 
                    value="suffix_prefix", command=self.update_algorithm).pack(anchor='w')
        ttk.Radiobutton(algorithm_frame, text="Word Fusion", variable=self.algorithm_var, 
                    value="word_fusion", command=self.update_algorithm).pack(anchor='w')
        ttk.Radiobutton(algorithm_frame, text="Premium Names", variable=self.algorithm_var, 
                    value="premium", command=self.update_algorithm).pack(anchor='w')

        # Create radio buttons for category selection
        ttk.Radiobutton(category_frame, text="4-Character", variable=self.category_var, 
                       value="4char", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="5-Character", variable=self.category_var, 
                       value="5char", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="English Words", variable=self.category_var, 
                       value="english", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="SCAM Themed", variable=self.category_var, 
                       value="scam", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="NFT", variable=self.category_var, 
                       value="nft", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Telegram", variable=self.category_var, 
                       value="telegram", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Human Names", variable=self.category_var, 
                       value="humans", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Gods", variable=self.category_var, 
                       value="gods", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Rappers", variable=self.category_var, 
                       value="rappers", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Actors", variable=self.category_var, 
                       value="actors", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Brands", variable=self.category_var, 
                       value="brands", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Games", variable=self.category_var, 
                       value="games", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Memes", variable=self.category_var, 
                       value="memes", command=self.update_category).pack(anchor='w')
        ttk.Radiobutton(category_frame, text="Crypto", variable=self.category_var, 
                       value="crypto", command=self.update_category).pack(anchor='w')
        
        # Buttons control panel
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(side='right', fill='y', padx=5)
        
        # Add existing buttons
        self.start_button = ttk.Button(button_frame, text="▶️ Start", command=self.start_checking)
        self.start_button.pack(side='left', padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="⏹️ Stop", command=self.stop_checking, state='disabled')
        self.stop_button.pack(side='left', padx=5)
        
        self.save_button = ttk.Button(button_frame, text="💾 Save", command=self.save_results)
        self.save_button.pack(side='left', padx=5)
        
        self.refresh_button = ttk.Button(button_frame, text="🔄 Refresh", command=self.update_results_tab)
        self.refresh_button.pack(side='left', padx=5)
        
        # New Clear Button
        self.clear_button = ttk.Button(button_frame, text="🧹 Clear All", command=self.clear_all)
        self.clear_button.pack(side='left', padx=5)
        
        # Statistics and log display
        stats_frame = ttk.LabelFrame(self.main_frame, text="Statistics")
        stats_frame.pack(fill='x', padx=10, pady=5)
        
        self.stats_label = ttk.Label(stats_frame, text="Waiting for start...")
        self.stats_label.pack(padx=10, pady=5)
        
        # Logs
        log_frame = ttk.LabelFrame(self.main_frame, text="Real-time Logs")
        log_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=20, width=100)
        self.log_text.pack(fill='both', expand=True, padx=5, pady=5)
        self.log_text.config(state='disabled')

        
    def setup_results_tab(self):
        """Sets up the results tab with available usernames and click-to-copy functionality."""
        results_frame = ttk.Frame(self.results_frame)
        results_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        self.results_label = ttk.Label(results_frame, text="Available usernames not found")
        self.results_label.pack(pady=5)
        
        # Table columns (added 'copy' column for better structure)
        columns = ('username', 'price', 'status', 'response_time', 'url')
        self.results_tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=15)

        self.results_tree.heading('username', text='Username')
        self.results_tree.heading('price', text='💰 Price')
        self.results_tree.heading('status', text='Status')
        self.results_tree.heading('response_time', text='Response Time')
        self.results_tree.heading('url', text='URL')

        # Set column widths
        self.results_tree.column('username', width=120)
        self.results_tree.column('status', width=100)
        self.results_tree.column('response_time', width=80)
        self.results_tree.column('url', width=200)

        # Scrollbar for the table
        scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=scrollbar.set)
        
        self.results_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Bind click event for username cells
        self.results_tree.bind("<ButtonRelease-1>", self.on_item_click)  # Click event binding

    def update_algorithm(self):
        """Обновляет выбранный алгоритм генерации"""
        self.current_algorithm = self.algorithm_var.get()
        algorithm_names = {
            "suffix_prefix": "Suffix/Prefix",
            "word_fusion": "Word Fusion", 
            "premium": "Premium Names"
        }
        self.log_message(f"⚙️ Выбран алгоритм: {algorithm_names.get(self.current_algorithm, 'Suffix/Prefix')}")
        
    def update_category(self):
        """Обновляет выбранную категорию"""
        self.current_category = self.category_var.get()
        self.log_message(f"📁 Выбрана категория: {self.get_category_name()}")
        
    def get_category_name(self):
        """Возвращает название категории"""
        categories = {
            "4char": "4-символьные",
            "5char": "5-символьные", 
            "english": "Английские слова",
            "scam": "SCAM-тематика",
            "nft": "NFT",
            "telegram": "Telegram", 
            "humans": "Имена людей",
            "gods": "Боги",
            "rappers": "Рэперы",
            "actors": "Актеры", 
            "brands": "Бренды",
            "games": "Игры",
            "memes": "Мемы",
            "crypto": "Крипта"
        }
        return categories.get(self.current_category, "4-символьные")
    
    
        
    def log_message(self, message):
        """Adds a message to the real-time logs"""
        self.log_text.config(state='normal')
        self.log_text.insert('end', message + '\n')
        self.log_text.see('end')
        self.log_text.config(state='disabled')

    def clear_all(self):
        """Clears all logs and resets the displayed available usernames"""
        # Clear the logs in the UI
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)  # Clear all text in the log
        self.log_text.config(state='disabled')
        
        # Reset the list of available usernames
        self.available_usernames = []
        
        # Update the UI table to show no available usernames
        self.results_label.config(text="Available usernames not found")
        
        # Clear the treeview of results
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Reset statistics
        self.total_checked = 0
        self.total_found = 0
        self.total_checked_since_restart = 0
        self.batch_count = 0
        
        # Update statistics display
        self.update_stats()
        
        # Log the clearing action
        self.log_message("🧹 All logs and found usernames cleared!")
        
    def update_stats(self):
        """Обновляет статистику"""
        if self.start_time:
            elapsed = (datetime.now() - self.start_time).total_seconds()
            speed = self.total_checked / (elapsed / 60) if elapsed > 0 else 0
            
            stats_text = (f"📊 Проверено: {self.total_checked} | "
                         f"🎯 Найдено: {self.total_found} | "
                         f"🚀 Скорость: {speed:.0f}/мин | "
                         f"⏱️ Время: {elapsed:.0f} сек | "
                         f"📁 Категория: {self.get_category_name()} | "
                         f"🔄 С последнего перезапуска: {self.total_checked_since_restart} | "
                         f"🎲 Уникальных: {len(self.generator.used_usernames)}")
            self.stats_label.config(text=stats_text)
        
    def update_results_tab(self):
        """Updates the results tab with available usernames."""
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        if self.available_usernames:
            self.results_label.config(text=f"Found {len(self.available_usernames)} available usernames")
            
            # Insert usernames into the table and make them clickable
            for user in self.available_usernames:
                self.results_tree.insert('', 'end', values=(
                    user['username'],
                    user.get('price', 'N/A'),  # Add price column
                    user['status'],
                    f"{user['response_time']}s",
                    user['url']
                ))
        else:
            self.results_label.config(text="No available usernames found")

    def on_item_click(self, event):
        """Handles item click in the Treeview (when username is clicked)."""
        item = self.results_tree.selection()
        if item:
            username = self.results_tree.item(item[0])['values'][0]  # Get the username from the first column
            self.copy_to_clipboard(username)  # Copy the clicked username to the clipboard

    def copy_to_clipboard(self, username):
        """Copies the given username to the clipboard and shows feedback."""
        self.root.clipboard_clear()  # Clear current clipboard content
        self.root.clipboard_append(username)  # Add the username to the clipboard
        self.log_message(f"Copied {username} to clipboard")  # Optionally log the action
        
        # Update the results label with a copy confirmation message
        self.results_label.config(text=f"Copied Username: {username}")



    def save_results(self):
        """Сохраняет результаты в файл"""
        if not self.available_usernames:
            self.log_message("❌ Нет доступных юзернеймов для сохранения")
            return
            
        filename = f"available_usernames_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("🎯 ДОСТУПНЫЕ ЮЗЕРНЕЙМЫ НА FRAGMENT.COM\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Категория: {self.get_category_name()}\n")
                f.write(f"Всего проверено: {self.total_checked} юзернеймов\n")
                f.write(f"Найдено доступных: {len(self.available_usernames)}\n")
                f.write(f"Время начала: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Время сохранения: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for user in self.available_usernames:
                    f.write(f"🔹 Юзернейм: {user['username']}\n")
                    f.write(f"🔗 Ссылка:   {user['url']}\n")
                    f.write(f"📊 Статус:   {user['status']}\n")
                    f.write(f"⏱️  Время ответа: {user.get('response_time', 0)}с\n")
                    f.write("-" * 40 + "\n")
            
            self.log_message(f"💾 Сохранено в {filename}")
            
        except Exception as e:
            self.log_message(f"❌ Ошибка при сохранении: {e}")
            
    def start_checking(self):
        """Запускает проверку в отдельном потоке"""
        if not self.running:
            self.running = True
            self.start_time = datetime.now()
            self.available_usernames = []
            self.total_checked = 0
            self.total_found = 0
            self.batch_count = 0
            self.total_checked_since_restart = 0
            
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')
            
            self.log_message("🚀 Запуск проверки...")
            self.log_message(f"📁 Категория: {self.get_category_name()}")
            self.log_message("⏹️ Для остановки нажмите кнопку 'Стоп'")
            self.log_message("🔄 Автоперезапуск каждые 150 юзернеймов")
            self.log_message("=" * 50)
            
            # Запускаем в отдельном потоке
            self.check_thread = threading.Thread(target=self.run_continuous, daemon=True)
            self.check_thread.start()
            
    def stop_checking(self):
        """Останавливает проверку"""
        if self.running:
            self.running = False
            self.start_button.config(state='normal')
            self.stop_button.config(state='disabled')
            
            self.log_message("🛑 Проверка остановлена")
            self.log_message(f"🎯 Итого: {self.total_checked} проверено, {self.total_found} найдено")
            
            # Обновляем таблицу результатов после остановки
            self.update_results_tab()
            
    def soft_restart(self):
        """Мягкий перезапуск парсера для избежания блокировок"""
        self.log_message("🔄 Мягкий перезапуск парсера...")
        
        # Сохраняем текущие настройки
        current_category = self.current_category
        available_usernames = self.available_usernames.copy()
        total_checked = self.total_checked
        total_found = self.total_found
        start_time = self.start_time
        
        # Пересоздаем парсер и генератор
        self.parser = FragmentParser()
        self.generator = UsernameGenerator()
        
        # Восстанавливаем состояние
        self.current_category = current_category
        self.available_usernames = available_usernames
        self.total_checked = total_checked
        self.total_found = total_found
        self.start_time = start_time
        self.total_checked_since_restart = 0
        
        self.log_message("✅ Парсер перезапущен, продолжаем работу...")
            
    def check_batch(self):
        """Проверка одного батча юзернеймов"""
        usernames = self.generator.generate_batch(40, self.current_category, self.current_algorithm)
        self.log_message(f"🎲 Сгенерировано: {len(usernames)} юзернеймов")
        if usernames:
            self.log_message(f"📋 Примеры: {', '.join(usernames[:3])}...")
        
        results = self.parser.check_usernames_batch(usernames)
        
        # Обновляем статистику
        self.total_checked += len(usernames)
        self.total_checked_since_restart += len(usernames)
        
        # Анализируем результаты
        successful = sum(1 for r in results if r['success'])
        available = [r for r in results if r['available']]
        errors = len(results) - successful
        
        # Логируем результаты батча
        self.log_message(f"📊 Результаты батча:")
        self.log_message(f"   ✅ Успешных: {successful}/{len(usernames)}")
        self.log_message(f"   ❌ Ошибок: {errors}")
        self.log_message(f"   🎯 Доступных: {len(available)}")
        
        if available:
            self.available_usernames.extend(available)
            self.total_found += len(available)
            self.log_message(f"   🎉 НАЙДЕНО ДОСТУПНЫХ:")
            for user in available:
                self.log_message(f"      🔹 {user['username']} - {user['status']} ({user['response_time']}s)")
            
            # Обновляем таблицу результатов
            self.update_results_tab()
        
        return len(available)
    
    def run_continuous(self):
        """Бесконечный цикл проверки (запускается в потоке)"""
        batch_count = 0
        
        try:
            while self.running:
                batch_count += 1
                self.batch_count = batch_count
                
                self.log_message(f"\n📦 БАТЧ #{batch_count}")
                self.log_message("=" * 40)
                
                found = self.check_batch()
                
                # Обновляем статистику в UI
                self.root.after(0, self.update_stats)
                
                # Мягкий перезапуск каждые 150 проверенных юзернеймов
                if self.total_checked_since_restart >= 150:
                    self.soft_restart()
                
                # Очищаем историю каждые 10 батчей чтобы не засорять память
                if batch_count % 10 == 0:
                    self.generator.clear_used_usernames()
                    self.log_message("🧹 История юзернеймов очищена")
                
                # Короткая пауза между батчами
                time.sleep(2)
                
        except Exception as e:
            self.log_message(f"❌ Ошибка: {e}")
        finally:
            self.root.after(0, self.stop_checking)

def main():
    """Запуск приложения"""
    root = tk.Tk()
    app = UsernameCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


  