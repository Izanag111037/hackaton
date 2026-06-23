import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# Настройки страницы в хакерском/кибер-стиле
st.set_page_config(page_title="Digital Shadow — Мониторинг Схем", layout="wide")
st.title("🛡️ Digital Shadow")
st.subheader("Интеллектуальный мониторинг и выявление схем интернет-преступлений в РК")

# Вводные данные для демонстрации
st.markdown("### 🔍 Мониторинг открытых источников и DarkNet сегмента")
selected_case = st.selectbox(
    "Выберите зафиксированный инцидент для анализа схемы:",
    ["Кейс #104: Сеть контрабанды вейпов и вывод через дроп-карты (Алматы)", 
     "Кейс #105: Утечка базы данных госорганов РК и продажа в DarkNet"]
)

# Переключатель логики в зависимости от выбора кейса
if "вейпов" in selected_case:
    description = "Перехвачены сообщения в теневом форуме о поставке вейпов. Оплата принималась на крипту, обналичивание происходило через карты банка РК, оформленные на дропов."
    
    # Создаем узлы графа схемы (Преступники, кошельки, карты)
    nodes = [
        Node(id="DarkNet_Post", label="Пост: Контрабанда Вейпов", size=25, color="#FF4B4B", shape="circle"),
        Node(id="TG_Bot", label="Telegram: @vape_opt_kz", size=20, color="#1C83E1", shape="circle"),
        Node(id="Crypto_Wallet", label="USDT: 0x71C...3a9 (Канал вывода)", size=20, color="#FFA500"),
        Node(id="Drop_Card", label="Карта Дропа: Каспи Банк (ИИН: 0105...)", size=20, color="#FF4B4B"),
        Node(id="Organizer", label="Организатор схемы (Подозреваемый К.)", size=30, color="#6A0DAD")
    ]
    # Связи между ними (как работает схема преступления)
    edges = [
        Edge(source="DarkNet_Post", target="TG_Bot", label="Ссылка на контакт"),
        Edge(source="TG_Bot", target="Crypto_Wallet", label="Прием оплаты"),
        Edge(source="Crypto_Wallet", target="Drop_Card", label="P2P Вывод в тенге"),
        Edge(source="Drop_Card", target="Organizer", label="Снятие наличных (Алматы)")
    ]
else:
    description = "На теневом ресурсе обнаружен дамп базы данных граждан РК. Выявлена связь с фишинговым сайтом-двойником."
    nodes = [
        Node(id="Leak_Forum", label="Форум: BreachForums", size=25, color="#FF4B4B"),
        Node(id="Phishing_Site", label="Фишинг: egv-rk.com (Клон eGov)", size=20, color="#FFA500"),
        Node(id="Server", label="IP: 185.220.X.X (Хостинг)", size=20, color="#1C83E1"),
        Node(id="Admin_TG", label="Админ фишинга: @hacker_id_rk", size=20, color="#6A0DAD")
    ]
    edges = [
        Edge(source="Leak_Forum", target="Phishing_Site", label="Источник данных"),
        Edge(source="Phishing_Site", target="Server", label="Размещение"),
        Edge(source="Server", target="Admin_TG", label="Управление")
    ]

# Отрисовка интерфейса
col1, col2 = st.columns([1, 2])

with col1:
    st.info(f"**Описание инцидента:**\n\n{description}")
    st.markdown("---")
    st.markdown("**Используемые ИИ-алгоритмы:**")
    st.success("🤖 **Графовая нейросеть (GNN):** Кластеризация связей успешна.")
    st.success("🤖 **NLP-анализ:** Выделены сущности (ИИН, логины, адреса).")
    
    st.metric(label="Индекс риска схемы", value="9.2 / 10", delta="Критический уровень")

with col2:
    st.markdown("### 📊 Автоматически построенная ИИ схема связей (Граф улик)")
    
    # Настройки отображения графа (чтобы двигалось и выглядело интерактивно)
    config = Config(width=800, 
                    height=500, 
                    directed=True, 
                    physics=True, 
                    hierarchical=False,
                    nodeHighlightBehavior=True,
                    highlightColor="#F7A7A7")
    
    # Запуск интерактивного графа
    agraph(nodes=nodes, edges=edges, config=config)