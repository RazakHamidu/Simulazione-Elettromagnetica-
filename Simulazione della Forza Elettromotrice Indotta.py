import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import time

# Configurazione dell'interfaccia utente con Streamlit
st.title("Simulazione Elettromagnetica")
st.write("Seleziona una simulazione dal menu a sinistra.")

# Creazione della sidebar per la selezione della pagina
pagina = st.sidebar.selectbox("Seleziona una simulazione", [
    "Flusso Magnetico e F.E.M.I.",
    "Andamento della Corrente in un Induttore DC e Tensione ai capi",
    "Sfasamento Tensione-Corrente in un Induttore AC"
])

if pagina == "Flusso Magnetico e F.E.M.I.":
    st.header("Flusso Magnetico e Forza Elettromotrice Indotta (F.E.M.I.)")
    st.write("Modifica i parametri e avvia la simulazione per osservare i cambiamenti.")

    # Input dell'utente per i parametri fisici del sistema
    N = st.slider("Numero di spire (N)", min_value=1, max_value=500, value=100)
    A = st.slider("Area della bobina (m^2)", min_value=0.001, max_value=0.1, value=0.01, step=0.001)
    B0 = st.slider("Campo magnetico massimo (T)", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
    f = st.slider("Frequenza (Hz)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    w = 2 * np.pi * f  # Calcolo della pulsazione (ω = 2πf)

    def flusso_magnetico(t):
        return N * A * B0 * np.sin(w * t)

    def fem_indotta(t):
        return -N * A * B0 * w * np.cos(w * t)

    fig, ax = plt.subplots()
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Flusso Magnetico (Wb) / F.E.M.I. (V)")
    ax.set_title("Flusso Magnetico e F.E.M.I. Indotta nel Tempo")
    ax.grid(True, linestyle="--", alpha=0.7)

    t_data, flux_data, fem_data = [], [], []
    plot_placeholder = st.empty()

    # Aggiungi il controllo della velocità della simulazione
    speed = st.slider("Velocità della simulazione (tempo di aggiornamento in secondi)", min_value=0.01, max_value=0.5, value=0.05, step=0.01)

    for frame in range(200):
        t = frame / 100
        flux = flusso_magnetico(t)
        fem = fem_indotta(t)
        
        t_data.append(t)
        flux_data.append(flux)
        fem_data.append(fem)
        
        if t > 2:
            t_data.pop(0)
            flux_data.pop(0)
            fem_data.pop(0)
        
        ax.clear()
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Flusso Magnetico (Wb) / F.E.M.I. (V)")
        ax.set_title("Flusso Magnetico e F.E.M.I. Indotta nel Tempo")
        ax.grid(True, linestyle="--", alpha=0.7)
        ax.plot(t_data, flux_data, lw=2, label="Flusso Magnetico Φ_B", color='#1f77b4')
        ax.plot(t_data, fem_data, lw=2, label="F.E.M.I. Indotta E", color='#ff7f0e', linestyle='dashed')
        ax.legend(loc='upper right', fontsize=10)
        
        plot_placeholder.pyplot(fig)
        time.sleep(speed)  # Usa il valore scelto per la velocità della simulazione

elif pagina == "Andamento della Corrente in un Induttore DC e Tensione ai capi":
    st.header("Andamento della Corrente e della Tensione in un Induttore DC")
    st.write("Ecco i grafici dell'andamento della corrente e della tensione ai capi di un induttore alimentato con corrente continua.")
    
    # Input per i parametri dell'induttore
    V = st.slider("Tensione di alimentazione (V)", min_value=1.0, max_value=100.0, value=10.0, step=0.1)
    R = st.slider("Resistenza (Ω)", min_value=0.1, max_value=100.0, value=10.0, step=0.1)
    L = st.slider("Induttanza (H)", min_value=0.001, max_value=10.0, value=1.0, step=0.001)
    
    tau = L / R  # Costante di tempo
    I_inf = V / R  # Corrente finale
    
    # Impostazione per la visualizzazione in tempo reale
    t_vals = np.linspace(0, 5 * tau, 500)  # Intervallo di tempo
    I_vals = np.zeros_like(t_vals)  # Array per la corrente
    V_L_vals = np.zeros_like(t_vals)  # Array per la tensione

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Impostazione dei grafici
    ax1.set_xlabel("Tempo (s)", fontsize=12)
    ax1.set_ylabel("Corrente (A)", fontsize=12)
    ax1.set_title("Andamento della Corrente in un Induttore DC", fontsize=14)
    ax1.plot(t_vals, I_vals, label="Corrente I(t)", color='#2ca02c', lw=2)
    ax1.axhline(I_inf, linestyle='--', color='gray', label="I∞", lw=1.5)
    ax1.axvline(tau, linestyle='--', color='red', label="τ", lw=1.5)
    ax1.grid(True, linestyle="--", alpha=0.7)
    ax1.legend(loc='upper left', fontsize=10)

    ax2.set_xlabel("Tempo (s)", fontsize=12)
    ax2.set_ylabel("Tensione (V)", fontsize=12)
    ax2.set_title("Andamento della Tensione ai capi di un Induttore DC", fontsize=14)
    ax2.plot(t_vals, V_L_vals, label="Tensione V_L(t)", color='#ff7f0e', lw=2)
    ax2.axhline(0, linestyle='--', color='gray', label="Zero Tensione", lw=1.5)
    ax2.grid(True, linestyle="--", alpha=0.7)
    ax2.legend(loc='upper right', fontsize=10)

    # Aggiungiamo uno spazio maggiore tra i grafici
    plt.subplots_adjust(hspace=0.5)

    plot_placeholder = st.empty()

    # Aggiungi il controllo della velocità della simulazione
    speed = st.slider("Velocità della simulazione (tempo di aggiornamento in secondi)", min_value=0.01, max_value=0.5, value=0.05, step=0.01)

    # Ciclo per aggiornare i grafici in tempo reale
    for i in range(len(t_vals)):
        I_vals[i] = I_inf * (1 - np.exp(-t_vals[i] / tau))  # Aggiorno la corrente
        V_L_vals[i] = V * np.exp(-t_vals[i] / tau)  # Aggiorno la tensione
        
        # Aggiorno i grafici
        ax1.clear()
        ax1.plot(t_vals[:i+1], I_vals[:i+1], label="Corrente I(t)", color='#2ca02c', lw=2)
        ax1.axhline(I_inf, linestyle='--', color='gray', label="I∞", lw=1.5)
        ax1.axvline(tau, linestyle='--', color='red', label="τ", lw=1.5)
        ax1.set_xlabel("Tempo (s)", fontsize=12)
        ax1.set_ylabel("Corrente (A)", fontsize=12)
        ax1.set_title("Andamento della Corrente in un Induttore DC", fontsize=14)
        ax1.grid(True, linestyle="--", alpha=0.7)
        ax1.legend(loc='upper left', fontsize=10)

        ax2.clear()
        ax2.plot(t_vals[:i+1], V_L_vals[:i+1], label="Tensione V_L(t)", color='#ff7f0e', lw=2)
        ax2.axhline(0, linestyle='--', color='gray', label="Zero Tensione", lw=1.5)
        ax2.set_xlabel("Tempo (s)", fontsize=12)
        ax2.set_ylabel("Tensione (V)", fontsize=12)
        ax2.set_title("Andamento della Tensione ai capi di un Induttore DC", fontsize=14)
        ax2.grid(True, linestyle="--", alpha=0.7)
        ax2.legend(loc='upper right', fontsize=10)

        plot_placeholder.pyplot(fig)
        time.sleep(speed)  # Usa il valore scelto per la velocità della simulazione

elif pagina == "Sfasamento Tensione-Corrente in un Induttore AC":
    st.header("Sfasamento Tensione-Corrente in un Induttore AC")
    st.write("Visualizzazione dello sfasamento di 90° tra tensione e corrente in un induttore alimentato in corrente alternata.")
    
    # Input per i parametri
    V_max = st.slider("Ampiezza massima della tensione (V)", min_value=1.0, max_value=50.0, value=10.0, step=0.1)
    f = st.slider("Frequenza (Hz)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    L = st.slider("Induttanza (H)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    
    # Calcoli
    w = 2 * np.pi * f  # Pulsazione
    Z_L = w * L  # Impedenza induttiva
    I_max = V_max / Z_L  # Ampiezza massima della corrente
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Tensione (V) / Corrente (A)")
    ax.set_title("Sfasamento Tensione-Corrente in un Induttore AC")
    ax.grid(True, linestyle="--", alpha=0.7)
    
    # Impostazione degli assi
    ax.set_ylim(-max(V_max, I_max)*1.2, max(V_max, I_max)*1.2)
    
    plot_placeholder = st.empty()
    
    # Controllo della velocità
    speed = st.slider("Velocità della simulazione (tempo di aggiornamento in secondi)", 
                     min_value=0.01, max_value=0.5, value=0.05, step=0.01)
    
    # Array per memorizzare i dati
    t_data = []
    v_data = []
    i_data = []
    
    # Simulazione in tempo reale
    for frame in range(400):
        t = frame / 50
        
        # Calcolo tensione e corrente
        v_t = V_max * np.sin(w * t)  # Tensione
        i_t = I_max * np.sin(w * t - np.pi/2)  # Corrente (sfasata di -90°)
        
        t_data.append(t)
        v_data.append(v_t)
        i_data.append(i_t)
        
        # Mantieni solo gli ultimi 200 punti
        if len(t_data) > 200:
            t_data.pop(0)
            v_data.pop(0)
            i_data.pop(0)
        
        ax.clear()
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Tensione (V) / Corrente (A)")
        ax.set_title("Sfasamento Tensione-Corrente in un Induttore AC")
        ax.grid(True, linestyle="--", alpha=0.7)
        
        # Plot delle curve
        ax.plot(t_data, v_data, 'r-', label='Tensione V_L(t)', linewidth=2)
        ax.plot(t_data, i_data, 'b-', label='Corrente I_L(t)', linewidth=2)
        
        # Aggiungi legenda e griglia
        ax.legend(loc='upper right')
        ax.set_ylim(-max(V_max, I_max)*1.2, max(V_max, I_max)*1.2)
        
        plot_placeholder.pyplot(fig)
        time.sleep(speed)
