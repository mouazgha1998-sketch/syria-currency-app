import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="محول عملات سوريا - عد للعشرة", page_icon="💰")

# --- إدارة حالة الأسعار ---
if 'usd_to_try' not in st.session_state:
    st.session_state.usd_to_try = 45.18
if 'try_to_syp_old' not in st.session_state:
    st.session_state.try_to_syp_old = 295.0

# --- لوحة التحكم (في القائمة الجانبية) ---
with st.sidebar:
    st.header("⚙️ إعدادات المدير")
    # ملاحظة: يمكنك تغيير كلمة المرور هنا
    password = st.text_input("أدخل كلمة المرور لتعديل الأسعار:", type="password")
    
    if password == "1234": 
        st.success("تم الدخول بنجاح")
        new_usd_try = st.number_input("سعر الدولار مقابل التركي:", value=st.session_state.usd_to_try)
        new_try_syp = st.number_input("سعر التركي مقابل السوري القديم:", value=st.session_state.try_to_syp_old)
        
        if st.button("تحديث الأسعار"):
            st.session_state.usd_to_try = new_usd_try
            st.session_state.try_to_syp_old = new_try_syp
            st.toast("✅ تم تحديث الأسعار بنجاح!")
    elif password != "":
        st.error("كلمة المرور غير صحيحة")

# --- واجهة التطبيق الرئيسية ---
st.title("💰 محول العملات السريع")
st.info(f"الأسعار الحالية: 1$ = {st.session_state.usd_to_try} TL | 1 TL = {st.session_state.try_to_syp_old} ل.س")

# المدخلات
col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("المبلغ المراد تحويله:", min_value=0.0, value=1.0, step=1.0)
with col2:
    currency = st.selectbox("عملة المبلغ المدخل:", 
                            ["ليرة تركية (TRY)", "دولار أمريكي (USD)", "ليرة سورية جديدة", "ليرة سورية قديمة"])

# حسابات التحويل
usd_to_try = st.session_state.usd_to_try
try_to_syp_old = st.session_state.try_to_syp_old

if "تركية" in currency:
    base_try = amount
elif "دولار" in currency:
    base_try = amount * usd_to_try
elif "جديدة" in currency:
    base_try = (amount * 100) / try_to_syp_old
else:
    base_try = amount / try_to_syp_old

# النتائج النهائية
st.divider()
c1, c2 = st.columns(2)
c1.metric("💵 دولار أمريكي", f"{base_try / usd_to_try:,.2f} $")
c2.metric("🇹🇷 ليرة تركية", f"{base_try:,.2f} TL")

# استخدام إيموجي العلم الجديد (الأخضر والأبيض والأسود مع 3 نجوم حمراء)
# ملاحظة: بعض الأنظمة القديمة قد تظهر العلم القديم، لذا نستخدم وصفاً نصياً بجانبه للتأكيد
st.write("---")
c3, c4 = st.columns(2)
with c3:
    st.subheader("🟢 ليرة سورية (جديدة)")
    st.title(f"{ (base_try * try_to_syp_old) / 100 :,.2f}")
with c4:
    st.subheader("📜 ليرة سورية (قديمة)")
    st.title(f"{ base_try * try_to_syp_old :,.2f}")

st.caption("تم ضبط الحسابات على أساس حذف صفرين (100 قديم = 1 جديد).")
