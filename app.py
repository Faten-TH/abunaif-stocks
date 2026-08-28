
import pandas as pd
import streamlit as st
import yfinance as yf

# إعدادات الصفحة
st.set_page_config(
    page_title="بوابة أبو نايف للتحليل المالي",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# تصميم وتنسيق الواجهة
st.markdown(
    """
    <style>
    .main-title { font-size: 30px; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #1E3A8A; color: white; font-weight: bold; border-radius: 10px; }
    .card { background-color: #F3F4F6; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    </style>
""",
    unsafe_allow_html=True,
)


def safe(info, key, default=None):
    v = info.get(key, default)
    return default if v is None else v


def calculate_rsi(close, period=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / (avg_loss + 1e-9)
    return (100 - (100 / (1 + rs))).iloc[-1]


# ==========================================
# القائمة الجانبية (الشريط الجانبي)
# ==========================================
st.sidebar.image(
    "https://img.icons8.com/color/96/000000/financial-analytics.png"
)
st.sidebar.title("🏢 بوابة التحليل")
st.sidebar.write("مرحباً بك يا **أبو نايف**")

program = st.sidebar.radio(
    "اختر برنامج التحليل المطلوب:",
    [
        "1️⃣ كود مايك (تحليل وجدولة)",
        "2️⃣ كود أبو نايف (BLACK DIAMOND)",
        "3️⃣ كود القيمة العادلة",
        "4️⃣ كود الجوهرة الكاملة (JEWEL V100)",
    ],
)

st.markdown(
    '<div class="main-title">🏢 نظام تحليل الأسهم والشركات المطور 🏢</div>',
    unsafe_allow_html=True,
)

# ==========================================
# 1. كود مايك
# ==========================================
if "1️⃣" in program:
    st.subheader("📊 كود مايك المطور")
    st.info("يقوم هذا البرنامج بتحليل قائمة محددة سلفاً من الأسهم وتقييمها.")

    if st.button("🚀 تشغيل التحليل الآن"):
        tickers = ["NVDA", "APLD", "IREN", "ZETA", "RKLB", "CIFR", "SLNH"]
        rows = []
        with st.spinner("جاري جلب البيانات وتحليل الأسهم..."):
            for ticker in tickers:
                try:
                    info = yf.Ticker(ticker).info
                    score = 0
                    rev = info.get("revenueGrowth")
                    if rev and rev >= 0.30:
                        score += 30
                    elif rev and rev >= 0.15:
                        score += 20
                    elif rev and rev > 0:
                        score += 10

                    fcf = info.get("freeCashflow")
                    if fcf and fcf > 0:
                        score += 20

                    debt = info.get("debtToEquity")
                    if debt and debt < 20:
                        score += 20
                    elif debt and debt < 50:
                        score += 10

                    inst = info.get("heldPercentInstitutions")
                    if inst and inst >= 0.70:
                        score += 20
                    elif inst and inst >= 0.50:
                        score += 10

                    pe = info.get("trailingPE")
                    if pe and pe < 40:
                        score += 10

                    rating = (
                        "ممتاز ⭐⭐⭐"
                        if score >= 80
                        else "جيد ⭐⭐"
                        if score >= 60
                        else "متوسط ⭐"
                        if score >= 40
                        else "ضعيف"
                    )

                    rows.append(
                        {
                            "السهم": ticker,
                            "الشركة": info.get("shortName"),
                            "السعر ($)": info.get("currentPrice"),
                            "نمو الإيرادات %": round(rev * 100, 2)
                            if rev
                            else None,
                            "النتيجة": score,
                            "التقييم": rating,
                        }
                    )
                except Exception:
                    pass

        df = pd.DataFrame(rows).sort_values("النتيجة", ascending=False)
        st.dataframe(df, use_container_width=True)

# ==========================================
# 2. كود أبو نايف
# ==========================================
elif "2️⃣" in program:
    st.subheader("💎 كود أبو نايف - BLACK DIAMOND V37")
    input_stocks = st.text_input(
        "أدخل رموز الأسهم مفصولة بفاصلة:", "NVDA, PLTR, META"
    )

    if st.button("🚀 تحليل الأسهم"):
        tickers = [
            x.strip().upper() for x in input_stocks.split(",") if x.strip()
        ]
        results = []
        with st.spinner("جاري التحليل الشامل..."):
            for symbol in tickers:
                try:
                    info = yf.Ticker(symbol).info
                    rev = safe(info, "revenueGrowth", 0)
                    debt = safe(info, "debtToEquity", 100) / 100.0
                    inst = safe(info, "heldPercentInstitutions", 0)

                    score = 50  # حساب تقريبي مبسط للسرعة
                    if rev >= 0.25:
                        score += 20
                    if debt < 0.5:
                        score += 15
                    if inst > 0.3:
                        score += 15

                    results.append(
                        {
                            "السهم": symbol,
                            "الشركة": safe(info, "shortName", symbol),
                            "السعر ($)": safe(info, "currentPrice", 0),
                            "النتيجة / 100": score,
                            "التقييم": "💎 ممتاز"
                            if score >= 80
                            else "👀 مراقبة",
                        }
                    )
                except Exception:
                    pass

        st.dataframe(pd.DataFrame(results), use_container_width=True)

# ==========================================
# 3. كود القيمة العادلة
# ==========================================
elif "3️⃣" in program:
    st.subheader("📊 كود حساب القيمة العادلة وهامش الأمان")
    symbol = st.text_input("أدخل رمز السهم:", "NVDA").strip().upper()

    if st.button("🔍 احسب القيمة العادلة"):
        with st.spinner("جاري معالجة البيانات الماليّة..."):
            try:
                info = yf.Ticker(symbol).info
                price = safe(
                    info, "currentPrice", safe(info, "regularMarketPrice", 0)
                )
                eps = safe(info, "trailingEps", 0)
                rev = safe(info, "revenueGrowth", 0)

                fair_pe = max(eps * 20, 0)
                fair_dcf = price * (1 + max(rev, 0) * 2)
                fair_value = (
                    (fair_pe + fair_dcf) / 2 if fair_pe > 0 else price
                )

                margin = (
                    (fair_value - price) / fair_value * 100
                    if fair_value
                    else 0
                )

                col1, col2, col3 = st.columns(3)
                col1.metric("السعر الحالي", f"${price:.2f}")
                col2.metric("القيمة العادلة", f"${fair_value:.2f}")
                col3.metric("هامش الأمان", f"{margin:.1f}%")

                if margin >= 15:
                    st.success("🟢 السهم أقل من القيمة العادلة (مناسب للدراسة)")
                elif margin >= -10:
                    st.warning("🟡 السهم قريب من القيمة العادلة")
                else:
                    st.error("🔴 السهم أعلى من القيمة العادلة")
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

# ==========================================
# 4. كود الجوهرة الكاملة (JEWEL V100)
# ==========================================
elif "4️⃣" in program:
    st.subheader("💎 فلتر الجوهرة — النسخة المعتمدة JEWEL V100")
    input_stocks = st.text_input(
        "أدخل رموز الأسهم للفحص الإلزامي الشامل:", "NVDA, PLTR, AMZN"
    )

    if st.button("🔍 فحص الجوهرة"):
        tickers = [
            x.strip().upper() for x in input_stocks.split(",") if x.strip()
        ]
        results = []

        with st.spinner("جاري فحص الشروط الإلزامية والتقييم..."):
            for symbol in tickers:
                try:
                    info = yf.Ticker(symbol).info
                    net_inc = safe(info, "netIncomeToCommon", 0)
                    ocf = safe(info, "operatingCashflow", 0)
                    fcf = safe(info, "freeCashflow", 0)
                    rev = safe(info, "revenueGrowth", 0)

                    # الشروط الإلزامية
                    passed = (
                        net_inc > 0 and ocf > 0 and fcf > 0 and rev >= 0.25
                    )

                    score = 40
                    if net_inc > 0:
                        score += 15
                    if ocf > 0:
                        score += 15
                    if fcf > 0:
                        score += 15
                    if rev >= 0.25:
                        score += 15

                    results.append(
                        {
                            "السهم": symbol,
                            "الشركة": safe(info, "shortName", symbol),
                            "الشروط الإلزامية": "✅ اجتاز"
                            if passed
                            else "❌ لم يجتز",
                            "الدرجة الإجمالية": score,
                            "نمو الإيرادات": f"{rev*100:.1f}%",
                        }
                    )
                except Exception:
                    pass

        st.dataframe(pd.DataFrame(results), use_container_width=True)
