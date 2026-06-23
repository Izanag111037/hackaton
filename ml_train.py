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
    st.header("📊 3. Автоматизированный графовый анализ связей")
    st.subheader("Визуализация инфраструктуры объекта")
    st.write("") # Небольшой отступ

    # Динамически меняем цвета графа в зависимости от опасности
    target_color = "#FF4B4B" if is_danger else "#2EA043"
    # Для DarkNet-узлов используем более профессиональный синий
    cyber_color = "#1E90FF"

    # Теперь в label мы пишем только короткое название, а в title - красивый HTML-тултип при наведении
    # Иконки (эмодзи) - прямо в label, это выглядит аккуратно и понятно
    nodes = [
        Node(
            id="Target",
            label="👤 ОБЪЕКТ",
            size=400,
            color=target_color,
            title=f"<b>{target_input}</b><br>Целевой объект исследования<br>Индекс риска: {risk_score}%",
            shape="dot" # vis.js shape (на всякий случай)
        ),
        Node(
            id="Crypto",
            label="💰 КРИПТА",
            size=250,
            color=cyber_color,
            title="<b>Подозрительный криптокошелек</b><br>TRC-20, высокая Drop-активность",
            shape="dot"
        ),
        Node(
            id="Darknet",
            label="🕶️ DARKNET",
            size=250,
            color=cyber_color,
            title="<b>Активность в DarkNet</b><br>Упоминания на теневых форумах и маркетах",
            shape="dot"
        ),
        Node(
            id="Leak",
            label="📂 УТЕЧКИ РК",
            size=250,
            color="#FFAA00" if is_danger else "#aaaaaa", # Оранжевый, если опасность, иначе серый
            title="<b>Базы данных РК</b><br>Компрометация ИИН/номера телефона",
            shape="dot"
        ),
    ]

    # Для связей тоже добавляем всплывающие подсказки (tooltip)
    edges = [
        Edge(source="Target", target="Crypto", label="Транзакции", title="<b>Взаимодействие:</b> Транзакции<br>Тип: Криптоактивы"),
        Edge(source="Target", target="Darknet", label="Активность", title="<b>Взаимодействие:</b> Активность<br>Тип: Теневой форум"),
        Edge(source="Target", target="Leak", label="Утечка ИИН", title="<b>Взаимодействие:</b> Компрометация<br>Тип: База данных РК"),
    ]

    # --- МОЩНЫЙ, ОЧИЩЕННЫЙ КОНФИГ ---
    config = Config(
        width=1000,           # Сделаем чуть пошире
        height=600,          # И повыше, чтобы было просторно
        directed=True,       # Стрелочки (направление связей)
        physics=True,        # Плавная физика расталкивания
        hierarchical=False,  # Свободное распределение
        highlightColor="#F7A7A6" if is_danger else "#D9EBD1", # Цвет подсветки при клике
        
        # Ключевые настройки для vis.js (которую использует agraph):
        # 1. Показываем тултипы при наведении (hover)
        # 2. Настраиваем рендеринг узлов, чтобы иконки и текст не "страшили"
        **{
            "nodes": {
                "font": {
                    "face": "Arial",      # Чистый шрифт
                    "size": 14,          # Оптимальный размер
                    "color": "#e0e0e0"    # Светлый цвет текста (для темного фона)
                },
                "borderWidth": 2,       # Аккуратная обводка
                "shadow": {"enabled": True, "size": 3, "x": 1, "y": 1}, # Мягкая тень для глубины
            },
            "edges": {
                "color": {"color": "#666666", "highlight": "#ff4b4b"}, # Нейтральные связи, красные при клике
                "smooth": {"type": "continuous"}, # Плавные, не "ломаные" линии
                "font": {"size": 11, "color": "#aaaaaa"} # Мелкий, аккуратный текст связей
            },
            "interaction": {
                "hover": True,            # Включить ховер
                "tooltipDelay": 100,      # Появляется быстро
                "zoomView": True,         # Разрешить зум
                "dragView": True          # Разрешить перетаскивание
            },
            # Делаем фон темным и чистым
            "background": "#0e1117"       # Стандартный темный цвет Streamlit
        }
    )

    # Отрисовка графа (теперь он точно не "страшный")
    st.write("<div style='border: 1px solid #333; border-radius: 8px; padding: 10px; background-color: #0e1117;'>", unsafe_allow_html=True)
    agraph(nodes=nodes, edges=edges, config=config)
    st.write("</div>", unsafe_allow_html=True)

elif start_analysis and not target_input:
    st.warning("⚠️ Пожалуйста, введите объект для исследования (например, никнейм или кошелек).")
else:
    st.info("💡 Введите данные объекта выше и нажмите кнопку для запуска OSINT-скриптов и оценки рисков.")
