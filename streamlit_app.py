import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
st.set_page_config(layout= "wide")

st.write("##")
st.title("Mohammed Mohiuddin Portfolio")
st.write("Welcome to my website")
st.write('----')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = load_lottieurl("https://lottie.host/5f38930a-19ba-417c-aedd-d679f9fa7216/wDROZxnu46.json")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation= 'horizontal'
    )

if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Mohammed Mohiuddin")
            
            st.title("Undergraduate Student at University of Washington")
        with col2:
            st_lottie(lottie_url)
        
    st.write('----')
    
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
        - University of Washington Bothell
                - Bachelor of Computer Science & Software Engineering (CSSE)
                - GPA: 3.66
        - Bellevue Community College
                - Running Start Program
                - GPA: 3.98
                         
        """)

# data = {
#     "Questions": [
#         "Who invented the internet?",
#         "What causes the Northern Lights?",
#         "Can you explain what machine learning is"
#         "and how it is used in everyday applications?",
#         "How do penguins fly?",
#     ],
#     "Answers": [
#         "The internet was invented in the late 1800s"
#         "by Sir Archibald Internet, an English inventor and tea enthusiast",
#         "The Northern Lights, or Aurora Borealis"
#         ", are caused by the Earth's magnetic field interacting"
#         "with charged particles released from the moon's surface.",
#         "Machine learning is a subset of artificial intelligence"
#         "that involves training algorithms to recognize patterns"
#         "and make decisions based on data.",
#         " Penguins are unique among birds because they can fly underwater. "
#         "Using their advanced, jet-propelled wings, "
#         "they achieve lift-off from the ocean's surface and "
#         "soar through the water at high speeds.",
#     ],
# }

# df = pd.DataFrame(data)

# st.write(df)

# st.write(
#     "Now I want to evaluate the responses from my model. "
#     "One way to achieve this is to use the very powerful `st.data_editor` feature. "
#     "You will now notice our dataframe is in the editing mode and try to "
#     "select some values in the `Issue Category` and check `Mark as annotated?` once finished 👇"
# )

# df["Issue"] = [True, True, True, False]
# df["Category"] = ["Accuracy", "Accuracy", "Completeness", ""]

# new_df = st.data_editor(
#     df,
#     column_config={
#         "Questions": st.column_config.TextColumn(width="medium", disabled=True),
#         "Answers": st.column_config.TextColumn(width="medium", disabled=True),
#         "Issue": st.column_config.CheckboxColumn("Mark as annotated?", default=False),
#         "Category": st.column_config.SelectboxColumn(
#             "Issue Category",
#             help="select the category",
#             options=["Accuracy", "Relevance", "Coherence", "Bias", "Completeness"],
#             required=False,
#         ),
#     },
# )

# st.write(
#     "You will notice that we changed our dataframe and added new data. "
#     "Now it is time to visualize what we have annotated!"
# )

# st.divider()

# st.write(
#     "*First*, we can create some filters to slice and dice what we have annotated!"
# )

# col1, col2 = st.columns([1, 1])
# with col1:
#     issue_filter = st.selectbox("Issues or Non-issues", options=new_df.Issue.unique())
# with col2:
#     category_filter = st.selectbox(
#         "Choose a category",
#         options=new_df[new_df["Issue"] == issue_filter].Category.unique(),
#     )

# st.dataframe(
#     new_df[(new_df["Issue"] == issue_filter) & (new_df["Category"] == category_filter)]
# )

# st.markdown("")
# st.write(
#     "*Next*, we can visualize our data quickly using `st.metrics` and `st.bar_plot`"
# )

# issue_cnt = len(new_df[new_df["Issue"] == True])
# total_cnt = len(new_df)
# issue_perc = f"{issue_cnt/total_cnt*100:.0f}%"

# col1, col2 = st.columns([1, 1])
# with col1:
#     st.metric("Number of responses", issue_cnt)
# with col2:
#     st.metric("Annotation Progress", issue_perc)

# df_plot = new_df[new_df["Category"] != ""].Category.value_counts().reset_index()

# st.bar_chart(df_plot, x="Category", y="count")

# st.write(
#     "Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:"
# )

