import streamlit as st


st.image("logo_petit_noir.png", width=150)

# CSS personnalisé
st.markdown(
    """
    <style>


    /* Masquer complètement le bandeau si nécessaire */
    header {
        visibility: hidden;
    }
    header > div {
        display: none;
    }



    /* Personnaliser les autres éléments si nécessaire */
    /* Applique le style pour centrer le texte globalement */
        .center-text {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            text-align: center;
            font-size: 20px;
        }

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');
   

    </style>
    """,
    unsafe_allow_html=True
)

st.header("Les zones d'entrainement")

st.text(" Les zones d'entrainement sont calculées sur la base de la fréquence cardiaque au repos et de la fréquence cardiaque maximale.")

st.text("La fréquence cardiaque maximale est obtenue en réalisant un test à intensité maximale en côte durant 6 minutes. Par défaut, la FC de repos la plus haute à ce jour peut être prise.")

st.text("La fréquence cardiaque de repos se mesure le matin au réveil. Par défaut, la FC de repos la plus basse à ce jour peut être prise")

st.text("Les zones d'entrainement sont basées sur la fréquence cardiaque de réserve. C'est la différentre entre la fréquence cardiaque maximale et la fréquence cardiaque de repos.")

st.text("La Fréquence cardiaque maximale est personnelle et ne peut pas être estimée par des formules générales telles que 220 - âge.")


st.divider()

fc_max = st.number_input("Fréquence cardiaque maximale", min_value=0, max_value=300, value=0, step=1)
fc_rest = st.number_input("Fréquence cardiaque au repos", min_value=0, max_value=300, value=0, step=1)

st.divider()

zone1_max = round(fc_rest + 0.6 * (fc_max - fc_rest))
zone2_max = round(fc_rest + 0.7 * (fc_max - fc_rest))
zone3_max = round(fc_rest + 0.8 * (fc_max - fc_rest))
zone4_max = round(fc_rest + 0.9 * (fc_max - fc_rest))

st.subheader("Zones 1")
st.write(f"{0} - {zone1_max}")

st.subheader("Zones 2")
st.write(f"{zone1_max} - {zone2_max}")

st.subheader("Zones 3")
st.write(f"{zone2_max} - {zone3_max}")

st.subheader("Zones 4")
st.write(f"{zone3_max} - {zone4_max}")

st.subheader("Zones 5")
st.write(f"{zone4_max} - {fc_max}")




                            

    
   

    