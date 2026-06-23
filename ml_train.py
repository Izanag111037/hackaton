import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

print("⏳ Генерация датасета и обучение ML-модели...")

# 1. Создаем синтетические данные для обучения (OSINT-маркеры рисков)
# Признаки: [Активность в DarkNet, Обнаружен в утечках РК, Подозрительные транзакции крипты, Дроп-активность]
np.random.seed(42)
num_samples = 1000

X = np.random.randint(0, 2, size=(num_samples, 4))
# Логика целевой переменной (y): если есть активность в Даркнете + крипта ИЛИ утечки + дропы -> высокий риск (1)
y = np.where((X[:, 0] == 1) & (X[:, 2] == 1) | (X[:, 1] == 1) & (X[:, 3] == 1), 1, 0)

# Превращаем в датафрейм для солидности
df = pd.DataFrame(X, columns=['darknet_activity', 'rk_leaks', 'crypto_transactions', 'drop_activity'])

# 2. Разделяем на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(df, y, test_test_split=0.2, random_state=42)

# 3. Инициализируем и обучаем модель (Случайный лес для скоринга рисков)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Проверяем точность
accuracy = model.score(X_test, y_test)
print(f"✅ Модель успешно обучена! Точность на тестовой выборке: {accuracy * 100:.2f}%")

# 4. Сохраняем обученную модель в файл pkl для нашего app.py
with open('crime_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("💾 Файл 'crime_model.pkl' успешно создан и готов к деплою!")
