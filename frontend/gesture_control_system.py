import streamlit as st
import cv2
import subprocess
import sys

st.title("Gesture Control System")
with open("gesture_control_system.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

# sidebar design
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width:350px
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width:350px
        margin-left: -350px
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title('Gesture Control System')
st.sidebar.subheader("Available Modules")


@st.cache()
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = width / float(w)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    return resized


app_mode = st.sidebar.selectbox('Choose the App module',
                                ['About App', 'Volume control system',
                                 'Virtual calculator', 'Drag and Drop',
                                 'Zoom-in and Zoom-out'])
if app_mode == 'About App':
    st.markdown("""In this app we are providing human-machine Interaction(HMI)
    or man machine interaction(MMI). We had provided the facillity of volume control,
    virtual calculator, drag and drop demonstrate and zoom in and zoom out """)
    st.header("Member List")
    list1 = ["Abhinav gupta", "Abhishek garg", "Anshika kumari", "Ayush kumar verma"]
    list2 = ["2100270140001", "2100270140002", "2100270140010", "2100270140016"]
    load = st.button('Member Info')
    if load:
        for i in range(0, 4):
            st.write(list1[i] + " " + list2[i])
        # st.write(list1[0] + "   " + list2[0])
        # st.image(Image.open('D:\\abhinav photos\\majorProjectUi\\'),width=100)
        # st.write(list1[1] + "   " + list2[1])
        # st.image(Image.open('D:\\abhinav photos\\majorProjectUi\\'),width=100)
        # st.write(list1[2] + "   " + list2[2])
        # st.image(Image.open('D:\\abhinav photos\\majorProjectUi\\'),width=100)
        # st.write(list1[3] + "   " + list2[3])
        # st.image(Image.open('D:\\abhinav photos\\majorProjectUi\\'),width=100)
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
            width:350px
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
            width:350px
            margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
elif app_mode == 'Volume control system':
    st.success("volume control open successfully")
    subprocess.run([f"{sys.executable}", "D:\\abhinav photos\\majorProjectUi\\VolumeHandControl.py"])

elif app_mode == 'Virtual calculator':
    st.success("Here's your virtual calculator")
    subprocess.run([f"{sys.executable}", "D:\\abhinav photos\\majorProjectUi\\main.py"])

elif app_mode == 'Drag and Drop':
    st.success("come on just select and drop your box")
    subprocess.run([f"{sys.executable}", "D:\\abhinav photos\\majorProjectUi\\DragAndDrop.py"])


elif app_mode == 'Zoom-in and Zoom-out':
    st.success("oh you see it is zoomed in or zoomed out")
    subprocess.run([f"{sys.executable}", "D:\\abhinav photos\\majorProjectUi\\zoom_module.py"])
