# Simulazione Elettromagnetica 🧲

Una applicazione interattiva per la visualizzazione e simulazione di fenomeni elettromagnetici, sviluppata con Python e Streamlit.

## 📝 Descrizione

Questa applicazione permette di visualizzare e interagire con tre diverse simulazioni elettromagnetiche:

1. **Flusso Magnetico e F.E.M.I.**
   - Visualizzazione del flusso magnetico e della forza elettromotrice indotta
   - Simulazione in tempo reale dell'andamento delle grandezze
   - Controllo dei parametri (numero spire, area bobina, campo magnetico, frequenza)

2. **Andamento Corrente-Tensione in Induttore DC**
   - Visualizzazione dell'andamento della corrente in un induttore DC
   - Simulazione della tensione ai capi dell'induttore
   - Controllo dei parametri (tensione, resistenza, induttanza)

3. **Sfasamento Tensione-Corrente in Induttore AC**
   - Visualizzazione dello sfasamento di 90° tra tensione e corrente
   - Simulazione in tempo reale del comportamento in regime sinusoidale
   - Controllo dei parametri (ampiezza tensione, frequenza, induttanza)

## 🚀 Come iniziare

### Prerequisiti

- Python 3.7 o superiore
- pip (gestore pacchetti Python)

### Installazione

1. Clona il repository:
```bash
git clone https://github.com/your-username/simulazione-elettromagnetica.git
cd simulazione-elettromagnetica
```

2. Installa le dipendenze necessarie:
```bash
pip install -r requirements.txt
```

3. Avvia l'applicazione:
```bash
streamlit run "Simulazione della Forza Elettromotrice Indotta.py"
```

## 🎮 Utilizzo

1. Seleziona una simulazione dal menu a sinistra
2. Modifica i parametri usando gli slider
3. Osserva la simulazione in tempo reale
4. Regola la velocità della simulazione secondo le tue esigenze

## 🔬 Dettagli Tecnici

### Flusso Magnetico e F.E.M.I.
- Calcolo del flusso magnetico: Φ = NBA sin(ωt)
- Calcolo della F.E.M.I.: ε = -NBA ω cos(ωt)

### Induttore DC
- Corrente: I(t) = I∞(1 - e^(-t/τ))
- Tensione: V_L(t) = V e^(-t/τ)
- Costante di tempo: τ = L/R

### Induttore AC
- Tensione: v(t) = V_max sin(ωt)
- Corrente: i(t) = I_max sin(ωt - 90°)
- Impedenza induttiva: Z_L = ωL
