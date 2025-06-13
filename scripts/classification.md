
---

### 📄 `classification/README.md`

```markdown
# Clasificación de señales EEG / EEG Signal Classification / Классификация сигналов ЭЭГ

Este script entrena y evalúa un modelo SVM para clasificar niveles de concentración a partir de características EEG.

---

## 🇪🇸 Descripción

`classification.py` utiliza un clasificador SVM para aprender patrones de concentración a partir de características extraídas (media, desviación estándar, potencia) de señales EEG.

### Entrada:
- Lista de diccionarios o DataFrame con características EEG
- Lista de etiquetas (0: baja concentración, 1: alta concentración)

### Salida:
- Modelo entrenado
- Porcentaje de exactitud

### Ejemplo de uso:

```python
from classification import train_and_evaluate

modelo, exactitud = train_and_evaluate(features, labels)
print(f"Exactitud del modelo: {exactitud}")
