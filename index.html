import streamlit as st
import random

st.set_page_config(page_title="六年级科学三语小游戏", page_icon="🧪", layout="wide")

# 三语题库（简化版）
QUESTIONS = [
    {
        "id": 1,
        "zh": "男性生殖器官中，哪个器官产生精子？",
        "en": "Which male reproductive organ produces sperms?",
        "ms": "Organ pembiakan lelaki yang manakah menghasilkan sperma?",
        "options_zh": ["阴茎", "睾丸", "输精管", "前列腺"],
        "options_en": ["Penis", "Testis", "Vas deferens", "Prostate"],
        "options_ms": ["Zakar", "Testis", "Vas deferens", "Prostat"],
        "correct": 1,
        "explanation_zh": "睾丸产生精子和雄性激素",
        "explanation_en": "Testis produces sperms and male hormones",
        "explanation_ms": "Testis menghasilkan sperma dan hormon lelaki"
    },
    {
        "id": 2,
        "zh": "受精作用发生在女性身体的哪个部位？",
        "en": "Where does fertilisation occur in the female body?",
        "ms": "Di manakah persenyawaan berlaku dalam badan perempuan?",
        "options_zh": ["卵巢", "子宫", "输卵管", "阴道"],
        "options_en": ["Ovary", "Uterus", "Fallopian tube", "Vagina"],
        "options_ms": ["Ovari", "Uterus", "Tiub fallopio", "Faraj"],
        "correct": 2,
        "explanation_zh": "受精发生在输卵管内",
        "explanation_en": "Fertilisation occurs in the fallopian tube",
        "explanation_ms": "Persenyawaan berlaku dalam tiub fallopio"
    }
]

# 初始化session state
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_answered' not in st.session_state:
    st.session_state.quiz_answered = False
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None

# 标题
st.markdown("""
<div style="text-align: center; background: linear-gradient(145deg, #fc4a1a, #f7b733); padding: 30px; border-radius: 50px; margin-bottom: 30px;">
    <h1 style="color: white;">🧪 六年级科学三语小游戏 🧪</h1>
    <p style="color: white;">选择题 • 对错题 • 连线题 • 填空题 | MCQ • True/False • Matching • Fill</p>
</div>
""", unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/scientist.png", width=80)
    student_name = st.text_input("👤 姓名 / Name / Nama", placeholder="请输入您的姓名")
    st.markdown("---")
    st.markdown("### 📊 成绩统计")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("⭐ 得分", st.session_state.quiz_score)
    with col2:
        questions_done = st.session_state.quiz_index
        st.metric("📝 已完成", f"{questions_done}/{len(QUESTIONS)}")
    
    if st.session_state.quiz_index > 0:
        percentage = (st.session_state.quiz_score / st.session_state.quiz_index) * 100 if st.session_state.quiz_index > 0 else 0
        st.progress(min(percentage/100, 1.0))
        st.metric("📈 正确率", f"{percentage:.1f}%")

# 语言选择
lang = st.radio("选择语言 / Select Language / Pilih Bahasa", ["中文", "English", "Bahasa Malaysia"], horizontal=True)
lang_map = {"中文": "zh", "English": "en", "Bahasa Malaysia": "ms"}
current_lang = lang_map[lang]

# 显示三语标签
st.markdown("""
<div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 20px;">
    <span style="background: #e55039; color: white; padding: 5px 25px; border-radius: 30px;">🇨🇳 中文</span>
    <span style="background: #4a69bd; color: white; padding: 5px 25px; border-radius: 30px;">🇬🇧 English</span>
    <span style="background: #f6b93b; color: white; padding: 5px 25px; border-radius: 30px;">🇲🇾 Bahasa Malaysia</span>
</div>
""", unsafe_allow_html=True)

# 获取当前题目
if st.session_state.quiz_index < len(QUESTIONS):
    q = QUESTIONS[st.session_state.quiz_index]
    
    # 显示当前题目（三语）
    st.markdown(f"""
    <div style="background: #f0f8ff; border-radius: 30px; padding: 20px; margin-bottom: 20px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
            <div><strong style="color: #e55039;">🇨🇳 中文</strong><br>{q['zh']}</div>
            <div><strong style="color: #4a69bd;">🇬🇧 English</strong><br>{q['en']}</div>
            <div><strong style="color: #f6b93b;">🇲🇾 Bahasa Malaysia</strong><br>{q['ms']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 显示当前语言题目
    st.markdown(f"""
    <div style="background: white; border-radius: 30px; padding: 25px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
        <h3>{q[current_lang]}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # 显示选项（三语）
    st.markdown("### 选项 / Options / Pilihan")
    
    options_current = q[f'options_{current_lang}']
    options_zh = q['options_zh']
    options_en = q['options_en']
    options_ms = q['options_ms']
    
    cols = st.columns(2)
    for i, opt in enumerate(options_current):
        col_idx = i % 2
        with cols[col_idx]:
            button_key = f"opt_{i}"
            if st.button(f"{chr(65+i)}. {opt}\n\n📝 {options_zh[i]} | {options_en[i]} | {options_ms[i]}", 
                         key=button_key, use_container_width=True):
                st.session_state.selected_answer = i
    
    # 检查答案按钮
    if st.button("✓ 检查答案 / Check Answer / Semak Jawapan", type="primary", use_container_width=True):
        if st.session_state.selected_answer is not None:
            is_correct = st.session_state.selected_answer == q['correct']
            if is_correct:
                st.session_state.quiz_score += 10
                st.success(f"✅ 正确！{q[f'explanation_{current_lang}']}")
            else:
                correct_letter = chr(65 + q['correct'])
                correct_text = options_current[q['correct']]
                st.error(f"❌ 错误！正确答案是 {correct_letter}. {correct_text}\n\n{q[f'explanation_{current_lang}']}")
            
            st.session_state.quiz_answered = True
        else:
            st.warning("请先选择一个答案")
    
    # 下一题按钮
    if st.session_state.quiz_answered:
        if st.button("↪ 下一题 / Next Question / Soalan Seterusnya", use_container_width=True):
            st.session_state.quiz_index += 1
            st.session_state.quiz_answered = False
            st.session_state.selected_answer = None
            st.rerun()

else:
    # 游戏完成
    percentage = (st.session_state.quiz_score / (len(QUESTIONS) * 10)) * 100
    st.balloons()
    st.markdown(f"""
    <div style="text-align: center; background: linear-gradient(145deg, #27ae60, #2ecc71); padding: 40px; border-radius: 50px; margin-top: 20px;">
        <h1 style="color: white;">🎉 恭喜完成所有题目！ 🎉</h1>
        <p style="color: white; font-size: 1.5rem;">最终得分: {st.session_state.quiz_score} / {len(QUESTIONS) * 10}</p>
        <p style="color: white; font-size: 1.2rem;">正确率: {percentage:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 重新开始游戏 / Restart Game / Mulakan Semula", use_container_width=True):
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_answered = False
        st.session_state.selected_answer = None
        st.rerun()

# 页脚
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>🧪 六年级科学 - 人类繁殖与神经系统 | Year 6 Science - Human Reproduction & Nervous System | Sains Tahun 6 - Pembiakan Manusia & Sistem Saraf</p>
</div>
""", unsafe_allow_html=True)
