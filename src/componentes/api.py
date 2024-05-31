from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pickle

# Cargar modelos previamente entrenados y el scaler
with open('logreg_model.pkl', 'rb') as file:
    logreg = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    ss = pickle.load(file)

app = FastAPI()

class UserInput(BaseModel):
    features: list

@app.post("/predict/")
async def predict(user_input: UserInput):
    try:
        # Convertir la entrada del usuario en un array de NumPy
        input_data = np.array([user_input.features])
        # Escalar los datos
        input_scaled = ss.transform(input_data)
        # Realizar la predicción
        prediction = logreg.predict(input_scaled)
        return {"prediction": "Maligno" if prediction[0] == 1 else "Benigno"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)