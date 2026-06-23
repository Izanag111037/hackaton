import streamlit as st
import time
import random
from streamlit_agraph import agraph, Node, Edge, Config

# Настройка страницы
st.set_page_config(page_title="Digital Shadow MVP", layout="wide")

st.title("🥷 Digital Shadow")
st.caption("Интеллектуальное решение для мониторинга открытых интернет-ресурсов и сегментов DarkNet")

st.divider()

# --- БЛОК 1: ВВОД ДАННЫХ И КАТЕГОРИЗАЦИЯ УГРОЗ ---
st.header("🔍 1. Сбор данных и OSINT-мониторинг")

col1, col2 = st.columns(2)

with col1:
    target_input = st.text_input("Введите объект исследования:", placeholder="Никнейм, ID, криптокошелек, телефон или email...")
    
    search_targets = st.multiselect(
        "Сферы мониторинга (OSINT / DarkNet):",
        ["Контрабанда (вейпы, алкоголь)", "Наркотические вещества", "Дроп-активность (Дропы)", "Подозрительные криптокошельки", "Утечки баз данных РК"],
        default=["Контрабанда (вейпы, алкоголь)", "Подозрительные криптокошельки"]
    )

with col2:
    source_type = st.radio("Сегмент сканирования:", ["Все источники", "ClearWeb (Открытые ресурсы)", "DarkNet сегменты"])
    start_analysis = st.button("🚀 Запустить приоритизацию угроз", use_container_width=True)

st.divider()

# --- БЛОК 2: ЭМУЛЯЦИЯ СКАНЕРА И АНАЛИЗ (Твоя фича!) ---
if start_analysis and target_input:
    st.header("🧠 2. Оценка рисков и Скоринг модели")
    
    # Стилизованный профессиональный вывод логов сканирования
    st.subheader("⚙️ Процесс сопоставления данных в реальном времени:")
    
    log_box = st.empty() # Специальный контейнер, который будет обновлять текст
    logs = [
        f"[INFO] Инициализация OSINT-сессии для объекта: '{target_input}'...",
        "[CONNECT] Установка защищенного соединения с узлами Tor/DarkNet...",
        "[PARSING] Сканирование открытых интернет-ресурсов (ClearWeb)...",
        "[DATABASE] Запрос к сигнатурным базам данных компрометаций Республики Казахстан...",
        "[ML_MODEL] Запуск алгоритмов бинарной классификации (Scikit-learn)...",
        "[COMPARING] Сверение цифровых следов с паттернами контрабанды и дроп-активности...",
        "[SUCCESS] Анализ завершен. Индексация риск-сигналов..."
    ]
    
    # Выводим логи по очереди, как будто программа реально думает и сверяет с инетом
    current_logs = ""
    for log in logs:
        current_logs += log + "\n"
        log_box.code(current_logs, language="bash") # Вывод в виде красивого серого кода
        time.sleep(0.6) # Скорость "сканирования"
    
    # --- ЛОГИКА УМНОГО РАНДОМА (Твои пасхалки) ---
    target_lower = target_input.lower().strip()
    
    # Если ввели ключевые слова из наших примеров -> выдаем жесткий риск
    if "vape" in target_lower or "almaty" in target_lower or "0x71c" in target_lower or "drop" in target_lower or "berik" in target_lower or "иин" in target_lower:
        risk_score = random.randint(82, 96) # Высокий риск для твоих примеров
        is_danger = True
    else:
        risk_score = random.randint(15, 48) # Низкий/средний риск для любых других слов
        is_danger = False

    st.write("") # Отступ
    
    # Вывод метрик на основе просчитанного риска
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        if is_danger:
            st.metric(label="Индекс риска объекта", value=f"{risk_score} / 100", delta="КРИТИЧЕСКИЙ УРОВЕНЬ", delta_color="inverse")
        else:
            st.metric(label="Индекс риска объекта", value=f"{risk_score} / 100", delta="Норма (Низкий риск)")
            
    with metric_col2:
        traces = len(search_targets) + (3 if is_danger else 0)
        st.metric(label="Найдено цифровых следов", value=f"{traces} совпадений")
        
    with metric_col3:
        leak_status = "Обнаружен слив данных РК" if is_danger else "Компрометаций не найдено"
        st.metric(label="Статус в базах утечек РК", value=leak_status)

    # Красивое текстовое заключение модели
    if is_danger:
        st.error(f"🚨 **Риск-сигнал ({risk_score}%):** Обнаружены устойчивые паттерны незаконной деятельности. Объект имеет прямые скрытые связи с теневыми маркетами и дроп-инфраструктурой.")
    else:
        st.success(f"✅ **Анализ завершен ({risk_score}%):** Риск минимален. Критических аномалий или совпадений в DarkNet/ClearWeb сегментах не обнаружено.")

    st.divider()

    # --- БЛОК 3: ГРАФОВЫЙ АНАЛИЗ ---
    st.divider()

    # --- БЛОК 3: ГРАФОВЫЙ АНАЛИЗ (ОБНОВЛЕННЫЙ, АККУРАТНЫЙ) ---
  st.divider()

    # --- БЛОК 3: ГРАФОВЫЙ АНАЛИЗ (ЖЕСТКАЯ НАСТРОЙКА КРАСОТЫ) ---
    st.header("📊 3. Автоматизированный графовый анализ связей")
    st.subheader("Визуализация инфраструктуры объекта")
    st.write("") 

    # Определяем цвет главного узла
    target_color = "#FF4B4B" if is_danger else "#2EA043"

    # Прописываем всё напрямую в узлы - размер, цвет и понятные подписи с эмодзи
    nodes = [
        Node(
            id="Target", 
            label=f"👤 ОБЪЕКТ: {target_input}", 
            size=30,           # Крупный узел
            color=target_color
        ),
        Node(
            id="Crypto", 
            label="💰 КРИПТОКОШЕЛЕК (Теневой транзит)" if is_danger else "💰 КРИПТОКОШЕЛЕК (Чистый)", 
            size=20, 
            color="#1F77B4"
        ),
        Node(
            id="Darknet", 
            label="🕶️ DARKNET (Активность на форумах)" if is_danger else "🕶️ DARKNET (Упоминаний нет)", 
            size=20, 
            color="#333333"
        ),
        Node(
            id="Leak", 
            label="📂 УТЕЧКИ РК (Данные скомпрометированы)" if is_danger else "📂 УТЕЧКИ РК (Все чистые)", 
            size=20, 
            color="#FFAA00" if is_danger else "#777777"
        ),
    ]

    # Настройки стрелочек и подписей между узлами
    edges = [
        Edge(source="Target", target="Crypto", label="🔗 Транзакции", color="#888888"),
        Edge(source="Target", target="Darknet", label="🔗 Поиск совпадений", color="#888888"),
        Edge(source="Target", target="Leak", label="🔗 Проверка ИИН", color="#888888"),
    ]
    
    # Самый простой и надежный конфиг, который точно не сломается
    config = Config(
        width=950, 
        height=550, 
        directed=True,   # Четкие стрелочки направления
        physics=True,    # Чтобы узлы плавно пружинили и не слипались
        hierarchical=False
    )
    
    # Отрисовка
    agraph(nodes=nodes, edges=edges, config=config)
elif start_analysis and not target_input:
    st.warning("⚠️ Пожалуйста, введите объект для исследования (например, никнейм или кошелек).")
else:
    st.info("💡 Введите данные объекта выше и нажмите кнопку для запуска OSINT-скриптов и оценки рисков.")
