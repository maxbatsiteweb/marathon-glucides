import streamlit as st
import math
import datetime

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

st.header("Protocole nutrition sur marahton")

st.text("La consommation de glucides est primordial pour soutenir un effort sur les 42 Km")

st.text("C'est une condition nécessaire (pas suffisante) pour éviter de 'prendre le mur' du 30ème kilomètre.")

st.text("Les dernières recherches en la matière montrent que c'est l'un des pilliers de la durabilité.")

st.text("La durabilité est la capacité à minimiser la dégradation de caractéristiques physiologiques durant un effort long (VO2Max, seuils, force maximale, économie de course notamment)")



st.text("Vous retrouverez ici un article d'Endurance 142 quant à l'importances des glucides pour les efforts longs.")

st.divider()


time_input = st.time_input("Temps cible (HH:MM:SS)", value=datetime.time(3, 30, 0), step=60)
time = time_input.hour * 3600 + time_input.minute * 60 + time_input.second

st.divider()

st.text("La science préconise des apports de glucides allant de 50g/h à 100g/h")

st.text("Pour les coureurs visant un marathon entre 4h00 et 3h00, 60g/h est une bonne base.")

st.text("Pour les coureurs visant 3h et moins, 90h/h est recommandé")

gram_gels = st.number_input("Grammes de glucides dans le gel (25g par défaut)", 25)

if time <= 180:
    gram_hour = 90
elif time >= 210:
    gram_hour = 60
else:
    gram_hour = 60 + (210 - time)

st.text(time)

st.text(gram_hour)

total_glucides = (time / 3600) * gram_hour

total_gels = total_glucides / gram_gels

split_secondes = time / total_gels

def secondes_to_minutes(x):
    minutes = math.floor(x / 60)
    seconds = int(x % 60)
    return f"{minutes:02d}:{seconds:02d}"


st.text(total_gels)

range_splits_secondes = [i*split_secondes for i in list(range(total_gels)) ]
range_splits_minutes = [secondes_to_minutes(i) for i in range_splits_secondes]

speed = 42195 / time
range_splits_km = [(speed*i)/1000 for i in range_splits_secondes]

def speed_to_pace(speed):

    pace_seconds = 1000 / speed
    minutes = math.floor(pace_seconds / 60)
    seconds = int(pace_seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

st.divider()

st.text(f"Vitesse: {speed_to_pace(speed)}")

st.text(f"Total de glucides : {total_glucides}")

st.text(f"Total de gels : {total_gels}")

st.text(f"Soit un gel aux minutes {range_splits_minutes}")

st.text(f"Soit un gel aux Km {range_splits_km}")





                            

    
   

    