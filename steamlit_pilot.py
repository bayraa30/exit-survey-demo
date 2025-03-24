import streamlit as st

# Page setup
st.set_page_config(page_title="Ажлаас Гарах Үеийн Асуулга", layout="wide")
st.image("https://i.imgur.com/uKIN0Fd.png", width=150)  # Replace with your logo

# Session state init
if "page" not in st.session_state:
    st.session_state.page = 0

#Show progress bar at the top
total_questions = 10
progress = st.progress(st.session_state.page / total_questions)


# Intro Page
if st.session_state.page == 0:
    st.title("Ажлаас Гарах Үеийн Асуулга")
    st.markdown("Сайн байна уу!")
    st.markdown(
        "Таны өгч буй үнэлгээ, санал хүсэлт нь бидний цаашдын хөгжлийг тодорхойлоход чухал үүрэгтэй тул "
        "дараах асуултад үнэн зөв, чин сэтгэлээсээ хариулна уу."
    )

    if st.button("Асуулга Эхлэх"):
        st.session_state.page = 1

elif st.session_state.page == 1:
    st.header("1) Ажлын байрны тодорхойлолт таны өдөр тутмын ажил үүрэгтэй нийцэж байсан уу?")
    st.markdown("Слайдер ашиглан өөрийн үнэлгээг өгнө үү.")

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.image("https://i.imgur.com/5HDu5mQ.png", caption="Нийцээгүй", use_container_width=True)

    with col3:
        st.image("https://i.imgur.com/Slnlc7w.png", caption="Төгс нийцсэн", use_container_width=True)

    with col2:
        slider_value_q1 = st.slider(
            "Өөрийн үнэлгээг сонгоно уу:",
            min_value=1,
            max_value=5,
            step=1,
            value=1,
            key="slider_q1"  # ✅ unique key for question 1
        )
        st.write(f"Таны сонгосон үнэлгээ: {slider_value_q1}")

    if st.button("Дараагийн асуулт руу шилжих"):
        st.session_state.answer1 = slider_value_q1
        st.session_state.page += 1


elif st.session_state.page == 2:
    st.header("Ажилд орсон анхны өдөр таны хүлээлтэд хүрч чадсан уу?")
    st.markdown("Слайдер ашиглан өөрийн үнэлгээг өгнө үү.")

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.image("https://i.imgur.com/YjXuQ3Z.png", caption="Хүлээлтэд хүрээгүй", use_container_width=True)

    with col3:
        st.image("https://i.imgur.com/9FFoFJI.png", caption="Хүлээлтээс давсан", use_container_width=True)

    with col2:
        # Only read the slider value — don't store in session state yet
        slider_value_q2 = st.slider(
            "Өөрийн үнэлгээг сонгоно уу:",
            min_value=1,
            max_value=5,
            step=1,
            value=1,
            key="slider_q2"
        )
        st.write(f"Таны сонгосон үнэлгээ: {slider_value_q2}")

    # ✅ Only update session state when button is clicked
    if st.button("Дараагийн асуулт руу шилжих", key="btn_q2"):
        st.session_state.answer2 = slider_value_q2
        st.session_state.page += 1


# Thir question with images 
elif st.session_state.page == 3:
    st.header("Ажлын процесс, үүрэг даалгаврыг хурдан ойлгоход тань Дасан зохицох хөтөлбөр болон баг хамт олон хангалттай мэдээлэл, заавар өгч чадсан уу?")
    st.markdown("Доорх сонголтуудаас өөрийн хариултыг сонгоно уу.")

    # Three-column layout for the images and choices
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://i.imgur.com/HgAdV0l.png", use_container_width=True)  # Replace with actual image
        if st.button("🔴 Хангалтгүй"):
            st.session_state.answer3 = "Хангалтгүй"
            st.session_state.page += 1

    with col2:
        st.image("https://i.imgur.com/ozPjQjD.png", use_container_width=True)  # Replace with actual image
        if st.button("🟡 Дунд зэрэг"):
            st.session_state.answer3 = "Дунд зэрэг"
            st.session_state.page += 1

    with col3:
        st.image("https://i.imgur.com/dePXr8c.png", use_container_width=True)  # Replace with actual image
        if st.button("🟢 Хангалттай"):
            st.session_state.answer3 = "Хангалттай"
            st.session_state.page += 1

# Fourth Question with Slider and Images
elif st.session_state.page == 4:
    st.header("Таныг ажилд нь чиглүүлж байсан Buddy хангалттай тусалж, дэмжлэг үзүүлж чадсан уу?")
    st.markdown("Слайдер ашиглан өөрийн үнэлгээг өгнө үү.")

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.image("https://i.imgur.com/dFqvw4o.png", caption="Би өөрөө өөртөө buddy байсан", use_container_width=True)  # Replace with actual left image URL

    with col3:
        st.image("https://i.imgur.com/XaIyoRi.png", caption="Маш сайн дэмжиж ажилласан", use_container_width=True)  # Replace with actual right image URL

    with col2:
        slider_value_q2 = st.slider(
            "Өөрийн үнэлгээг сонгоно уу:",
            min_value=1,
            max_value=5,
            step=1,
            format="%d"
        )
        st.write(f"Таны сонгосон үнэлгээ: {slider_value_q2}")

        if st.button("Дараагийн асуулт руу шилжих"):
            st.session_state.answer2 = slider_value_q2
            st.session_state.page += 1

