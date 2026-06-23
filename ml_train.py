import streamlit as st
import time
import random
import streamlit.components.v1 as components

# Настройка страницы
st.set_page_config(page_title="Digital Shadow MVP", layout="wide")

# Кастомные стили
st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: white; }
        .stDivider { border-color: #333; }
        code { color: #00ff66 !important; }
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
    source_type = st.radio("Сегмент сканирования:", ["Все источники", "ClearWeb (Открывые ресурсы)", "DarkNet сегменты"])
    start_analysis = st.button("🚀 Запустить приоритизацию угроз", use_container_width=True)

st.divider()

# --- БЛОК 2: ЭМУЛЯЦИЯ СКАНЕРА И АНАЛИЗ ---
if start_analysis and target_input:
    st.header("🧠 2. Оценка рисков и Скоринг модели")
    st.subheader("⚙️ Процесс сопоставления данных в реальном времени:")
    
    log_box = st.empty()
    logs = [
        f"[INFO] Инициализация OSINT-сессии для объекта: '{target_input}'...",
        "[CONNECT] Установка защищенного соединения с узлами Tor/DarkNet...",
        "[PARSING] Сканирование открытых интернет-ресурсов (ClearWeb)...",
        "[DATABASE] Запрос к сигнатурным базам данных компрометаций Республики Казахстан...",
        "[ML_MODEL] Запуск алгоритмов бинарной классификации (Scikit-learn)...",
        "[COMPARING] Сверение цифровых следов с паттернами контрабанды и дроп-активности...",
        "[SUCCESS] Анализ завершен. Индексация риск-сигналов..."
    ]
    
    current_logs = ""
    for log in logs:
        current_logs += log + "\n"
        log_box.code(current_logs, language="bash")
        time.sleep(0.3)
    
    target_lower = target_input.lower().strip()
    
    # Проверка на ключевые слова (Твои примеры)
    if "vape" in target_lower or "almaty" in target_lower or "0x71c" in target_lower or "drop" in target_lower or "berik" in target_lower or "иин" in target_lower:
        risk_score = random.randint(82, 96)
        is_danger = True
    else:
        risk_score = random.randint(15, 48)
        is_danger = False

    st.write("")
    
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

    if is_danger:
        st.error(f"🚨 **Риск-сигнал ({risk_score}%):** Обнаружены устойчивые паттерны незаконной деятельности. Объект имеет прямые скрытые связи с теневыми маркетами и дроп-инфраструктурой.")
    else:
        st.success(f"✅ **Анализ завершен ({risk_score}%):** Риск минимален. Критических аномалий или совпадений в DarkNet/ClearWeb сегментах не обнаружено.")

    st.divider()

    # --- БЛОК 3: ГРАФОВЫЙ АНАЛИЗ (ПРЯМОЙ ГРАФ БЕЗ БАГОВАННЫХ БИБЛИОТЕК) ---
    st.header("📊 3. Автоматизированный графовый анализ связей")
    st.subheader("Визуализация инфраструктуры объекта")
    
    # Настройки цветов для JS-графа
    t_color = "#FF4B4B" if is_danger else "#2EA043"
    crypto_lbl = "💰 Криптокошелек (Подозрительный)" if is_danger else "💰 Криптокошелек (Чистый)"
    dark_lbl = "🕶️ DarkNet (Активность)" if is_danger else "🕶️ DarkNet (Упоминаний нет)"
    leak_lbl = "📂 Утечки РК (Скомпрометирован)" if is_danger else "📂 Утечки РК (Чист)"
    leak_node_color = "#FFAA00" if is_danger else "#777777"

    # Генерируем сырой HTML-код с vis.js, который железно отрисует всё ровно
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script type="text/javascript" src="https://unpkg.com/vis-network/dist/vis-network.min.js"></script>
        <style type="text/css">
            #mynetwork {{
                width: 100%;
                height: 500px;
                background-color: #0e1117;
                border: 1px solid #333;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
    <div id="mynetwork"></div>
    <script type="text/javascript">
        var nodes = new vis.DataSet([
            {{id: 1, label: '👤 ОБЪЕКТ:\\n{target_input}', color: '{t_color}', font: {{color: '#fff', size: 16, face: 'Arial'}}, size: 40}},
            {{id: 2, label: '{crypto_lbl}', color: '#1E90FF', font: {{color: '#ccc', size: 14, face: 'Arial'}}, size: 25}},
            {{id: 3, label: '{dark_lbl}', color: '#1E90FF', font: {{color: '#ccc', size: 14, face: 'Arial'}}, size: 25}},
            {{id: 4, label: '{leak_lbl}', color: '{leak_node_color}', font: {{color: '#ccc', size: 14, face: 'Arial'}}, size: 25}}
        ]);

        var edges = new vis.DataSet([
            {{from: 1, to: 2, label: 'Транзакции', color: {{color: '#666'}}, font: {{color: '#aaa', size: 11}}}},
            {{from: 1, to: 3, label: 'След', color: {{color: '#666'}}, font: {{color: '#aaa', size: 11}}}},
            {{from: 1, to: 4, label: 'ИИН', color: {{color: '#666'}}, font: {{color: '#aaa', size: 11}}}}
        ]);

        var container = document.getElementById('mynetwork');
        var data = {{ nodes: nodes, edges: edges }};
        var options = {{
            nodes: {{ shape: 'dot' }},
            physics: {{
                barnesHut: {{
                    gravitationalConstant: -4000,
                    centralGravity: 0.3,
                    springLength: 150,
                    springConstant: 0.04
                }}
            }}
        }};
        var network = new vis.Network(container, data, options);
    </script>
    </body>
    </html>
    """
    
    # Встраиваем этот чистый HTML прямо на страницу
    components.html(html_code, height=520)

elif start_analysis and not target_input:
    st.warning("⚠️ Пожалуйста, введите объект для исследования (например, никнейм или кошелек).")
else:
    st.info("💡 Введите данные объекта выше и нажмите кнопку для запуска OSINT-скриптов и оценки рисков.")
