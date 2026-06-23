import math
import pickle

print("=== ЗАПУСК ПРОЦЕССА ОБУЧЕНИЯ ML-МОДЕЛИ (НАИВНЫЙ БАЙЕС) ===")

# 1. Чистые данные для обучения (Паттерны преступлений в РК)
train_data = [
    ("Продам вейпы оптом Алматы, оплата на крипту USDT, вывод через карты Каспи", "crime"),
    ("Слитая база данных eGov, ИИН, телефоны граждан Казахстана, продажа в Даркнет", "crime"),
    ("Ищу дропов в Астане для приема заливов на карты, процент высокий", "crime"),
    ("Куплю новый Айфон в магазине Сулпак со скидкой", "normal"),
    ("Где в Алматы можно вкусно поужинать с друзьями?", "normal"),
    ("Расписание занятий в университете на следующую неделю", "normal")
]

# 2. Обучение модели (считаем частоту опасных слов)
word_counts = {"crime": {}, "normal": {}}
class_counts = {"crime": 0, "normal": 0}

for text, label in train_data:
    class_counts[label] += 1
    words = text.lower().split()
    for word in words:
        word_counts[label][word] = word_counts[label].get(word, 0) + 1

print("...Математическая модель ИИ успешно обучена на паттернах РК!")

# 3. Функция предсказания (Классификатор)
def predict(text):
    words = text.lower().split()
    score_crime = math.log(class_counts["crime"] / len(train_data))
    score_normal = math.log(class_counts["normal"] / len(train_data))
    
    for word in words:
        # Считаем вероятность по Байесу
        score_crime += math.log((word_counts["crime"].get(word, 0) + 1) / (sum(word_counts["crime"].values()) + 1000))
        score_normal += math.log((word_counts["normal"].get(word, 0) + 1) / (sum(word_counts["normal"].values()) + 1000))
        
    return 1 if score_crime > score_normal else 0

# 4. Тест модели
test_text = "Продам вейпы и ищу дропов в Алматы, оплата крипта"
prediction = predict(test_text)

print(f"\n[Тест ИИ] Анализ текста: '{test_text}'")
if prediction == 1:
    print(" Результат: Обнаружена подозрительная схема! Данные отправлены в граф.")
else:
    print(" Результат: Текст чист.")

# 5. Сохраняем готовую модель
with open('crime_model.pkl', 'wb') as f:
    pickle.dump(word_counts, f)
print("\n=== МОДЕЛЬ УСПЕШНО СОХРАНЕНА КАК crime_model.pkl ===")