#Fifth open ended questtion
elif st.session_state.page == 5:
    st.header("Та ажлын байрны соёл, багийн уур амьсгалыг өөрчлөх, сайжруулах талаарх саналаа бичнэ үү?")
    st.markdown("Доорх талбарт хариултаа бичнэ үү:")

    response = st.text_area("Хариулт:", height=200)

    if st.button("Дараагийн асуулт руу шилжих"):
        st.session_state.answer4 = response
        st.session_state.page += 1

#Sixth question with four images
elif st.session_state.page == 6:
    st.header("Таны шууд удирдлага ихэвчлэн ямар зан төлөв гаргадаг байсан бэ?")
    st.markdown("Зургуудын доорх тайлбараас сонгон хариулна уу:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("https://i.imgur.com/Fa0OMaa.png", use_container_width=True)
        if st.button("Уурлаж бухимдсан", key="btn_angry"):
            st.session_state.answer6 = "Уурлаж бухимдсан"
            st.session_state.page += 1

    with col2:
        st.image("https://i.imgur.com/QzsvVzv.png", use_container_width=True)
        if st.button("Ажил хэрэгч, дайчин", key="btn_direct"):
            st.session_state.answer6 = "Ажил хэрэгч, дайчин"
            st.session_state.page += 1

    with col3:
        st.image("https://i.imgur.com/pE5obqG.png", use_container_width=True)
        if st.button("Урам зоригтой, найрсаг", key="btn_friendly"):
            st.session_state.answer6 = "Урам зоригтой, найрсаг"
            st.session_state.page += 1

    with col4:
        st.image("https://i.imgur.com/MZ1H7Wt.png", use_container_width=True)
        if st.button("Идэвхгүй, гутарсан", key="btn_passive"):
            st.session_state.answer6 = "Идэвхгүй, гутарсан"
            st.session_state.page += 1

# Seventh Question with Slider and Images
elif st.session_state.page == 7:
    st.header("Та баг доторх хамтын ажиллагаа болон ажилтан хоорондын харилцаанд хэр сэтгэл хангалуун байсан бэ?")
    st.markdown("Слайдер ашиглан өөрийн үнэлгээг өгнө үү.")

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.image("https://i.imgur.com/s01gjXu.png", caption="Эсрэгээрээ хэцүү байсан", use_container_width=True)  # Replace with actual left image URL

    with col3:
        st.image("https://i.imgur.com/RaVIyD7.png", caption=" Маш их сэтгэл хангалуун байсан. ", use_container_width=True)  # Replace with actual right image URL

    with col2:
        slider_value_q2 = st.slider(
            "Өөрийн үнэлгээг сонгоно уу:",
            min_value=1,
            max_value=5,
            step=1,
            format="%d"
        )
        st.write(f"Таны сонгосон үнэлгээ: {slider_value_q2}")

        if st.button("Дараагийн асуулт руу шилжих"):
            st.session_state.answer2 = slider_value_q2
            st.session_state.page += 1

#Eight open ended questtion
elif st.session_state.page == 8:
    st.header("Танд өдөр тутмын ажлаа урам зоригтой хийхэд ямар ямар хүчин зүйлс нөлөөлдөг байсан бэ?")
    st.markdown("Доорх талбарт хариултаа бичнэ үү:")

    response = st.text_area("Хариулт:", height=200)

    if st.button("Дараагийн асуулт руу шилжих"):
        st.session_state.answer4 = response
        st.session_state.page += 1

# Ninth Question with Slider and Images
elif st.session_state.page == 9:
    st.header("Таны ажлын гүйцэтгэлийг үнэлэх (KPI) үзүүлэлтүүд хариуцан ажиллаж байсан  ажил үүрэгтэй уялдаж нийцэж байсан уу?")
    st.markdown("Слайдер ашиглан өөрийн үнэлгээг өгнө үү.")

    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.image("https://i.imgur.com/nfT6Lsc.png", caption="Зарим талаараа л нийцдэггүй байсан", use_container_width=True)
    with col3:
        st.image("https://i.imgur.com/lm76zZ9.png", caption="100% нийцэж байсан", use_container_width=True)

    with col2:
        slider_value_q9 = st.slider(
            "Өөрийн үнэлгээг сонгоно уу:",
            min_value=1,
            max_value=5,
            step=1,
            value=1,
            key="slider_q9"
        )
        st.write(f"Таны сонгосон үнэлгээ: {slider_value_q9}")

    if st.button("Дараагийн асуулт руу шилжих", key="btn_q9"):
        st.session_state.answer9 = slider_value_q9
        st.session_state.page += 1



#Tenth question with slider and image, finishing remark
elif st.session_state.page == 10:
    st.header("Компанидаа ажил, мэргэжлийн хувьд өсөж, хөгжих боломжтой санагдсан уу?")
    st.markdown("Слайдер ашиглан өөрийн үнэлгээг өгнө үү.")

    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.image("https://i.imgur.com/tmFDnpf.png", caption="Өсөж хөгжих боломж байгаагүй", use_container_width=True)
    with col3:
        st.image("https://i.imgur.com/XcAr6kR.png", caption="Маш их боломжууд байдаг", use_container_width=True)

    with col2:
        final_rating = st.slider(
            "Өөрийн үнэлгээг сонгоно уу:",
            min_value=1,
            max_value=5,
            step=1,
            value=1,
            key="slider_q10"
        )
        st.write(f"Таны сонгосон үнэлгээ: {final_rating}")

    if st.button("Судалгааг дуусгах", key="btn_q10"):
        st.session_state.final_rating = final_rating
        st.success("🎉 Баярлалаа! Таны хариултыг амжилттай хүлээн авлаа.")
        st.balloons()







