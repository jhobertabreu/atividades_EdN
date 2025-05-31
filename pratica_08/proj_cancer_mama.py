from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score

# Carrega e explora os dados
print("--- CARREGANDO DADOS ---")
data = load_breast_cancer()
print(f"Dataset: {data.DESCR.split('.')[0]}")
print(f"Número de amostras: {data.data.shape[0]}")
print(f"Número de características: {data.data.shape[1]}")
print(f"Classes: {data.target_names}")

# Divide os dados
print("\n--- PREPARANDO DADOS ---")
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, 
    test_size=0.3, 
    random_state=42,
    stratify=data.target  
)

print(f"Treino: {len(X_train)} amostras")
print(f"Teste: {len(X_test)} amostras")

# Inicializa e treina o modelo
print("\n--- TREINANDO MODELO ---")
model = RandomForestClassifier(
    n_estimators=100,  
    random_state=42,   
    n_jobs=-1         
)

model.fit(X_train, y_train)
print("Modelo treinado com sucesso!")

# Faz previsões
print("\n--- FAZENDO PREVISÕES ---")
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Calcula métricas
print("\n--- RESULTADOS ---")
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)

# Exibe resultados de forma organizada
print(f"Acurácia:   {accuracy:.3f} ({accuracy*100:.1f}%)")
print(f"Precisão:   {precision:.3f} ({precision*100:.1f}%)")
print(f"Recall:     {recall:.3f} ({recall*100:.1f}%)")
print(f"F1-Score:   {f1:.3f} ({f1*100:.1f}%)")
print(f"AUC-ROC:    {auc:.3f} ({auc*100:.1f}%)")

# Interpreta os resultados de forma simples
print("\n=== INTERPRETAÇÃO ===")
if accuracy >= 0.95:
    print("Excelente performance!")
elif accuracy >= 0.90:
    print("Boa performance!")
elif accuracy >= 0.80:
    print("Performance razoável")
else:
    print("Performance baixa - precisa melhorar")

print(f"\nO modelo acertou {int(accuracy*len(X_test))} de {len(X_test)} casos de teste.")