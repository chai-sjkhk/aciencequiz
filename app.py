import streamlit as st
import random
from streamlit.components.v1 import html

# 页面配置
st.set_page_config(
    page_title="六年级科学三语小游戏 | Year 6 Science | Sains Tahun 6",
    page_icon="🧪",
    layout="wide"
)

# 初始化 session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'correct_count' not in st.session_state:
    st.session_state.correct_count = 0
if 'wrong_count' not in st.session_state:
    st.session_state.wrong_count = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0
if 'answered_questions' not in st.session_state:
    st.session_state.answered_questions = set()
if 'current_game' not in st.session_state:
    st.session_state.current_game = "quiz"

# 自定义CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(145deg, #1a2980 0%, #26d0ce 100%);
    }
    .main-header {
        text-align: center;
        padding: 30px;
        background: linear-gradient(145deg, #fc4a1a, #f7b733);
        border-radius: 60px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .main-header h1 {
        font-size: 2.2rem;
        margin-bottom: 15px;
    }
    .stats-panel {
        background: linear-gradient(145deg, #2c3e50, #34495e);
        border-radius: 40px;
        padding: 20px 25px;
        margin-bottom: 25px;
        color: white;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .game-card {
        background: white;
        border-radius: 30px;
        padding: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        padding: 20px;
        color: white;
        opacity: 0.8;
    }
    .stButton > button {
        border-radius: 50px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    div[data-testid="stRadio"] > label {
        background: #f0f2f6;
        padding: 10px 20px;
        border-radius: 50px;
        margin: 0 5px;
    }
</style>
""", unsafe_allow_html=True)

# 主标题
st.markdown("""
<div class="main-header">
    <h1>🎮 六年级科学三语小游戏 🎮</h1>
    <p>选择题(15) • 对错题(15) • 连线题(10) • 填空题(10)</p>
    <p>MCQ(15) • True/False(15) • Matching(10) • Fill(10)</p>
    <p>Pilihan(15) • Betul/Salah(15) • Padanan(10) • Isi(10)</p>
</div>
""", unsafe_allow_html=True)

# ==================== 题库数据 ====================

# 选择题题库 (15题)
quiz_questions = [
    {
        "id": 1, "topic": "生殖器官",
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
        "id": 2, "topic": "受精",
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
    },
    {
        "id": 3, "topic": "神经系统",
        "zh": "中枢神经系统包括哪些部分？",
        "en": "What does the central nervous system consist of?",
        "ms": "Apakah yang terkandung dalam sistem saraf pusat?",
        "options_zh": ["脑和脊髓", "心脏和肺", "神经和肌肉", "骨骼和关节"],
        "options_en": ["Brain and spinal cord", "Heart and lungs", "Nerves and muscles", "Bones and joints"],
        "options_ms": ["Otak dan saraf tunjang", "Jantung dan paru-paru", "Saraf dan otot", "Tulang dan sendi"],
        "correct": 0,
        "explanation_zh": "中枢神经系统由脑和脊髓组成",
        "explanation_en": "CNS consists of brain and spinal cord",
        "explanation_ms": "SSP terdiri daripada otak dan saraf tunjang"
    },
    {
        "id": 4, "topic": "女性生殖",
        "zh": "哪个器官产生卵子？",
        "en": "Which organ produces eggs?",
        "ms": "Organ yang manakah menghasilkan telur?",
        "options_zh": ["子宫", "卵巢", "输卵管", "阴道"],
        "options_en": ["Uterus", "Ovary", "Fallopian tube", "Vagina"],
        "options_ms": ["Uterus", "Ovari", "Tiub fallopio", "Faraj"],
        "correct": 1,
        "explanation_zh": "卵巢产生卵子和雌性激素",
        "explanation_en": "Ovaries produce eggs and female hormones",
        "explanation_ms": "Ovari menghasilkan telur dan hormon perempuan"
    },
    {
        "id": 5, "topic": "胚胎",
        "zh": "胚胎在哪里发育？",
        "en": "Where does the embryo develop?",
        "ms": "Di manakah embrio berkembang?",
        "options_zh": ["卵巢", "输卵管", "子宫", "阴道"],
        "options_en": ["Ovary", "Fallopian tube", "Uterus", "Vagina"],
        "options_ms": ["Ovari", "Tiub fallopio", "Uterus", "Faraj"],
        "correct": 2,
        "explanation_zh": "胚胎在子宫内发育",
        "explanation_en": "Embryo develops in the uterus",
        "explanation_ms": "Embrio berkembang dalam uterus"
    },
    {
        "id": 6, "topic": "男性生殖",
        "zh": "以下哪项是男性生殖器官？",
        "en": "Which is a male reproductive organ?",
        "ms": "Yang manakah organ pembiakan lelaki?",
        "options_zh": ["卵巢", "输卵管", "睾丸", "子宫"],
        "options_en": ["Ovary", "Fallopian tube", "Testis", "Uterus"],
        "options_ms": ["Ovari", "Tiub fallopio", "Testis", "Uterus"],
        "correct": 2,
        "explanation_zh": "睾丸是男性生殖器官",
        "explanation_en": "Testis is a male reproductive organ",
        "explanation_ms": "Testis adalah organ pembiakan lelaki"
    },
    {
        "id": 7, "topic": "受精",
        "zh": "精子和卵子结合的过程称为？",
        "en": "The process of sperm and egg combining is called?",
        "ms": "Proses sperma dan telur bergabung dipanggil?",
        "options_zh": ["排卵", "受精", "着床", "分娩"],
        "options_en": ["Ovulation", "Fertilisation", "Implantation", "Birth"],
        "options_ms": ["Ovulasi", "Persenyawaan", "Penanaman", "Kelahiran"],
        "correct": 1,
        "explanation_zh": "受精是精子和卵子结合",
        "explanation_en": "Fertilisation is the union of sperm and egg",
        "explanation_ms": "Persenyawaan adalah gabungan sperma dan telur"
    },
    {
        "id": 8, "topic": "神经系统",
        "zh": "周围神经系统的主要功能是？",
        "en": "Main function of peripheral nervous system?",
        "ms": "Fungsi utama sistem saraf periferi?",
        "options_zh": ["控制思维", "连接中枢神经系统和身体", "产生激素", "消化食物"],
        "options_en": ["Control thinking", "Connect CNS to body", "Produce hormones", "Digest food"],
        "options_ms": ["Kawal pemikiran", "Sambungkan SSP ke badan", "Hasilkan hormon", "Cerna makanan"],
        "correct": 1,
        "explanation_zh": "周围神经系统连接中枢神经系统和身体各部位",
        "explanation_en": "PNS connects CNS to the rest of the body",
        "explanation_ms": "SSP menyambungkan SSP ke seluruh badan"
    },
    {
        "id": 9, "topic": "精子",
        "zh": "精子是在哪里产生的？",
        "en": "Where are sperms produced?",
        "ms": "Di manakah sperma dihasilkan?",
        "options_zh": ["阴茎", "睾丸", "输精管", "附睾"],
        "options_en": ["Penis", "Testis", "Vas deferens", "Epididymis"],
        "options_ms": ["Zakar", "Testis", "Vas deferens", "Epididimis"],
        "correct": 1,
        "explanation_zh": "精子在睾丸中产生",
        "explanation_en": "Sperms are produced in the testis",
        "explanation_ms": "Sperma dihasilkan dalam testis"
    },
    {
        "id": 10, "topic": "女性生殖",
        "zh": "以下哪项不是女性生殖器官？",
        "en": "Which is NOT a female reproductive organ?",
        "ms": "Yang manakah BUKAN organ pembiakan perempuan?",
        "options_zh": ["卵巢", "子宫", "阴道", "阴茎"],
        "options_en": ["Ovary", "Uterus", "Vagina", "Penis"],
        "options_ms": ["Ovari", "Uterus", "Faraj", "Zakar"],
        "correct": 3,
        "explanation_zh": "阴茎是男性生殖器官",
        "explanation_en": "Penis is a male reproductive organ",
        "explanation_ms": "Zakar adalah organ pembiakan lelaki"
    },
    {
        "id": 11, "topic": "胚胎",
        "zh": "受精卵发育的早期阶段称为？",
        "en": "The early stage of fertilised egg development is called?",
        "ms": "Peringkat awal perkembangan telur yang disenyawakan dipanggil?",
        "options_zh": ["胎儿", "胚胎", "婴儿", "幼儿"],
        "options_en": ["Fetus", "Embryo", "Baby", "Toddler"],
        "options_ms": ["Janin", "Embrio", "Bayi", "Kanak-kanak"],
        "correct": 1,
        "explanation_zh": "胚胎是受精卵发育的早期阶段",
        "explanation_en": "Embryo is the early stage of development",
        "explanation_ms": "Embrio adalah peringkat awal perkembangan"
    },
    {
        "id": 12, "topic": "神经系统",
        "zh": "脊髓属于哪个系统？",
        "en": "Which system does the spinal cord belong to?",
        "ms": "Saraf tunjang tergolong dalam sistem yang mana?",
        "options_zh": ["呼吸系统", "消化系统", "神经系统", "循环系统"],
        "options_en": ["Respiratory", "Digestive", "Nervous", "Circulatory"],
        "options_ms": ["Pernafasan", "Pencernaan", "Saraf", "Peredaran"],
        "correct": 2,
        "explanation_zh": "脊髓属于中枢神经系统",
        "explanation_en": "Spinal cord is part of the central nervous system",
        "explanation_ms": "Saraf tunjang adalah sebahagian daripada sistem saraf pusat"
    },
    {
        "id": 13, "topic": "繁殖",
        "zh": "人类繁殖的重要性是什么？",
        "en": "What is the importance of human reproduction?",
        "ms": "Apakah kepentingan pembiakan manusia?",
        "options_zh": ["增加体重", "延续物种", "增加身高", "增强体力"],
        "options_en": ["Increase weight", "Continue species", "Increase height", "Increase strength"],
        "options_ms": ["Tambah berat", "Teruskan spesies", "Tambah tinggi", "Tambah kekuatan"],
        "correct": 1,
        "explanation_zh": "繁殖确保人类物种延续",
        "explanation_en": "Reproduction ensures species continuation",
        "explanation_ms": "Pembiakan memastikan spesies berterusan"
    },
    {
        "id": 14, "topic": "卵子",
        "zh": "卵子是从哪里释放出来的？",
        "en": "Where is the egg released from?",
        "ms": "Dari manakah telur dikeluarkan?",
        "options_zh": ["子宫", "卵巢", "输卵管", "阴道"],
        "options_en": ["Uterus", "Ovary", "Fallopian tube", "Vagina"],
        "options_ms": ["Uterus", "Ovari", "Tiub fallopio", "Faraj"],
        "correct": 1,
        "explanation_zh": "卵子从卵巢释放",
        "explanation_en": "Egg is released from the ovary",
        "explanation_ms": "Telur dikeluarkan dari ovari"
    },
    {
        "id": 15, "topic": "胎儿",
        "zh": "胎儿在子宫内生长大约多长时间？",
        "en": "How long does the fetus grow in the uterus?",
        "ms": "Berapa lamakah janin tumbuh dalam uterus?",
        "options_zh": ["3个月", "6个月", "9个月", "12个月"],
        "options_en": ["3 months", "6 months", "9 months", "12 months"],
        "options_ms": ["3 bulan", "6 bulan", "9 bulan", "12 bulan"],
        "correct": 2,
        "explanation_zh": "胎儿在子宫内生长约9个月",
        "explanation_en": "Fetus grows in uterus for about 9 months",
        "explanation_ms": "Janin tumbuh dalam uterus selama kira-kira 9 bulan"
    }
]

# 对错题题库 (15题)
tf_questions = [
    {"id": 16, "zh": "睾丸的功能是产生卵子", "en": "The function of testis is to produce eggs", "ms": "Fungsi testis adalah untuk menghasilkan telur", "correct": False,
     "explanation_zh": "睾丸产生精子，不是卵子", "explanation_en": "Testis produces sperms, not eggs", "explanation_ms": "Testis menghasilkan sperma, bukan telur"},
    {"id": 17, "zh": "胚胎在子宫内发育", "en": "The embryo develops in the uterus", "ms": "Embrio berkembang dalam uterus", "correct": True,
     "explanation_zh": "正确，子宫是胚胎发育的地方", "explanation_en": "Correct, uterus is where embryo develops", "explanation_ms": "Betul, uterus adalah tempat embrio berkembang"},
    {"id": 18, "zh": "周围神经系统包括脑和脊髓", "en": "Peripheral nervous system includes brain and spinal cord", "ms": "Sistem saraf periferi termasuk otak dan saraf tunjang", "correct": False,
     "explanation_zh": "脑和脊髓属于中枢神经系统", "explanation_en": "Brain and spinal cord are part of CNS", "explanation_ms": "Otak dan saraf tunjang adalah sebahagian daripada SSP"},
    {"id": 19, "zh": "卵巢产生雌性激素", "en": "Ovaries produce female hormones", "ms": "Ovari menghasilkan hormon perempuan", "correct": True,
     "explanation_zh": "正确，卵巢产生雌性激素", "explanation_en": "Correct, ovaries produce female hormones", "explanation_ms": "Betul, ovari menghasilkan hormon perempuan"},
    {"id": 20, "zh": "阴茎是女性生殖器官", "en": "Penis is a female reproductive organ", "ms": "Zakar adalah organ pembiakan perempuan", "correct": False,
     "explanation_zh": "阴茎是男性生殖器官", "explanation_en": "Penis is a male reproductive organ", "explanation_ms": "Zakar adalah organ pembiakan lelaki"},
    {"id": 21, "zh": "受精发生在输卵管内", "en": "Fertilisation occurs in the fallopian tube", "ms": "Persenyawaan berlaku dalam tiub fallopio", "correct": True,
     "explanation_zh": "正确，受精发生在输卵管", "explanation_en": "Correct, fertilisation occurs in fallopian tube", "explanation_ms": "Betul, persenyawaan berlaku dalam tiub fallopio"},
    {"id": 22, "zh": "精子是女性生殖细胞", "en": "Sperms are female reproductive cells", "ms": "Sperma adalah sel pembiakan perempuan", "correct": False,
     "explanation_zh": "精子是男性生殖细胞", "explanation_en": "Sperms are male reproductive cells", "explanation_ms": "Sperma adalah sel pembiakan lelaki"},
    {"id": 23, "zh": "子宫是胎儿生长的地方", "en": "Uterus is where the fetus grows", "ms": "Uterus adalah tempat janin tumbuh", "correct": True,
     "explanation_zh": "正确，子宫是胎儿生长的地方", "explanation_en": "Correct, fetus grows in uterus", "explanation_ms": "Betul, janin tumbuh dalam uterus"},
    {"id": 24, "zh": "神经系统控制身体活动", "en": "Nervous system controls body activities", "ms": "Sistem saraf mengawal aktiviti badan", "correct": True,
     "explanation_zh": "正确，神经系统控制身体活动", "explanation_en": "Correct, nervous system controls body", "explanation_ms": "Betul, sistem saraf mengawal badan"},
    {"id": 25, "zh": "阴道是产生卵子的器官", "en": "Vagina is the organ that produces eggs", "ms": "Faraj adalah organ yang menghasilkan telur", "correct": False,
     "explanation_zh": "卵巢产生卵子，阴道是产道", "explanation_en": "Ovaries produce eggs, vagina is birth canal", "explanation_ms": "Ovari menghasilkan telur, faraj adalah saluran kelahiran"},
    {"id": 26, "zh": "胚胎植入子宫壁", "en": "Embryo implants into uterus wall", "ms": "Embrio menanam ke dinding uterus", "correct": True,
     "explanation_zh": "正确，胚胎会植入子宫壁", "explanation_en": "Correct, embryo implants into uterus wall", "explanation_ms": "Betul, embrio menanam ke dinding uterus"},
    {"id": 27, "zh": "脊髓属于周围神经系统", "en": "Spinal cord is part of peripheral nervous system", "ms": "Saraf tunjang adalah sebahagian daripada sistem saraf periferi", "correct": False,
     "explanation_zh": "脊髓属于中枢神经系统", "explanation_en": "Spinal cord is part of central nervous system", "explanation_ms": "Saraf tunjang adalah sebahagian daripada sistem saraf pusat"},
    {"id": 28, "zh": "繁殖对人类不重要", "en": "Reproduction is not important to humans", "ms": "Pembiakan tidak penting kepada manusia", "correct": False,
     "explanation_zh": "繁殖很重要，确保物种延续", "explanation_en": "Reproduction is important for species continuation", "explanation_ms": "Pembiakan penting untuk kesinambungan spesies"},
    {"id": 29, "zh": "胎儿在子宫内生长约9个月", "en": "Fetus grows in uterus for about 9 months", "ms": "Janin tumbuh dalam uterus selama kira-kira 9 bulan", "correct": True,
     "explanation_zh": "正确，人类怀孕约9个月", "explanation_en": "Correct, human pregnancy is about 9 months", "explanation_ms": "Betul, kehamilan manusia adalah kira-kira 9 bulan"},
    {"id": 30, "zh": "脑是中枢神经系统的一部分", "en": "Brain is part of the central nervous system", "ms": "Otak adalah sebahagian daripada sistem saraf pusat", "correct": True,
     "explanation_zh": "正确，脑是中枢神经系统的主要部分", "explanation_en": "Correct, brain is main part of CNS", "explanation_ms": "Betul, otak adalah bahagian utama SSP"}
]

# 连线题题库 (10题)
matching_data = [
    {"id": 31, "left_zh": "睾丸", "left_en": "Testis", "left_ms": "Testis", "right_zh": "产生精子", "right_en": "Produces sperms", "right_ms": "Menghasilkan sperma"},
    {"id": 32, "left_zh": "卵巢", "left_en": "Ovary", "left_ms": "Ovari", "right_zh": "产生卵子", "right_en": "Produces eggs", "right_ms": "Menghasilkan telur"},
    {"id": 33, "left_zh": "输卵管", "left_en": "Fallopian tube", "left_ms": "Tiub fallopio", "right_zh": "受精场所", "right_en": "Site of fertilisation", "right_ms": "Tempat persenyawaan"},
    {"id": 34, "left_zh": "子宫", "left_en": "Uterus", "left_ms": "Uterus", "right_zh": "胚胎发育", "right_en": "Embryo development", "right_ms": "Perkembangan embrio"},
    {"id": 35, "left_zh": "阴茎", "left_en": "Penis", "left_ms": "Zakar", "right_zh": "排尿和输送精子", "right_en": "Urination and sperm delivery", "right_ms": "Kencing dan hantar sperma"},
    {"id": 36, "left_zh": "阴道", "left_en": "Vagina", "left_ms": "Faraj", "right_zh": "产道", "right_en": "Birth canal", "right_ms": "Saluran kelahiran"},
    {"id": 37, "left_zh": "脑", "left_en": "Brain", "left_ms": "Otak", "right_zh": "控制中心", "right_en": "Control center", "right_ms": "Pusat kawalan"},
    {"id": 38, "left_zh": "脊髓", "left_en": "Spinal cord", "left_ms": "Saraf tunjang", "right_zh": "传递信息", "right_en": "Transmits information", "right_ms": "Menghantar maklumat"},
    {"id": 39, "left_zh": "精子", "left_en": "Sperm", "left_ms": "Sperma", "right_zh": "男性生殖细胞", "right_en": "Male reproductive cell", "right_ms": "Sel pembiakan lelaki"},
    {"id": 40, "left_zh": "卵子", "left_en": "Egg", "left_ms": "Telur", "right_zh": "女性生殖细胞", "right_en": "Female reproductive cell", "right_ms": "Sel pembiakan perempuan"}
]

# 填空题题库 (10题)
fill_questions = [
    {"id": 41, "sentence_zh": "________ 是男性生殖细胞，________ 是女性生殖细胞。", "sentence_en": "________ are male reproductive cells, ________ are female reproductive cells.", "sentence_ms": "________ ialah sel pembiakan lelaki, ________ ialah sel pembiakan perempuan.",
     "answers_zh": ["精子", "卵子"], "answers_en": ["Sperms", "Eggs"], "answers_ms": ["Sperma", "Telur"], "blanks": 2},
    {"id": 42, "sentence_zh": "受精卵发育成 ________，然后在 ________ 内生长。", "sentence_en": "The fertilised egg develops into ________, then grows in the ________.", "sentence_ms": "Telur yang disenyawakan berkembang menjadi ________, kemudian tumbuh dalam ________.",
     "answers_zh": ["胚胎", "子宫"], "answers_en": ["embryo", "uterus"], "answers_ms": ["embrio", "uterus"], "blanks": 2},
    {"id": 43, "sentence_zh": "中枢神经系统由 ________ 和 ________ 组成。", "sentence_en": "The central nervous system consists of ________ and ________.", "sentence_ms": "Sistem saraf pusat terdiri daripada ________ dan ________.",
     "answers_zh": ["脑", "脊髓"], "answers_en": ["brain", "spinal cord"], "answers_ms": ["otak", "saraf tunjang"], "blanks": 2},
    {"id": 44, "sentence_zh": "________ 连接中枢神经系统和身体各部位。", "sentence_en": "________ connects the central nervous system to the body.", "sentence_ms": "________ menyambungkan sistem saraf pusat ke badan.",
     "answers_zh": ["周围神经系统"], "answers_en": ["peripheral nervous system"], "answers_ms": ["sistem saraf periferi"], "blanks": 1},
    {"id": 45, "sentence_zh": "睾丸的功能是产生 ________ 和雄性激素。", "sentence_en": "The function of testis is to produce ________ and male hormones.", "sentence_ms": "Fungsi testis adalah untuk menghasilkan ________ dan hormon lelaki.",
     "answers_zh": ["精子"], "answers_en": ["sperms"], "answers_ms": ["sperma"], "blanks": 1},
    {"id": 46, "sentence_zh": "卵巢的功能是产生 ________ 和雌性激素。", "sentence_en": "The function of ovary is to produce ________ and female hormones.", "sentence_ms": "Fungsi ovari adalah untuk menghasilkan ________ dan hormon perempuan.",
     "answers_zh": ["卵子"], "answers_en": ["eggs"], "answers_ms": ["telur"], "blanks": 1},
    {"id": 47, "sentence_zh": "________ 是受精发生的场所。", "sentence_en": "________ is the site of fertilisation.", "sentence_ms": "________ adalah tempat persenyawaan berlaku.",
     "answers_zh": ["输卵管"], "answers_en": ["Fallopian tube"], "answers_ms": ["Tiub fallopio"], "blanks": 1},
    {"id": 48, "sentence_zh": "人类繁殖的重要性是确保 ________ 延续。", "sentence_en": "The importance of human reproduction is to ensure ________ continuation.", "sentence_ms": "Kepentingan pembiakan manusia adalah untuk memastikan ________ berterusan.",
     "answers_zh": ["物种"], "answers_en": ["species"], "answers_ms": ["spesies"], "blanks": 1},
    {"id": 49, "sentence_zh": "胎儿在子宫内生长约 ________ 个月。", "sentence_en": "Fetus grows in the uterus for about ________ months.", "sentence_ms": "Janin tumbuh dalam uterus selama kira-kira ________ bulan.",
     "answers_zh": ["9"], "answers_en": ["9"], "answers_ms": ["9"], "blanks": 1},
    {"id": 50, "sentence_zh": "________ 系统控制我们的思考、记忆和身体活动。", "sentence_en": "The ________ system controls our thinking, memory and body activities.", "sentence_ms": "Sistem ________ mengawal pemikiran, ingatan dan aktiviti badan kita.",
     "answers_zh": ["神经"], "answers_en": ["nervous"], "answers_ms": ["saraf"], "blanks": 1}
]

# ==================== 侧边栏 ====================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/scientist.png", width=80)
    
    student_name = st.text_input("👤 姓名 / Name / Nama", placeholder="请输入您的姓名")
    
    st.markdown("---")
    st.markdown("### 📊 成绩统计")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("✅ 正确", st.session_state.correct_count)
    with col2:
        st.metric("❌ 错误", st.session_state.wrong_count)
    
    st.metric("📊 总题数", st.session_state.total_questions)
    
    if st.session_state.total_questions > 0:
        percentage = (st.session_state.correct_count / st.session_state.total_questions) * 100
        st.progress(percentage / 100)
        st.metric("📈 正确率", f"{percentage:.1f}%")
    
    st.markdown("---")
    st.markdown("### ⭐ 游戏得分")
    st.markdown(f"<h1 style='text-align: center; color: #fc4a1a;'>{st.session_state.score}</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎯 学习目标")
    st.markdown("""
    - ✅ 确认男性和女性的生殖器官
    - ✅ 说出中枢神经系统的主要部位
    - ✅ 讲述生殖器官的功能
    - ✅ 推论繁殖对人类的重要性
    - ✅ 总结神经系统的重要性
    """)

# ==================== 主游戏区域 ====================
# 统计面板
st.markdown(f"""
<div class="stats-panel">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <h3>🎮 游戏区域 | Game Area | Kawasan Permainan</h3>
            <p>学生: {student_name if student_name else "未输入"}</p>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 0.9rem;">当前得分 | Current Score | Skor Semasa</div>
            <div style="font-size: 2rem; font-weight: bold;">⭐ {st.session_state.score}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 语言选择
lang = st.radio(
    "选择语言 / Select Language / Pilih Bahasa",
    ["中文", "English", "Bahasa Malaysia"],
    horizontal=True,
    label_visibility="collapsed"
)
lang_map = {"中文": "zh", "English": "en", "Bahasa Malaysia": "ms"}
current_lang = lang_map[lang]

# 三语标签
st.markdown("""
<div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 20px;">
    <span style="background: #e55039; color: white; padding: 5px 25px; border-radius: 30px;">🇨🇳 中文</span>
    <span style="background: #4a69bd; color: white; padding: 5px 25px; border-radius: 30px;">🇬🇧 English</span>
    <span style="background: #f6b93b; color: white; padding: 5px 25px; border-radius: 30px;">🇲🇾 Bahasa Malaysia</span>
</div>
""", unsafe_allow_html=True)

# 游戏类型选择
game_type = st.radio(
    "选择游戏类型 / Select Game Type / Pilih Jenis Permainan",
    ["📝 选择题 (15题)", "✓✗ 对错题 (15题)", "🔗 连线题 (10题)", "✏️ 填空题 (10题)"],
    horizontal=True,
    label_visibility="collapsed"
)

if game_type == "📝 选择题 (15题)":
    st.session_state.current_game = "quiz"
    questions = quiz_questions
    total_q = 15
elif game_type == "✓✗ 对错题 (15题)":
    st.session_state.current_game = "truefalse"
    questions = tf_questions
    total_q = 15
elif game_type == "🔗 连线题 (10题)":
    st.session_state.current_game = "matching"
    questions = matching_data
    total_q = 10
else:
    st.session_state.current_game = "fill"
    questions = fill_questions
    total_q = 10

# 初始化当前题目标题
if f'{st.session_state.current_game}_index' not in st.session_state:
    st.session_state[f'{st.session_state.current_game}_index'] = 0

# 显示游戏
if game_type == "📝 选择题 (15题)":
    # 选择题游戏
    idx = st.session_state.quiz_index if 'quiz_index' in st.session_state else 0
    if idx < len(quiz_questions):
        q = quiz_questions[idx]
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <span style="font-size: 1.2rem;">第 <strong style="color: #fc4a1a; font-size: 1.5rem;">{idx+1}</strong> / {len(quiz_questions)} 题</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 三语题目显示
        st.markdown(f"""
        <div style="background: #f0f8ff; border-radius: 30px; padding: 20px; margin-bottom: 20px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
                <div><strong style="color: #e55039;">🇨🇳 中文</strong><br>{q['zh']}</div>
                <div><strong style="color: #4a69bd;">🇬🇧 English</strong><br>{q['en']}</div>
                <div><strong style="color: #f6b93b;">🇲🇾 BM</strong><br>{q['ms']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 当前语言题目
        st.markdown(f"""
        <div style="background: white; border-radius: 30px; padding: 25px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
            <h3>{q[current_lang]}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 选项
        options_current = q[f'options_{current_lang}']
        options_zh = q['options_zh']
        options_en = q['options_en']
        options_ms = q['options_ms']
        
        st.markdown("### 选项 / Options / Pilihan")
        
        cols = st.columns(2)
        for i, opt in enumerate(options_current):
            with cols[i % 2]:
                if st.button(f"{chr(65+i)}. {opt}\n\n📝 {options_zh[i]} | {options_en[i]} | {options_ms[i]}", 
                             key=f"quiz_opt_{idx}_{i}", use_container_width=True):
                    st.session_state[f'quiz_selected_{idx}'] = i
        
        # 检查答案
        if st.button("✓ 检查答案 / Check Answer / Semak Jawapan", key="quiz_check", use_container_width=True):
            selected = st.session_state.get(f'quiz_selected_{idx}', None)
            if selected is not None:
                is_correct = selected == q['correct']
                q_id = f"quiz_{q['id']}"
                
                if q_id not in st.session_state.answered_questions:
                    st.session_state.answered_questions.add(q_id)
                    st.session_state.total_questions += 1
                    if is_correct:
                        st.session_state.correct_count += 1
                        st.session_state.score += 10
                    else:
                        st.session_state.wrong_count += 1
                
                if is_correct:
                    st.success(f"✅ 正确！{q[f'explanation_{current_lang}']}")
                else:
                    correct_letter = chr(65 + q['correct'])
                    correct_text = options_current[q['correct']]
                    st.error(f"❌ 错误！正确答案是 {correct_letter}. {correct_text}\n\n{q[f'explanation_{current_lang}']}")
                
                st.session_state[f'quiz_answered_{idx}'] = True
            else:
                st.warning("请先选择一个答案")
        
        # 下一题
        if st.session_state.get(f'quiz_answered_{idx}', False):
            if st.button("↪ 下一题 / Next Question / Soalan Seterusnya", key="quiz_next", use_container_width=True):
                st.session_state.quiz_index = idx + 1
                st.session_state[f'quiz_answered_{idx}'] = False
                if idx + 1 >= len(quiz_questions):
                    st.session_state.quiz_index = 0
                st.rerun()
    else:
        st.session_state.quiz_index = 0
        st.rerun()

elif game_type == "✓✗ 对错题 (15题)":
    # 对错题游戏
    idx = st.session_state.tf_index if 'tf_index' in st.session_state else 0
    if idx < len(tf_questions):
        q = tf_questions[idx]
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <span style="font-size: 1.2rem;">第 <strong style="color: #fc4a1a; font-size: 1.5rem;">{idx+1}</strong> / {len(tf_questions)} 题</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 三语陈述
        st.markdown(f"""
        <div style="background: #f0f8ff; border-radius: 30px; padding: 20px; margin-bottom: 20px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
                <div><strong style="color: #e55039;">🇨🇳 中文</strong><br>{q['zh']}</div>
                <div><strong style="color: #4a69bd;">🇬🇧 English</strong><br>{q['en']}</div>
                <div><strong style="color: #f6b93b;">🇲🇾 BM</strong><br>{q['ms']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 当前语言陈述
        st.markdown(f"""
        <div style="background: white; border-radius: 30px; padding: 30px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
            <h3>{q[current_lang]}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 正确/错误按钮
        col1, col2 = st.columns(2)
        with col1:
            true_btn = st.button("✅ 正确 / True / Betul", key=f"tf_true_{idx}", use_container_width=True)
        with col2:
            false_btn = st.button("❌ 错误 / False / Salah", key=f"tf_false_{idx}", use_container_width=True)
        
        if true_btn:
            st.session_state[f'tf_selected_{idx}'] = True
        if false_btn:
            st.session_state[f'tf_selected_{idx}'] = False
        
        # 检查答案
        if st.button("✓ 检查答案 / Check Answer / Semak Jawapan", key="tf_check", use_container_width=True):
            selected = st.session_state.get(f'tf_selected_{idx}', None)
            if selected is not None:
                is_correct = selected == q['correct']
                q_id = f"tf_{q['id']}"
                
                if q_id not in st.session_state.answered_questions:
                    st.session_state.answered_questions.add(q_id)
                    st.session_state.total_questions += 1
                    if is_correct:
                        st.session_state.correct_count += 1
                        st.session_state.score += 10
                    else:
                        st.session_state.wrong_count += 1
                
                if is_correct:
                    st.success(f"✅ 正确！{q[f'explanation_{current_lang}']}")
                else:
                    st.error(f"❌ 错误！{q[f'explanation_{current_lang}']}")
                
                st.session_state[f'tf_answered_{idx}'] = True
            else:
                st.warning("请选择正确或错误")
        
        # 下一题
        if st.session_state.get(f'tf_answered_{idx}', False):
            if st.button("↪ 下一题 / Next Question / Soalan Seterusnya", key="tf_next", use_container_width=True):
                st.session_state.tf_index = idx + 1
                st.session_state[f'tf_answered_{idx}'] = False
                if idx + 1 >= len(tf_questions):
                    st.session_state.tf_index = 0
                st.rerun()
    else:
        st.session_state.tf_index = 0
        st.rerun()

elif game_type == "🔗 连线题 (10题)":
    # 连线题游戏
    st.markdown("""
    <div style="background: white; border-radius: 30px; padding: 25px; text-align: center; margin-bottom: 20px;">
        <h3>🔗 连线配对游戏 | Matching Game | Permainan Padanan</h3>
        <p>将左边的器官与右边的功能正确连线</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 显示连线题
    if 'matching_matches' not in st.session_state:
        st.session_state.matching_matches = {}
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 器官 | Organs | Organ")
        for item in matching_data:
            left_text = item[f'left_{current_lang}']
            left_key = f"{item['id']}_left"
            if st.button(f"📌 {left_text}\n\n{item['left_zh']} | {item['left_en']} | {item['left_ms']}", 
                         key=left_key, use_container_width=True):
                st.session_state.selected_left = item['id']
    
    with col2:
        st.markdown("### 功能 | Functions | Fungsi")
        for item in matching_data:
            right_text = item[f'right_{current_lang}']
            right_key = f"{item['id']}_right"
            if st.button(f"🔗 {right_text}\n\n{item['right_zh']} | {item['right_en']} | {item['right_ms']}", 
                         key=right_key, use_container_width=True):
                if hasattr(st.session_state, 'selected_left'):
                    left_id = st.session_state.selected_left
                    if left_id == item['id']:
                        st.success(f"✅ 正确！{item[f'left_{current_lang}']} ↔ {item[f'right_{current_lang}']}")
                        q_id = f"match_{item['id']}"
                        if q_id not in st.session_state.answered_questions:
                            st.session_state.answered_questions.add(q_id)
                            st.session_state.total_questions += 1
                            st.session_state.correct_count += 1
                            st.session_state.score += 5
                        st.session_state.matching_matches[item['id']] = True
                    else:
                        st.error(f"❌ 错误！{left_id} 和 {item['id']} 不匹配")
                        q_id = f"match_wrong_{left_id}_{item['id']}"
                        if q_id not in st.session_state.answered_questions:
                            st.session_state.answered_questions.add(q_id)
                            st.session_state.total_questions += 1
                            st.session_state.wrong_count += 1
                    delattr(st.session_state, 'selected_left')
                    st.rerun()

elif game_type == "✏️ 填空题 (10题)":
    # 填空题游戏
    idx = st.session_state.fill_index if 'fill_index' in st.session_state else 0
    if idx < len(fill_questions):
        q = fill_questions[idx]
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <span style="font-size: 1.2rem;">第 <strong style="color: #fc4a1a; font-size: 1.5rem;">{idx+1}</strong> / {len(fill_questions)} 题</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 三语句子
        st.markdown(f"""
        <div style="background: #f0f8ff; border-radius: 30px; padding: 20px; margin-bottom: 20px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
                <div><strong style="color: #e55039;">🇨🇳 中文</strong><br>{q['sentence_zh']}</div>
                <div><strong style="color: #4a69bd;">🇬🇧 English</strong><br>{q['sentence_en']}</div>
                <div><strong style="color: #f6b93b;">🇲🇾 BM</strong><br>{q['sentence_ms']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 当前语言句子
        sentence_current = q[f'sentence_{current_lang}']
        st.markdown(f"""
        <div style="background: white; border-radius: 30px; padding: 25px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
            <h3>{sentence_current.replace('________', '<span style="color: #1976d2; text-decoration: underline;">________</span>')}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 答案输入框
        user_answers = []
        for i in range(q['blanks']):
            answer = st.text_input(f"答案 {i+1} / Answer {i+1} / Jawapan {i+1}", 
                                   key=f"fill_ans_{idx}_{i}", placeholder="请输入答案")
            user_answers.append(answer)
        
        # 检查答案
        if st.button("✓ 检查答案 / Check Answer / Semak Jawapan", key="fill_check", use_container_width=True):
            answers_current = q[f'answers_{current_lang}']
            correct_count = 0
            for i, ans in enumerate(user_answers):
                if ans.strip().lower() == answers_current[i].lower():
                    correct_count += 1
            
            all_correct = correct_count == q['blanks']
            q_id = f"fill_{q['id']}"
            
            if q_id not in st.session_state.answered_questions:
                st.session_state.answered_questions.add(q_id)
                st.session_state.total_questions += 1
                if all_correct:
                    st.session_state.correct_count += 1
                    st.session_state.score += 15
                else:
                    st.session_state.wrong_count += 1
            
            if all_correct:
                st.success("✅ 完全正确！")
            else:
                st.error(f"❌ 答对了 {correct_count}/{q['blanks']} 个")
                st.info(f"正确答案: {', '.join(answers_current)}")
            
            st.session_state[f'fill_answered_{idx}'] = True
        
        # 下一题
        if st.session_state.get(f'fill_answered_{idx}', False):
            if st.button("↪ 下一题 / Next Question / Soalan Seterusnya", key="fill_next", use_container_width=True):
                st.session_state.fill_index = idx + 1
                st.session_state[f'fill_answered_{idx}'] = False
                if idx + 1 >= len(fill_questions):
                    st.session_state.fill_index = 0
                st.rerun()
    else:
        st.session_state.fill_index = 0
        st.rerun()

# 重置游戏按钮
st.markdown("---")
reset_col1, reset_col2, reset_col3 = st.columns([1, 2, 1])
with reset_col2:
    if st.button("🔄 重新开始全部游戏 / Reset All Games / Mulakan Semua Permainan Semula", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key not in ['student_name']:
                del st.session_state[key]
        st.session_state.score = 0
        st.session_state.correct_count = 0
        st.session_state.wrong_count = 0
        st.session_state.total_questions = 0
        st.session_state.answered_questions = set()
        st.session_state.quiz_index = 0
        st.session_state.tf_index = 0
        st.session_state.fill_index = 0
        if hasattr(st.session_state, 'selected_left'):
            delattr(st.session_state, 'selected_left')
        st.rerun()

# 页脚
st.markdown("""
<div class="footer">
    <p>🧪 六年级科学 - 人类繁殖与神经系统 | Year 6 Science - Human Reproduction & Nervous System | Sains Tahun 6 - Pembiakan Manusia & Sistem Saraf</p>
</div>
""", unsafe_allow_html=True)
