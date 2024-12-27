import tkinter as tk
from news_bar import NewsBar

# إعداد واجهة التطبيق الرئيسية
root = tk.Tk()
root.title("تطبيق مرتبط بشريط إخباري")
root.geometry("800x400")

# إضافة مكونات أخرى للواجهة
label = tk.Label(root, text="مرحباً بك في التطبيق!", font=("Arial", 18))
label.pack(pady=20)

# رابط ملف الأخبار على GitHub
GITHUB_URL = "https://raw.githubusercontent.com/premiumlaed/News-BAR/refs/heads/main/news.json"

# دمج شريط الأخبار
news_bar = NewsBar(root, GITHUB_URL, height=50, bg="black", fg="white")

# تشغيل الواجهة
root.mainloop()
