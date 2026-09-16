import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GERMANY Export Growth Study", page_icon="🌍", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"]{direction:rtl;text-align:right;background:#fbfdfb}
[data-testid="stSidebar"]{border-left:1px solid #d9e4dc;background:#0b0e0c}
[data-testid="stSidebar"] *{direction:rtl;text-align:right;color:#f6fff8}
.block-container{max-width:1600px;padding-top:1rem;padding-bottom:2rem}
.hero{background:linear-gradient(135deg,#080b09 0%,#111713 68%,#a6f3b5 180%);border:1px solid #27352b;border-radius:24px;padding:30px 32px;margin-bottom:18px;box-shadow:0 14px 40px rgba(0,0,0,.12)}
.hero h1{color:#fff;margin:6px 0 0;font-size:2.2rem}.hero p{color:#dce8df;line-height:1.9;margin:.7rem 0 0}.tag{display:inline-block;background:#c9ffd5;color:#07150b;border-radius:999px;padding:5px 11px;margin-left:6px;font-size:.76rem;font-weight:850}
.kpi{background:#fff;border:1px solid #dce7df;border-radius:16px;padding:16px 18px;min-height:128px;box-shadow:0 6px 18px rgba(10,30,18,.05)}
.kpi .label{font-size:.82rem;color:#58675e}.kpi .value{font-size:1.46rem;font-weight:850;color:#0c1710;margin:.3rem 0}.kpi .note{font-size:.78rem;color:#6b786f;line-height:1.55}.panel{background:#fff;border:1px solid #dce7df;border-radius:16px;padding:18px 20px;margin:.55rem 0 1rem}.good{border-right:5px solid #61d881;background:#f3fff6}.warn{border-right:5px solid #e5b34f;background:#fffaf0}.risk{border-right:5px solid #db6a6a;background:#fff5f5}.small{font-size:.82rem;color:#657169}.titleline{font-weight:900;font-size:1.1rem;color:#0b1710;margin-bottom:.3rem}.cta{display:inline-block;background:#a6f3b5;color:#07150b;padding:9px 14px;border-radius:10px;font-weight:900}.pill{display:inline-block;border:1px solid #cfe5d4;border-radius:999px;padding:4px 9px;margin:2px;background:#f6fff8}.mono{direction:ltr;text-align:left;font-family:monospace;white-space:pre-wrap;background:#0c120e;color:#dfffea;border-radius:12px;padding:14px}
</style>
""", unsafe_allow_html=True)

markets = pd.DataFrame([
[1,"العراق",92,"Germany Care Adult Diapers","Importer / Pharmacy","Arabic Quick Win","Adult care fragmentation + importer pool","سريع جدًا"],
[2,"ليبيا",90,"Germany Care Adult Diapers","Fast Distributor","Arabic Quick Win","قرب جغرافي + سرعة replenishment","سريع جدًا"],
[3,"أوغندا",89,"Adult Diapers + Underpads","Medical Importer","East Africa Scale","نشاط مستوردين مرتفع + medical channel","سريع"],
[4,"تنزانيا",88,"Adult Diapers + Pants","Value Distributor","East Africa Scale","سوق value-driven ومجال challenger","سريع"],
[5,"المغرب",87,"Adult Diapers + Underpads","Pharmacy / Home Care","Francophone","نمو قوي في adult incontinence + Agadir","متوسط-سريع"],
[6,"غانا",86,"Adult Diapers","Wholesale / Medical","West Africa","قاعدة مشترين جيدة + repeat demand","سريع"],
[7,"كينيا",83,"Adult + Underpads","Healthcare Distributor","East Africa Scale","قناة طبية قوية لكن منافسة أعلى","متوسط"],
[8,"الإمارات",84,"Germany Pants","Pharmacy / E-commerce","GCC High Value","قيمة سوقية جيدة + showcase hub","متوسط"],
[9,"السعودية",82,"Germany Pants","Pharmacy / Home Care","GCC High Value","قوة شرائية عالية لكن منافسة قوية","متوسط"],
[10,"عمان",81,"Pants + Adult","Distributor","GCC High Value","سوق مناسب لموزع واحد قوي","متوسط"],
[11,"قطر",79,"Germany Pants","Premium Value","GCC High Value","سوق صغير لكن قيمة جيدة","متوسط"],
[12,"الكويت",78,"Germany Pants","Pharmacy","GCC High Value","قناة صيدليات واضحة","متوسط"],
[13,"الأردن",76,"Adult Diapers","Pharmacy","Arab Selective","سهولة لغة وقناة صيدليات","متوسط"],
[14,"الكاميرون",75,"Adult Diapers","Value Distributor","Francophone Africa","value-market مناسب","متوسط"],
[15,"رواندا",74,"Adult Diapers","Medical / FMCG","East Africa","حجم أصغر لكن سهولة test","متوسط"],
[16,"زامبيا",73,"Adult + Underpads","Institutional","East/Southern Africa","قناة مؤسسات طبية","متوسط"],
[17,"إثيوبيا",72,"Adult + Underpads","Medical","East Africa","طلب مؤسسي محتمل","متوسط"],
[18,"كوت ديفوار",71,"Adult Diapers","Francophone Distributor","Francophone Africa","قناة موزعين قوية","متوسط"],
[19,"السنغال",70,"Adult Diapers","Francophone Distributor","Francophone Africa","قابلية localization فرنسي","متوسط"],
[20,"البحرين",67,"Germany Pants","Pharmacy","GCC","سوق صغير مرتفع القيمة","متوسط"],
[21,"الجزائر",69,"Pants / Adult","Challenger","North Africa","حجم جيد لكن تركّز تنافسي","أبطأ"],
[22,"جنوب أفريقيا",68,"Germany Pants","Value Challenger","Southern Africa","سوق كبير لكن تنافس وهيكلة قوية","أبطأ"],
[23,"تونس",64,"Germany Pants","Selective","North Africa","تركيز تنافسي مرتفع","أبطأ"],
[24,"لبنان",65,"Adult Diapers","Pharmacy","Levant","قناة صيدليات واضحة","متوسط"],
[25,"نيجيريا",63,"Adult Diapers","Selective Importer","West Africa","TAM كبير لكن FX ومخاطر تشغيل","أبطأ"],
[26,"الكونغو الديمقراطية",62,"Adult Diapers","Wholesale","Central Africa","wholesale opportunity","أبطأ"],
[27,"أنجولا",61,"Adult Diapers","Medical Distributor","Lusophone Africa","فرصة موزع متخصص","أبطأ"],
[28,"جيبوتي",60,"Adult Diapers","Re-export","Red Sea","قرب + re-export","متوسط"],
[29,"موريشيوس",58,"Germany Pants","Premium Niche","Indian Ocean","niche premium-value","أبطأ"],
[30,"زيمبابوي",57,"Adult Diapers","Medical Distribution","Southern Africa","selective opportunity","أبطأ"]
], columns=["Rank","الدولة","Export Score","Hero Product","Entry Channel","Cluster","Why Now","سرعة متوقعة"])

products = pd.DataFrame([
["Germany Care Adult Diapers",1,"Hero Product","Adult Care","العراق، ليبيا، أوغندا، تنزانيا، المغرب، غانا","Reliable protection. Everyday dignity.","Request Distributor Pricing"],
["Germany Pants",2,"Margin / GCC Hero","Active Adult Care","السعودية، الإمارات، عمان، قطر، الكويت، البحرين","Freedom to move. Protection you can trust.","Request Pants Samples"],
["Germany Care Underpads",3,"Institutional Cross-Sell","Hospital / Home Care","المغرب، أوغندا، كينيا، زامبيا، إثيوبيا","Dependable care for clinical and home use.","Request Institutional Pricing"],
["Germany Baby",4,"Portfolio Expansion","Baby Care","العراق، ليبيا، أوغندا، تنزانيا، غانا","Care starts early. Value that travels further.","Build a Mixed Container"],
["Germany Lady Maternity Pads",5,"Pharmacy Cross-Sell","Maternity / Postpartum","الخليج، المغرب، الأردن","Comfort and protection for recovery.","Request Maternity Range"],
["Germany Face Masks",6,"Supporting SKU","Hygiene","انتقائي حسب السوق","Everyday hygiene, dependable protection.","Request Hygiene Catalogue"]
], columns=["Product","Priority","Role","Category","Best Markets","Positioning","CTA"])

entry_plays = pd.DataFrame([
[1,"العراق","Germany Care Adult Diapers","Premium everyday protection without premium-brand pricing.","Importer → Medical distributor → Pharmacy → Home Care","Request Iraq distributor pricing + mixed-container offer."],
[2,"ليبيا","Germany Care Adult Diapers + Underpads","Reliable Egyptian-made care, close to your market and built for fast replenishment.","Importer → Wholesale → Pharmacy / Medical","Get Libya wholesale pricing and fastest shipment schedule."],
[3,"السعودية","Germany Pants","Freedom to move. Protection you can trust.","Pharmacy chains → Home Healthcare → E-commerce","Request Saudi registration pack, samples and distributor margin structure."],
[4,"المغرب","Adult Diapers + Underpads","Protection fiable. Confort quotidien. Valeur accessible.","Pharmacy → Home Care → Medical Distributor","Demandez notre offre distributeur Maroc + échantillons."],
[5,"GCC Cluster","Germany Pants","Discreet protection for active everyday living.","Pharmacy → E-commerce → Home Care","Request GCC distributor pricing + pull-up sample kit."],
[6,"East Africa","Adult Diapers + Underpads","Dependable care. Competitive landed economics. Built for repeat demand.","Medical importer → Hospital → Pharmacy","Send monthly volume and destination port for a quote."],
[7,"Portfolio Play","Adult + Baby + Pants + Underpads","One supplier. Multiple high-repeat hygiene categories. Better container economics.","National Distributor → Multi-channel","Build your mixed GERMANY container."]
], columns=["#","Market Entry Play","Hero Offer","Positioning","Channel","CTA"])

keywords = {
"Core Product Keywords": ["adult diapers","adult incontinence diapers","incontinence briefs","adult pull up pants","adult diaper pants","underpads","disposable underpads","maternity pads","continence care products","elderly care products"],
"Buyer Keywords": ["importer","direct importer","major importer","leading importer","bulk importer","distributor","exclusive distributor","national distributor","medical distributor","healthcare distributor","pharmacy supplier","hospital supplier","medical wholesaler"],
"Competitor Discovery": ["TENA distributor [COUNTRY]","Seni distributor [COUNTRY]","Lifree distributor [COUNTRY]","Abena distributor [COUNTRY]","MoliCare distributor [COUNTRY]"],
"Decision Makers": ["Owner","Managing Director","Import Manager","Procurement Manager","Purchasing Manager","Commercial Director","Category Manager - Hygiene","Business Development Manager"]
}

queries = [
'"adult diapers" importer [COUNTRY]',
'"adult diapers" distributor [COUNTRY]',
'"adult incontinence products" distributor [COUNTRY]',
'"adult diaper pants" importer [COUNTRY]',
'"underpads" importer [COUNTRY]',
'"medical disposables" importer [COUNTRY]',
'"hospital supplies" distributor [COUNTRY]',
'"home healthcare" distributor [COUNTRY]',
'"pharmacy wholesaler" [COUNTRY]',
'"elderly care products" distributor [COUNTRY]',
'"adult diapers" buyer consignee [COUNTRY]',
'"TENA" distributor [COUNTRY]',
'"Seni" distributor [COUNTRY]'
]

email_campaign = [
("01 — Commercial Hook","A stronger adult-care opportunity for [Country]?","One care portfolio. Multiple repeat-demand categories.","GERMANY is a multi-category care range from NEGPI covering adult diapers, pull-up pants, underpads, baby care and maternity care. We are evaluating distribution partners in [Country]. Instead of a generic catalogue, we can prepare a commercial offer around your market, channel and destination port.","Reply PRICE for distributor pricing."),
("02 — Positioning","Not another low-cost diaper brand","Reliable protection. Everyday comfort. Complete care.","GERMANY is positioned between expensive global brands and inconsistent low-cost alternatives. Adult Care. Pants. Underpads. Baby Care. Maternity Care. One supplier, multiple repeat-demand categories.","Want the export catalogue and price range?"),
("03 — Economics","What would GERMANY cost landed in [Port]?","Let’s compare economics, not just FOB price.","Share your destination port and approximate monthly volume and we can prepare an indicative commercial structure for the most relevant GERMANY SKUs, including mixed-category loading where useful.","Send your port + monthly volume."),
("04 — Portfolio","One supplier. Five care categories.","Increase revenue from the same distribution network.","Adult Diapers, Pull-Up Pants, Underpads, Baby Care and Maternity Care can all be sold through overlapping pharmacy, medical and wholesale channels.","Build your GERMANY assortment."),
("05 — Competitor Switch","Compare GERMANY with your current supplier","Quality, portfolio, MOQ and commercial value.","If you already represent an adult-care brand, send one current SKU, pack format or target price segment and we can prepare a GERMANY comparison.","Send one SKU to benchmark."),
("06 — Trial","Test first. Scale second.","Evaluate GERMANY before discussing bigger volume.","A new care supplier should prove the product before asking for scale. We can start with product evaluation and then structure a market-fit offer.","Request your evaluation pack."),
("07 — Conversion","Should we reserve [Country] for further discussion?","Closing our current GERMANY distributor shortlist.","If adult diapers, pants or underpads are relevant to your business, choose the next step directly.","Reply PRICE, SAMPLE or CALL.")
]

swot = {
"Strengths":["Multi-category portfolio across adult, baby, underpads, maternity and hygiene","Egyptian manufacturing base with export orientation","Ability to serve pharmacy, medical, wholesale and home-care channels","Potential mixed-container economics and account expansion","Quality/accessibility positioning supports value markets"],
"Weaknesses":["Brand architecture can be confusing without a clear master-brand story","Export-facing commercial assets need sharper MOQ, lead-time, loading and pricing structure","Public proof for performance claims should be stronger and more standardized","Name GERMANY requires clear country-of-origin communication"],
"Opportunities":["Adult care growth in selected MENA/Africa markets","Importer acquisition via trade-data + category-specific outreach","Cross-sell from Adult Diapers into Pants and Underpads","OEM/private-label layer to improve capacity utilization","Regional clusters reduce localization and sales-cost duplication"],
"Threats":["Strong incumbents such as TENA, Fine, Lifree, Seni, Abena and regional players","FX, freight and raw-material volatility","Distributor concentration and exclusivity risk","Regulatory and claims compliance differences by market","Long cash cycles if payment terms are poorly controlled"]
}

st.sidebar.title("GERMANY Export Command Center")
section = st.sidebar.radio("اختر القسم", ["Executive Overview","Brand & Positioning","Products","Top 30 Markets","7 Entry Plays","SWOT","Importer Research","Keyword Engine","Email Campaign","90-Day Plan","Economics & KPIs","Sources & Notes"])

st.markdown("""
<div class="hero">
<span class="tag">NEGPI</span><span class="tag">GERMANY</span><span class="tag">Export Growth</span>
<h1>GERMANY — International Export Growth Study</h1>
<p><b>Care for Every Stage.</b><br>تحويل GERMANY من منتج حفاضات كبار سن إلى Care & Hygiene Portfolio قابل للتوسع دوليًا عبر Adult Care, Pants, Underpads, Baby Care, Maternity Care وHygiene.</p>
</div>
""", unsafe_allow_html=True)

if section == "Executive Overview":
    c1,c2,c3,c4 = st.columns(4)
    cards=[("Hero Product","Germany Care Adult Diapers","أقوى مدخل أولي لمعظم أسواق MENA/Africa"),("Second Growth Engine","Germany Pants","أفضل fit للخليج والـactive adult segment"),("Fastest Cluster","Iraq + Libya","أعلى أولوية للـquick-win export"),("North Star","First Reorder","الـPO الأول اختبار؛ إعادة الطلب دليل fit")]
    for col,(lab,val,note) in zip([c1,c2,c3,c4],cards): col.markdown(f'<div class="kpi"><div class="label">{lab}</div><div class="value">{val}</div><div class="note">{note}</div></div>',unsafe_allow_html=True)
    st.subheader("الخلاصة الاستراتيجية")
    st.markdown("""
<div class='panel good'><div class='titleline'>GERMANY = Care Portfolio, not a single-SKU diaper brand</div>
الاستراتيجية الأقوى هي الدخول بمنتج بطل واضح، ثم توسيع الحساب نفسه إلى Pants وUnderpads ثم Baby/Maternity. القيمة للموزع ليست مجرد امتصاص أعلى؛ بل <b>More Categories + Repeat Demand + One Supplier + Better Container Economics</b>.</div>
<div class='panel'><b>Master Positioning:</b> Care for Every Stage.<br><b>Export Positioning:</b> Care for Every Stage. Built for Every Market.<br><b>Core Message:</b> Reliable protection. Everyday comfort. Complete care.<br><b>B2B Message:</b> One trusted care portfolio. More categories. More repeat sales.<br><b>Primary CTA:</b> Bring GERMANY to Your Market. — Request Distributor Pricing.</div>
""",unsafe_allow_html=True)
    st.subheader("أعلى 10 أسواق")
    st.dataframe(markets.head(10), use_container_width=True, hide_index=True)
    fig=px.bar(markets.head(15).sort_values("Export Score"),x="Export Score",y="الدولة",orientation="h",text="Export Score",title="Top 15 Export Opportunity Scores")
    st.plotly_chart(fig,use_container_width=True)

elif section == "Brand & Positioning":
    st.subheader("Brand Platform")
    st.markdown("""
<div class='panel good'><h2>GERMANY</h2><h3>Care for Every Stage.</h3><p><b>Reliable protection. Everyday comfort. Complete care.</b></p>
<p>Baby Care • Adult Care • Pants • Underpads • Maternity Care • Hygiene</p><span class='cta'>Bring GERMANY to Your Market.</span><p class='small'>Manufactured in Egypt by NEGPI.</p></div>
""",unsafe_allow_html=True)
    st.markdown("""
<div class='panel'><b>Commercial Reframe</b><br>بدل “we manufacture adult diapers”، الرسالة المقترحة: <b>GERMANY is a multi-category care portfolio designed to give distributors reliable quality, repeat-demand products and stronger category expansion from one manufacturing partner.</b></div>
<div class='panel warn'><b>Country-of-origin discipline</b><br>اسم GERMANY يجب ألا يُستخدم بما يوحي أن المنتج ألماني المنشأ إذا لم يكن كذلك. اجعل <b>Manufactured in Egypt by NEGPI</b> واضحًا في المواد التجارية والتصديرية.</div>
""",unsafe_allow_html=True)

elif section == "Products":
    st.subheader("Product Portfolio & Role")
    st.dataframe(products,use_container_width=True,hide_index=True)
    st.subheader("ترتيب التوسع")
    fig=px.bar(products.sort_values("Priority",ascending=False),x="Priority",y="Product",orientation="h",title="Product Priority")
    st.plotly_chart(fig,use_container_width=True)

elif section == "Top 30 Markets":
    st.subheader("Top 30 Priority Markets")
    cluster=st.multiselect("فلتر Cluster",sorted(markets["Cluster"].unique()),default=[])
    data=markets if not cluster else markets[markets["Cluster"].isin(cluster)]
    st.dataframe(data,use_container_width=True,hide_index=True)
    fig=px.scatter(data,x="Rank",y="Export Score",size="Export Score",color="Cluster",hover_name="الدولة",hover_data=["Hero Product","Entry Channel","Why Now"],title="Market Priority Map")
    st.plotly_chart(fig,use_container_width=True)
    st.caption("Export Score هو نموذج أولوية داخلي للدراسة، وليس ضمانًا أو نسبة ربح فعلية.")

elif section == "7 Entry Plays":
    st.subheader("أقوى 7 نقاط دخول")
    st.dataframe(entry_plays,use_container_width=True,hide_index=True)
    for _,r in entry_plays.iterrows():
        st.markdown(f"<div class='panel'><b>#{r['#']} — {r['Market Entry Play']}</b><br><b>Hero:</b> {r['Hero Offer']}<br><b>Positioning:</b> {r['Positioning']}<br><b>Channel:</b> {r['Channel']}<br><b>CTA:</b> {r['CTA']}</div>",unsafe_allow_html=True)

elif section == "SWOT":
    st.subheader("SWOT Analysis")
    a,b=st.columns(2)
    for i,(k,v) in enumerate(swot.items()):
        col=a if i%2==0 else b
        cls='good' if k in ['Strengths','Opportunities'] else 'warn' if k=='Weaknesses' else 'risk'
        col.markdown(f"<div class='panel {cls}'><b>{k}</b><br>"+"<br>".join([f"• {x}" for x in v])+"</div>",unsafe_allow_html=True)

elif section == "Importer Research":
    st.subheader("1,000 Target Accounts Architecture")
    pools=pd.DataFrame([["Confirmed/Likely Adult Diaper Importers",300],["Medical/Hospital Distributors",200],["Pharmacy/FMCG Distributors",175],["Home Care/Underpads/Nursing Suppliers",175],["Competitor-category Distributors",150]],columns=["Pool","Target Accounts"])
    st.dataframe(pools,use_container_width=True,hide_index=True)
    fig=px.pie(pools,values="Target Accounts",names="Pool",hole=.45,title="Lead Pool Mix")
    st.plotly_chart(fig,use_container_width=True)
    st.markdown("""
<div class='panel'><b>Lead Scoring — 100 points</b><br>Recent import activity 30 • Adult-care fit 20 • Shipment frequency 15 • Distribution network 10 • Pharmacy/medical reach 10 • Multi-category fit 5 • Company scale 5 • Decision maker identified 5.</div>
<div class='panel good'><b>80–100 = Golden Account</b><br>65–79 = Priority • 50–64 = Nurture • أقل من 50 = لا يستهلك وقت Export Manager.</div>
""",unsafe_allow_html=True)

elif section == "Keyword Engine":
    st.subheader("Keyword Bank")
    for k,v in keywords.items():
        st.markdown(f"<div class='panel'><b>{k}</b><br>"+" ".join([f"<span class='pill'>{x}</span>" for x in v])+"</div>",unsafe_allow_html=True)
    st.subheader("Golden Search Queries")
    st.code("\n".join(queries),language="text")
    st.markdown("""
<div class='panel good'><b>Search Formula</b><br>PRODUCT + importer → PRODUCT + distributor → COMPETITOR + distributor → PRODUCT + buyer/consignee → medical supplies + PRODUCT.</div>
""",unsafe_allow_html=True)

elif section == "Email Campaign":
    st.subheader("7-Email Export Campaign")
    for n,sub,prev,body,cta in email_campaign:
        with st.expander(f"{n} — {sub}"):
            st.markdown(f"**Subject:** {sub}\n\n**Preview:** {prev}\n\n{body}\n\n**CTA:** {cta}")
    st.markdown("""
<div class='panel good'><b>Email Footer System</b><br><b>GERMANY — Care for Every Stage.</b><br>Adult Care | Pants | Underpads | Baby Care | Maternity Care<br><b>Bring GERMANY to Your Market.</b><br>Manufactured by NEGPI — Egypt.</div>
""",unsafe_allow_html=True)

elif section == "90-Day Plan":
    plan=pd.DataFrame([
["Days 1–10","Export Weaponisation","Positioning, price matrix, MOQ, loading, certificates, technical sheets, samples, country decks"],
["Days 11–25","Build 1,000 Accounts","Importers, medical distributors, competitor channels, decision makers, scoring"],
["Days 26–40","Campaign Blitz","Tier A personalization, Tier B semi-personalized, subject/CTA testing, fast reply handling"],
["Days 41–60","Sales Conversion","RFQs, samples, calls, comparisons, credit checks, pilot PO"],
["Days 61–75","Market Launch Prep","Distributor materials, local language, pharmacy/hospital listing, launch support"],
["Days 76–90","Reorder System","Sell-through, inventory days, active doors, DSO, contribution margin, repeat order"]
],columns=["Timing","Phase","Execution"])
    st.dataframe(plan,use_container_width=True,hide_index=True)
    st.markdown("""
<div class='panel good'><b>90-Day Target</b><br>2–5 active distributor agreements • 1–3 initial export shipments • 5–12 late-stage RFQs • 15–30 qualified opportunities • 1+ repeat order.</div>
<div class='panel'><b>72-Hour Objective</b><br>الهدف الواقعي من أول 1,000 حساب هو RFQ Momentum وليس ضمان شحنة خلال 3 أيام. أي PO أو Deposit سريع يُعامل كـoutperformance.</div>
""",unsafe_allow_html=True)

elif section == "Economics & KPIs":
    st.subheader("Export Economics Framework")
    st.markdown("""
<div class='panel'><b>NEGPI Contribution Margin</b><br>Selling Price − Manufacturing Cost − Export Packaging − Rebates − Marketing Support − Sales Commission − Finance/Credit Cost.</div>
<div class='panel'><b>Distributor Economics</b><br>FOB/CIF + Duty + Logistics + Storage = Landed Cost → Distributor Sell-in → Distributor GP → Retail Price → Retailer GP.</div>
<div class='panel good'><b>Commercial rule</b><br>لا تبِع على أساس Lowest FOB فقط. بع على أساس <b>Distributor Gross Profit per Container + Repeat Demand + Portfolio Expansion</b>.</div>
""",unsafe_allow_html=True)
    kpis=pd.DataFrame([["North Star","First Reorder"],["Pipeline","Qualified Accounts → RFQs → Samples → Negotiations → POs"],["Revenue","FOB Revenue + Contribution Margin"],["Distribution","Active Doors + Sell-through"],["Cash","DSO + Payment Discipline"],["Inventory","Inventory Rotation / Days"]],columns=["KPI Layer","Measure"])
    st.dataframe(kpis,use_container_width=True,hide_index=True)

elif section == "Sources & Notes":
    st.subheader("Study Basis")
    st.markdown("""
<div class='panel'>الدراسة مبنية على ملف NEGPI المرفوع، وعلى التطوير الاستراتيجي الذي تم في هذه المحادثة حول GERMANY، منتجاته، الـpositioning، الأسواق، الـGTM، الـemail campaign والـkeyword framework. أي أرقام سوقية أو أسماء مستوردين أو قواعد تجارة يجب تحديثها دوريًا قبل اتخاذ قرار تجاري نهائي.</div>
<div class='panel warn'><b>Important:</b> Market scores, sales velocity labels and 90-day outcomes are strategic planning assumptions, وليست ضمانات مبيعات أو أرباح.</div>
""",unsafe_allow_html=True)
