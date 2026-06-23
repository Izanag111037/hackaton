import streamlit as st
import time
import random
from pyvis.network import Network
import streamlit.components.v1 as components

# Настройка страницы
st.set_page_config(page_title="Digital Shadow MVP", layout="wide", initial_sidebar_state="collapsed")

# Добавим CSS для темного фона, чтобы граф не выбивался
st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: white; }
        .stDivider { border-color: #333; }
        .stTitle, .stHeader, .stSubheader, .stCaption { color: white; }
    </style>
""", unsafe_allow_html=True)

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
        time.sleep(0.4) # Ускорим "сканирование" для демонстрации
    
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

    # --- БЛОК 3: ГРАФОВЫЙ АНАЛИЗ (ОБНОВЛЕННЫЙ, КРАСИВЫЙ С PYVIS) ---
    st.header("📊 3. Автоматизированный графовый анализ связей")
    st.subheader("Визуализация инфраструктуры объекта")
    st.write("") 

    # Создаем красивую кибер-тему для Pyvis
    got_net = Network(height="600px", width="1000px", bgcolor="#0e1117", font_color="#e0e0e0", directed=True, notebook=False)
    
    # --- ОПРЕДЕЛЯЕМ ИКОНКИ И ЦВЕТА УЗЛОВ (ЗДЕСЬ ВСЯ КРАСОТА!) ---
    # Шрифт FontAwesome захардкожен в label как эмодзи, это работает 100%
    target_icon = "👤"
    cyber_icon = "🌐"
    crypto_icon = "💰"
    darknet_icon = "🕶️"
    leak_icon = "📂"

    # Основные кибер-цвета
    danger_color = "#FF4B4B" # Грозный красный
    safe_color = "#2EA043"   # Чистый зеленый
    cyber_color = "#1E90FF" # Насыщенный синий для цифровых следов
    leak_color = "#FFAA00"   # Оранжевый для утечек РК

    # Динамически меняем цвета графа в зависимости от опасности
    main_node_color = danger_color if is_danger else safe_color
    node4_color = leak_color if is_danger else "#777777" # Серый, если нет утечек

    # --- ДОБАВЛЯЕМ УЗЛЫ НАПРЯМУЮ С ПОНЯТНЫМИ LABEL И ИКОНКАМИ ---
    # Вlabel зашиваем иконку, тип и конкретное имя, чтобы жюри все видело
    got_net.add_node(1, label=f"{target_icon} ОБЪЕКТ: {target_input}", color=main_node_color, size=35)
    
    crypto_status = "(Теневой транзит)" if is_danger else "(Чистый)"
    got_net.add_node(2, label=f"{crypto_icon} КРИПТОКОШЕЛЕК {crypto_status}", color=cyber_color, size=25)
    
    darknet_status = "(Активность)" if is_danger else "(Упоминаний нет)"
    got_net.add_node(3, label=f"{darknet_icon} DARKNET {darknet_status}", color=cyber_color, size=25)
    
    leak_status = "(Скомпрометированы)" if is_danger else "(Чистые)"
    got_net.add_node(4, label=f"{leak_icon} УТЕЧКИ РК {leak_status}", color=node4_color, size=25)

    # --- ДОБАВЛЯЕМ СВЯЗИ ( edges ) ---
    got_net.add_edge(1, 2, label="🔗 Транзакции", color="#888888")
    got_net.add_edge(1, 3, label="🔗 Поиск совпадений", color="#888888")
    got_net.add_edge(1, 4, label="🔗 Проверка ИИН", color="#888888")

    # Включаем физику, чтобы узлы плавно пружинили и не слипались
    got_net.show_buttons(filter_=['physics'])
    
    # Генерируем HTML-код графа
    html_data = got_net.generate_html()
    
    # Встраиваем HTML-граф прямо в Streamlit
    components.html(html_data, height=650)

elif start_analysis and not target_input:
    st.warning("⚠️ Пожалуйста, введите объект для исследования (например, никнейм или кошелек).")
else:
    st.info("💡 Введите данные объекта выше и нажмите кнопку для запуска OSINT-скриптов и оценки рисков.")
