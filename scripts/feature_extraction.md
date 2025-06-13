# Extracción de características de señales EEG / EEG Feature Extraction / Извлечение признаков ЭЭГ

Este script extrae características estadísticas básicas de señales EEG simuladas o preprocesadas, centradas en las bandas theta, alpha y beta.

---

## 🇪🇸 Descripción

`feature_extraction.py` calcula media, desviación estándar y potencia de cada banda EEG. Estas características son útiles para analizar el nivel de concentración o para entrenar modelos de aprendizaje automático.

### Entrada:
- Tres listas/arrays de numpy: `theta`, `alpha`, `beta` (ondas EEG separadas por banda)

### Salida:
- Diccionario con estadísticas básicas por banda

### Ejemplo de uso:

```python
from feature_extraction import extract_features

caracteristicas = extract_features(theta, alpha, beta)
print(caracteristicas)
