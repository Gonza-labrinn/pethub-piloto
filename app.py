import streamlit as st
import pandas as pd

# 1. Base de datos simulada (Reemplaza la nube por ahora)
base_de_datos = {
    "123456789012345": {
        "nombre": "Roco",
        "especie": "Canino - Mestizo",
        "tutor": "Rodrigo Araya",
        "alergias": "🔴 Alérgico a la Penicilina",
        "historial": [
            {"Fecha": "2026-05-10", "Evento": "Urgencia - Traumatismo", "Clínica": "Vet Peñablanca"},
            {"Fecha": "2025-12-01", "Evento": "Vacuna Óctuple", "Clínica": "Vet Centro Villa Alemana"},
            {"Fecha": "2025-08-15", "Evento": "Implantación Microchip", "Clínica": "Operativo Municipal"}
        ]
    }
}

# 2. Interfaz Visual de la App
st.set_page_config(page_title="PetHub Pro - Triage", page_icon="🐾")
st.title("🐾 PetHub Pro: Acceso Clínico")
st.write("Plataforma Interoperable de Salud Animal (Piloto Villa Alemana)")

st.markdown("---")

# 3. Buscador del Microchip
chip_ingresado = st.text_input("Pase el escáner RFID o digite el microchip (15 dígitos):", max_chars=15)

if st.button("Buscar Historial Clínico"):
    if chip_ingresado in base_de_datos:
        paciente = base_de_datos[chip_ingresado]
        st.success(f"✅ Identidad Confirmada: {paciente['nombre']}")
        
        # Mostrar datos críticos rápido (Triage)
        st.subheader("⚠️ Alertas Médicas (Triage)")
        st.error(paciente['alergias'])
        
        st.subheader("📖 Historial Médico Unificado")
        # Convertir los datos a una tabla visual
        tabla_historial = pd.DataFrame(paciente['historial'])
        st.table(tabla_historial)
    elif chip_ingresado == "":
        st.warning("Por favor ingrese un número de chip.")
    else:
        st.error("❌ Paciente no encontrado en la red. Solicite código QR temporal.")
