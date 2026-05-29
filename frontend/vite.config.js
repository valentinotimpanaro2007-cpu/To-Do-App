import { defineConfig } from 'vite'          // Vite-Konfigurationsfunktion
import react from '@vitejs/plugin-react'     // React-Plugin für Vite

// Vite-Konfiguration: definiert Build- und Dev-Server-Einstellungen
export default defineConfig({
  plugins: [react()],   // React-Unterstützung aktivieren
})
