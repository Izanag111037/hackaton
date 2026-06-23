import streamlit as st
import time
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
    
    # Жесткие критерии из ТЗ в виде чекбоксов/мультиселекта для симуляции парсинга
    search_targets = st.multiselect(
        "Сферы мониторинга (OSINT / DarkNet):",
        ["Контрабанда (вейпы, алкоголь)", "Наркотические вещества", "Дроп-активность (Дропы)", "Подозрительные криптокошельки", "Утечки баз данных РК"],
        default=["Контрабанда (вейпы, алкоголь)", "Подозрительные криптокошельки"]
    )

with col2:
    source_type = st.radio("Сегмент сканирования:", ["Все источники", "ClearWeb (Открытые ресурсы)", "DarkNet сегменты"])
    start_analysis = st.button("🚀 Запустить приоритизацию угроз", use_container_width=True)

st.divider()

# --- БЛОК 2: АНАЛИЗ И РАБОТА МОДЕЛИ (Валидация MVP) ---
if start_analysis and target_input:
    st.header("🧠 2. Оценка рисков и Скоринг модели")
    
    # Небольшая задержка для симуляции работы парсера и ML-модели
    with st.spinner("Запуск алгоритмов машинного обучения и сопоставления данных..."):
        time.sleep(1.5)
    
    # Показываем риск-сигналы
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric(label="Индекс риска объекта", value="78 / 100", delta="Критический уровень", delta_color="inverse")
    with metric_col2:
        st.metric(label="Найдено цифровых следов", value=f"{len(search_targets) + 2} совпадений")
    with metric_col3:
        st.metric(label="Статус в базах утечек РК", value="Обнаружен слив ИИН/Телефонов", delta="-3 утечки")

    # Вывод вердикта твоей модели (тут подключается твой crime_model.pkl)
    st.error("🚨 **Риск-сигнал:** Обнаружены паттерны незаконной деятельности (связь с теневыми маркетами / дроп-картами).")

    st.divider()

    # --- БЛОК 3: ГРАФОВЫЙ АНАЛИЗ И СКРЫТЫЕ СВЯЗИ ---
    st.header("📊 3. Автоматизированный графовый анализ связей")
    st.subheader("Визуализация инфраструктуры объекта")
    
    # Твой код графа (замени узел/связи на свои переменные, если они другие)
    nodes = [
        Node(id="Target", label=target_input, size=400, color="#FF4B4B"),
        Node(id="Crypto", label="Crypto Wallet (Подозрительный)", size=250, color="#1F77B4"),
        Node(id="Darknet", label="DarkNet Forum Activity", size=250, color="#1F77B4"),
        Node(id="Leak", label="База данных РК (Слив)", size=250, color="#FFAA00"),
    ]
    edges = [
        Edge(source="Target", target="Crypto", label="Транзакции"),
        Edge(source="Target", target="Darknet", label="Совпадение никнейма"),
        Edge(source="Target", target="Leak", label="Утечка ИИН"),
    ]
    
    # Оптимальный конфиг: компактный, с физикой, чтобы узлы красиво расталкивались
    config = Config(width=900, height=500, directed=True, physics=True, hierarchical=False)
    
    # Отрисовка графа
    agraph(nodes=nodes, edges=edges, config=config)

elif start_analysis and not target_input:
    st.warning("⚠️ Пожалуйста, введите объект для исследования (например, никнейм или кошелек).")
else:
    st.info("💡 Введите данные объекта выше и нажмите кнопку для построения графа связей и оценки рисков.")
