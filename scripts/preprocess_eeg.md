# preprocess_eeg.py

## Español

Este script contiene funciones básicas para el preprocesamiento de señales EEG. Incluye filtrado pasabanda para aislar las frecuencias relevantes, eliminación de ruido de línea eléctrica mediante un filtro notch y normalización de la señal. Estas técnicas son esenciales para preparar las señales EEG antes de su análisis o procesamiento avanzado.

Funciones principales:
- `bandpass_filter`: Filtra la señal entre dos frecuencias definidas.
- `notch_filter`: Elimina el ruido a 50 Hz (frecuencia típica de la línea eléctrica).
- `normalize_signal`: Normaliza la señal para tener media cero y varianza uno.

Ejemplo de uso incluido al final del script.

---

## English

This script provides basic preprocessing functions for EEG signals. It includes bandpass filtering to isolate relevant frequency bands, removal of powerline noise using a notch filter, and signal normalization. These steps are essential for preparing EEG data for further analysis or advanced processing.

Main functions:
- `bandpass_filter`: Filters the signal between specified frequency cutoffs.
- `notch_filter`: Removes 50 Hz powerline noise.
- `normalize_signal`: Normalizes the signal to zero mean and unit variance.

Example usage is included at the end of the script.

---

## Русский

Этот скрипт содержит базовые функции для предобработки ЭЭГ сигналов. Включает полосовой фильтр для выделения нужных частотных диапазонов, удаление шума сетевой частоты (50 Гц) с помощью фильтра заграждения (notch) и нормализацию сигнала. Эти этапы необходимы для подготовки ЭЭГ данных к дальнейшему анализу или обработке.

Основные функции:
- `bandpass_filter`: Фильтрует сигнал между заданными частотами.
- `notch_filter`: Удаляет шум сетевой частоты 50 Гц.
- `normalize_signal`: Нормализует сигнал с нулевым средним и единичной дисперсией.

Пример использования приведён в конце скрипта.
