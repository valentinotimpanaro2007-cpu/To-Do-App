import js from '@eslint/js'                  // Basis-Regeln
import globals from 'globals'                // Globale Variablen (z.B. Browser)
import reactHooks from 'eslint-plugin-react-hooks'  // Regeln für React Hooks
import reactRefresh from 'eslint-plugin-react-refresh'  // Regeln für React Refresh
import { defineConfig, globalIgnores } from 'eslint/config'

// ESLint-Konfiguration: stellt Code-Qualität sicher
export default defineConfig([
  globalIgnores(['dist']),     // 'dist'-Ordner ignorieren
  {
    files: ['**/*.{js,jsx}'],  // Nur JS/JSX-Dateien prüfen
    extends: [
      js.configs.recommended,              // Standard-JS-Regeln
      reactHooks.configs.flat.recommended,  // React-Hooks-Regeln
      reactRefresh.configs.vite,            // React-Refresh-Regeln
    ],
    languageOptions: {
      globals: globals.browser,         // Browser-Globals (z.B. window)
      parserOptions: { ecmaFeatures: { jsx: true } },  // JSX erlauben
    },
  },
])
