import tkinter as tk
import requests
import threading

class NewsBar:
    def __init__(self, parent, github_url, height=60, bg="black", fg="white"):
        self.github_url = github_url
        self.news = ["جارٍ تحميل الأخبار..."]
        self.current_news_index = 0
        self.current_news = self.news[0]
        self.x_position = 800

        # إعداد شريط الأخبار
        self.canvas = tk.Canvas(parent, height=height, bg=bg, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.fg = fg

        # بدء التحديثات
        self.fetch_news_periodically()
        self.update_news()
        self.move_news()

    def fetch_news(self):
        try:
            response = requests.get(self.github_url)
            if response.status_code == 200:
                data = response.json()
                return data.get("news", [])
            else:
                return ["خطأ في تحميل الأخبار."]
        except Exception as e:
            return [f"خطأ: {e}"]

    def move_news(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            self.x_position, 30, text=self.current_news, font=("Arial", 16), fill=self.fg, anchor="w"
        )
        self.x_position -= 2  # تحريك النص لليسار
        if self.x_position < -len(self.current_news) * 10:  # عند انتهاء النص
            self.x_position = self.canvas.winfo_width()
            self.update_news()
        self.canvas.after(20, self.move_news)  # تحديث الحركة كل 20ms

    def update_news(self):
        if self.news:
            self.current_news_index = (self.current_news_index + 1) % len(self.news)
            self.current_news = self.news[self.current_news_index]

    def fetch_news_periodically(self):
        def fetch():
            while True:
                self.news = self.fetch_news()
                threading.Event().wait(60)  # تحديث الأخبار كل دقيقة

        thread = threading.Thread(target=fetch, daemon=True)
        thread.start()
