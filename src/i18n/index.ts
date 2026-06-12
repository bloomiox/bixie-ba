import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import bs from './bs.json';
import en from './en.json';
import de from './de.json';

i18n.use(initReactI18next).init({
  resources: { bs: { translation: bs }, en: { translation: en }, de: { translation: de } },
  lng: 'bs',
  fallbackLng: 'bs',
  interpolation: { escapeValue: false },
});

export default i18n;
