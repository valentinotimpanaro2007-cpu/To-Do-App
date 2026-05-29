import { StrictMode } from 'react'        // React-Modus für strengere Entwicklung
import { createRoot } from 'react-dom/client'  // Erstellt den React-Root im Browser
import App from './App.jsx'               // Hauptkomponente der App

// Bindet die React-App an das HTML-Element mit der ID "root"
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />     {/* Startet die gesamte Anwendung */}
  </StrictMode>,
)
