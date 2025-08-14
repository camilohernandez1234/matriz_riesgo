import streamlit as st
import pandas as pd

# -------------------
# Configuración inicial
# -------------------

riesgo = "Ataque de ransomware que compromete la disponibilidad del sistema"

# Controles ISO 27001:2022 y su efecto
controles = {
    "Política de seguridad de la información (A.5.1)": {"impacto": -1, "probabilidad": -1},
    "Control de acceso a la información (A.5.15)": {"impacto": 0, "probabilidad": -2},
    "Gestión de identidades (A.5.16)": {"impacto": 0, "probabilidad": -1},
    "Cifrado de datos (A.8.24)": {"impacto": -2, "probabilidad": 0},
    "Protección contra malware (A.8.7)": {"impacto": 0, "probabilidad": -2},
    "Plan de continuidad del negocio TIC (A.5.30)": {"impacto": -3, "probabilidad": 0},
    "Gestión de vulnerabilidades técnicas (A.8.8)": {"impacto": 0, "probabilidad": -1},
    "Copias de seguridad (A.8.13)": {"impacto": -2, "probabilidad": 0},
    "Seguridad de la red (A.8.20)": {"impacto": -1, "probabilidad": -1},
    "Protección física de equipos (A.7.10)": {"impacto": -1, "probabilidad": 0},
    "Seguridad en las comunicaciones (A.8.19)": {"impacto": -1, "probabilidad": -1},
    "Gestión de incidentes de seguridad (A.5.24)": {"impacto": -1, "probabilidad": -2},
    "Uso aceptable de activos (A.5.10)": {"impacto": 0, "probabilidad": -1},
    "Protección contra código malicioso (A.8.6)": {"impacto": 0, "probabilidad": -2},
    "Control de cambios (A.8.32)": {"impacto": -1, "probabilidad": -1},
    "Monitoreo de seguridad (A.8.16)": {"impacto": -1, "probabilidad": -2},
    "Seguridad en dispositivos móviles (A.6.2)": {"impacto": 0, "probabilidad": -1},
    "Protección de la información en tránsito (A.8.21)": {"impacto": -1, "probabilidad": -1},
    "Revisión de acceso de usuarios (A.5.18)": {"impacto": 0, "probabilidad": -1},
    "Concientización y capacitación en seguridad (A.6.3)": {"impacto": -1, "probabilidad": -1}
}

# Descripciones breves
descripciones = {
    "Política de seguridad de la información (A.5.1)": "Define las reglas generales de protección de la información.",
    "Control de acceso a la información (A.5.15)": "Restringe el acceso solo a usuarios autorizados.",
    "Gestión de identidades (A.5.16)": "Administra cuentas y credenciales de usuarios.",
    "Cifrado de datos (A.8.24)": "Protege información confidencial mediante cifrado.",
    "Protección contra malware (A.8.7)": "Previene infecciones por software malicioso.",
    "Plan de continuidad del negocio TIC (A.5.30)": "Recupera servicios críticos tras incidentes.",
    "Gestión de vulnerabilidades técnicas (A.8.8)": "Detecta y corrige debilidades técnicas.",
    "Copias de seguridad (A.8.13)": "Respalda datos importantes para su recuperación.",
    "Seguridad de la red (A.8.20)": "Protege la red contra accesos no autorizados.",
    "Protección física de equipos (A.7.10)": "Evita daños o robos de hardware.",
    "Seguridad en las comunicaciones (A.8.19)": "Protege datos transmitidos por redes.",
    "Gestión de incidentes de seguridad (A.5.24)": "Responde a incidentes de seguridad.",
    "Uso aceptable de activos (A.5.10)": "Normas para el uso seguro de recursos.",
    "Protección contra código malicioso (A.8.6)": "Previene ataques por código malicioso.",
    "Control de cambios (A.8.32)": "Gestiona cambios para evitar riesgos.",
    "Monitoreo de seguridad (A.8.16)": "Supervisa sistemas para detectar amenazas.",
    "Seguridad en dispositivos móviles (A.6.2)": "Protege datos en dispositivos portátiles.",
    "Protección de la información en tránsito (A.8.21)": "Asegura datos durante la transmisión.",
    "Revisión de acceso de usuarios (A.5.18)": "Verifica permisos de acceso periódicamente.",
    "Concientización y capacitación en seguridad (A.6.3)": "Forma al personal en buenas prácticas."
}
# Función para calcular riesgo

def calcular_riesgo(controles_aplicados):
    prob = 9
    imp = 9

    for control in controles_aplicados:
        efecto = controles[control]
        prob += efecto["probabilidad"]
        imp += efecto["impacto"]

    prob = max(1, min(9, prob))
    imp = max(1, min(9, imp))
    nivel = prob * imp

    if nivel <= 20:
        categoria = "Bajo"
        color = "🟢"
    elif nivel <= 50:
        categoria = "Medio"
        color = "🟡"
    else:
        categoria = "Alto"
        color = "🔴"

    if prob >= 8:
        texto_prob = "Muy Alta"
    elif prob >= 6:
        texto_prob = "Alta"
    elif prob >= 4:
        texto_prob = "Media"
    elif prob >= 2:
        texto_prob = "Baja"
    else:
        texto_prob = "Muy Baja"

    return prob, imp, nivel, categoria, color, texto_prob


# muchachos aqui dejo la interfaz grafica 

st.set_page_config(page_title="Matriz de Riesgo", layout="centered")
st.title("Matriz de Riesgo")
st.subheader(riesgo)

# Selección de controles
controles_aplicados = st.multiselect(
    "Selecciona los controles aplicados:",
    list(controles.keys())
)

# Mostrar descripciones en letra pequeña
if controles_aplicados:
    st.markdown(" Descripción :")
    for c in controles_aplicados:
        st.markdown(f"<small>**{c}:** {descripciones[c]}</small>", unsafe_allow_html=True)

# Cálculo del riesgo
prob, imp, nivel, categoria, color, texto_prob = calcular_riesgo(controles_aplicados)

# Mostrar resultados
st.markdown(f"Probabilidad final: {prob} / 9 ({texto_prob})")
st.markdown(f"Impacto final: {imp} / 9")
st.markdown(f"Nivel de riesgo: {nivel} {color} ({categoria})")


# en esta parte se genera la matriz

st.write(" Matriz de Riesgo 9×9")
matriz = []
for i in range(9, 0, -1):
    fila = []
    for j in range(1, 10):
        valor = i * j
        if valor <= 20:
            cell = "🟢 Bajo"
        elif valor <= 50:
            cell = "🟡 Medio"
        else:
            cell = "🔴 Alto"
        if i == round(prob) and j == round(imp):
            cell += " ⬅️"
        fila.append(cell)
    matriz.append(fila)

df = pd.DataFrame(matriz, index=[9,8,7,6,5,4,3,2,1], columns=[1,2,3,4,5,6,7,8,9])
st.dataframe(df)
