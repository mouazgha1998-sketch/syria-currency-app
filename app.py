import streamlit as st

st.set_page_config(page_title="محول عملات سوريا والتركية", page_icon="💰")

st.title("💰 محول العملات السريع")
st.write("أدخل المبلغ في أي خانة ليتم تحويله تلقائياً لبقية العملات")

# أسعار الصرف (يمكنك تعديلها هنا يدوياً مستقبلاً)
usd_to_try = 45.18
try_to_syp_old = 295.0
old_to_new_ratio = 100

# تصميم واجهة الإدخال
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("المبلغ:", min_value=0.0, value=1.0, step=1.0)
    
with col2:
    currency = st.selectbox("العملة المدخلة:", 
                            ["ليرة تركية (TRY)", "دولار أمريكي (USD)", "ليرة سورية جديدة", "ليرة سورية قديمة"])

# تحويل المدخل إلى ليرة تركية كقاعدة حسابية
if "تركية" in currency:
    base_try = amount
elif "دولار" in currency:
    base_try = amount * usd_to_try
elif "جديدة" in currency:
    base_try = (amount * old_to_new_ratio) / try_to_syp_old
else:
    base_try = amount / try_to_syp_old

# حساب القيم المقابلة
val_usd = base_try / usd_to_try
val_try = base_try
val_syp_old = base_try * try_to_syp_old
val_syp_new = val_syp_old / old_to_new_ratio

st.markdown("---")

# عرض النتائج في بطاقات جميلة
st.subheader("القيم المعادلة:")
c1, c2 = st.columns(2)
c1.info(f"💵 **دولار أمريكي**\n\n{val_usd:,.2f} $")
c2.success(f"🇹🇷 **ليرة تركية**\n\n{val_try:,.2f} TL")

c3, c4 = st.columns(2)
c3.warning(f"🇸🇾 **سوري (جديد)**\n\n{val_syp_new:,.2f}")
c4.error(f"📜 **سوري (قديم)**\n\n{val_syp_old:,.2f}")