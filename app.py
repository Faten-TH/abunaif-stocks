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
    .main-title { font-size: 28px; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #1E3A8A; color: white; font-weight: bold; border-radius: 10px; }
    </style>
""",
    unsafe_allow_html=True,
)


def safe(info, key, default=0):
    v = info.get(key, default)
    return default if v is None else v


# القائمة الجانبية
st.sidebar.title("🏢 بوابة التحليل الشاملة")
st.sidebar.write("مرحباً بك يا **أبو نايف** 🌹")

program = st.sidebar.radio(
    "اختر برنامج التحليل المطلوب:",
    [
        "1️⃣ كود مايك (تحليل وجدولة تفصيلية)",
        "2️⃣ كود أبو نايف (BLACK DIAMOND الشامل)",
        "3️⃣ كود القيمة العادلة وهامش الأمان التفصيلي",
        "4️⃣ كود الجوهرة الكاملة (JEWEL V100 - تفصيلي)",
    ],
)

st.markdown(
    '<div class="main-title">🏢 نظام تحليل الأسهم والشركات المطور الشامل 🏢</div>',
    unsafe_allow_html=True,
)

# ==========================================
# 1. كود مايك التفصيلي
# ==========================================
if "1️⃣" in program:
    st.subheader("📊 كود مايك - تحليل المعايير التفصيلية")
    st.info(
        "يعرض التفاصيل الكاملة لنمو الإيرادات، التدفق النقدي، نسبة الديون، ملكية المؤسسات، ومكرر الربحية."
    )

    default_tickers = "NVDA, APLD, IREN, ZETA, RKLB, CIFR, SLNH"
    input_stocks = st.text_input(
        "أدخل رموز الأسهم مفصولة بفاصلة:", default_tickers
    )

    if st.button("🚀 تشغيل التحليل التفصيلي"):
        tickers = [
            x.strip().upper() for x in input_stocks.split(",") if x.strip()
        ]
        rows = []
        with st.spinner("جاري جلب كافة المعايير المالية..."):
            for ticker in tickers:
                try:
                    info = yf.Ticker(ticker).info
                    score = 0

                    rev = safe(info, "revenueGrowth", None)
                    if rev and rev >= 0.30:
                        score += 30
                    elif rev and rev >= 0.15:
                        score += 20
                    elif rev and rev > 0:
                        score += 10

                    fcf = safe(info, "freeCashflow", None)
                    if fcf and fcf > 0:
                        score += 20

                    debt = safe(info, "debtToEquity", None)
                    if debt is not None and debt < 20:
                        score += 20
                    elif debt is not None and debt < 50:
                        score += 10

                    inst = safe(info, "heldPercentInstitutions", None)
                    if inst and inst >= 0.70:
                        score += 20
                    elif inst and inst >= 0.50:
                        score += 10

                    pe = safe(info, "trailingPE", None)
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
                            "الشركة": safe(info, "shortName", ticker),
                            "السعر ($)": safe(info, "currentPrice", 0),
                            "نمو الإيرادات": f"{rev*100:.1f}%"
                            if rev is not None
                            else "غير متوفر",
                            "التدفق النقدي الحر ($)": f"{fcf:,.0f}"
                            if fcf is not None
                            else "غير متوفر",
                            "نسبة الديون %": f"{debt:.1f}%"
                            if debt is not None
                            else "غير متوفر",
                            "ملكية المؤسسات": f"{inst*100:.1f}%"
                            if inst is not None
                            else "غير متوفر",
                            "مكرر الربحية (P/E)": f"{pe:.1f}"
                            if pe is not None
                            else "غير متوفر",
                            "النقاط / 100": score,
                            "التقييم": rating,
                        }
                    )
                except Exception:
                    pass

        if rows:
            df = pd.DataFrame(rows).sort_values(
                "النقاط / 100", ascending=False
            )
            st.dataframe(df, use_container_width=True)

# ==========================================
# 2. كود أبو نايف - BLACK DIAMOND الشامل
# ==========================================
elif "2️⃣" in program:
    st.subheader("💎 كود أبو نايف - BLACK DIAMOND (تفصيل كامل للمعايير)")
    input_stocks = st.text_input(
        "أدخل رموز الأسهم مفصولة بفاصلة:", "NVDA, PLTR, META, AMZN, AAPL"
    )

    if st.button("🚀 تحليل جميع الجوانب المالية"):
        tickers = [
            x.strip().upper() for x in input_stocks.split(",") if x.strip()
        ]
        results = []
        with st.spinner("جاري حساب جميع تفاصيل BLACK DIAMOND..."):
            for symbol in tickers:
                try:
                    info = yf.Ticker(symbol).info

                    rev = safe(info, "revenueGrowth", 0)
                    debt = safe(info, "debtToEquity", 0)
                    inst = safe(info, "heldPercentInstitutions", 0)
                    fcf = safe(info, "freeCashflow", 0)
                    profit_margin = safe(info, "profitMargins", 0)
                    roe = safe(info, "returnOnEquity", 0)

                    score = 0
                    if rev >= 0.25:
                        score += 25
                    elif rev > 0:
                        score += 15

                    if debt < 50:
                        score += 20
                    elif debt < 100:
                        score += 10

                    if inst >= 0.50:
                        score += 20
                    elif inst >= 0.30:
                        score += 10

                    if fcf > 0:
                        score += 15
                    if profit_margin > 0.15:
                        score += 10
                    if roe > 0.15:
                        score += 10

                    results.append(
                        {
                            "السهم": symbol,
                            "اسم الشركة": safe(info, "shortName", symbol),
                            "السعر الحالي ($)": safe(
                                info, "currentPrice", safe(info, "previousClose", 0)
                            ),
                            "نمو الإيرادات %": f"{rev*100:.1f}%",
                            "الديون للحقوق %": f"{debt:.1f}%",
                            "ملكية المؤسسات %": f"{inst*100:.1f}%",
                            "هامش الربح %": f"{profit_margin*100:.1f}%",
                            "العائد على الملكية %": f"{roe*100:.1f}%",
                            "التدفق النقدي": "إيجابي 🟢"
                            if fcf > 0
                            else "سلبي 🔴",
                            "النتيجة النهائية": f"{score} / 100",
                            "التقييم": "💎 الماس أسود"
                            if score >= 80
                            else "🟢 جيد جداً"
                            if score >= 60
                            else "👀 تحت المراقبة",
                        }
                    )
                except Exception:
                    pass

        if results:
            st.dataframe(pd.DataFrame(results), use_container_width=True)

# ==========================================
# 3. كود القيمة العادلة التفصيلي
# ==========================================
elif "3️⃣" in program:
    st.subheader("📊 حساب القيمة العادلة وتفاصيل التقييم المالي")
    symbol = st.text_input("أدخل رمز السهم:", "NVDA").strip().upper()

    if st.button("🔍 عرض تفاصيل التقييم وقيم المعادلات"):
        with st.spinner("جاري استخراج المؤشرات وقيم النموذج..."):
            try:
                info = yf.Ticker(symbol).info
                price = safe(
                    info, "currentPrice", safe(info, "regularMarketPrice", 0)
                )
                eps = safe(info, "trailingEps", 0)
                rev = safe(info, "revenueGrowth", 0)
                pe = safe(info, "trailingPE", 0)
                book_value = safe(info, "bookValue", 0)

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

                st.markdown("### 📌 النتائج الرئيسية:")
                col1, col2, col3 = st.columns(3)
                col1.metric("السعر الحالي بالسوق", f"${price:.2f}")
                col2.metric("القيمة العادلة المحسوبة", f"${fair_value:.2f}")
                col3.metric("هامش الأمان", f"{margin:.1f}%")

                st.markdown("---")
                st.markdown("### 📋 التفاصيل والمدخلات الحسابية:")
                details = {
                    "المعيار / المؤشر": [
                        "ربحية السهم (EPS)",
                        "نمو الإيرادات المتوقع",
                        "مكرر الربحية الحالي (P/E)",
                        "القيمة الدفترية للسهم",
                        "تقييم مكرر الربحية المستهدف",
                        "تقييم التدفقات المخصومة المفترضة",
                    ],
                    "القيمة": [
                        f"${eps:.2f}",
                        f"{rev*100:.2f}%",
                        f"{pe:.2f}",
                        f"${book_value:.2f}",
                        f"${fair_pe:.2f}",
                        f"${fair_dcf:.2f}",
                    ],
                }
                st.table(pd.DataFrame(details))

                if margin >= 15:
                    st.success("🟢 السهم يتداول بأقل من قيمته العادلة (فرصة ممتازة للفرز)")
                elif margin >= -10:
                    st.warning("🟡 السهم متوازن وقريب من قيمته العادلة")
                else:
                    st.error("🔴 السهم أعلى من قيمته العادلة حالياً")
            except Exception as e:
                st.error(f"حدث خطأ أثناء جلب البيانات: {e}")

# ==========================================
# 4. كود الجوهرة الكاملة (JEWEL V100 - التفصيلي)
# ==========================================
elif "4️⃣" in program:
    st.subheader("💎 فلتر الجوهرة الشامل — JEWEL V100 (عرض جميع الشروط)")
    input_stocks = st.text_input(
        "أدخل رموز الأسهم للفحص الشامل التفصيلي:", "NVDA, PLTR, AMZN, META"
    )

    if st.button("🔍 اجراء فحص الجوهرة التفصيلي"):
        tickers = [
            x.strip().upper() for x in input_stocks.split(",") if x.strip()
        ]
        results = []

        with st.spinner("جاري فحص جميع الشروط والمؤشرات الماليّة..."):
            for symbol in tickers:
                try:
                    info = yf.Ticker(symbol).info
                    net_inc = safe(info, "netIncomeToCommon", 0)
                    ocf = safe(info, "operatingCashflow", 0)
                    fcf = safe(info, "freeCashflow", 0)
                    rev = safe(info, "revenueGrowth", 0)
                    gross_margin = safe(info, "grossMargins", 0)

                    # فحص الشروط الفردية
                    c1 = net_inc > 0  # ربحية صافية
                    c2 = ocf > 0  # تدفق تشغيلي موجبة
                    c3 = fcf > 0  # تدفق حر موجب
                    c4 = rev >= 0.25  # نمو إيرادات أعلى من 25%

                    all_passed = c1 and c2 and c3 and c4

                    score = 0
                    if c1:
                        score += 25
                    if c2:
                        score += 25
                    if c3:
                        score += 25
                    if c4:
                        score += 25

                    results.append(
                        {
                            "السهم": symbol,
                            "الشركة": safe(info, "shortName", symbol),
                            "ربحية الشركة": "✅ إيجابي"
                            if c1
                            else "❌ خاسرة",
                            "التدفق التشغيلي": "✅ موجب"
                            if c2
                            else "❌ سالب",
                            "التدفق الحر (FCF)": "✅ موجب"
                            if c3
                            else "❌ سالب",
                            "نمو الإيرادات (المستهدف >= 25%)": f"{rev*100:.1f}%",
                            "هامش المجمل": f"{gross_margin*100:.1f}%",
                            "حالة الاجتياز الإجمالية": "💎 جوهرة معتمدة"
                            if all_passed
                            else "❌ لم تجتز الشروط",
                            "درجة الفحص": f"{score} / 100",
                        }
                    )
                except Exception:
                    pass

        if results:
            st.dataframe(pd.DataFrame(results), use_container_width=True)
