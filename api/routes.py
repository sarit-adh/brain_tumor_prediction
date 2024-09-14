import os
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from src.modeling import Model

router = APIRouter()

@router.get("/models")
async def get_models():
    saved_models = os.listdir("../trained_models/")
    return [saved_model for saved_model in saved_models if saved_model.endswith(".keras")]
    
@router.post("/predict/")
async def predict(
    base_model_name: str = Form(...),  # Form data for model name
    epochs: int = Form(...),           # Form data for epochs
    image_file: UploadFile = File(...) # File upload for image
):
    
    file_save_path = f"../uploaded_images/{image_file.filename}"
    
    with open(file_save_path, "wb+") as outfile:
        outfile.write(image_file.file.read())
    model = Model(base_model_name, epochs)
    model.load_model("../trained_models/")
    prediction = model.predict( file_save_path)
    probability_tumor = str(prediction[0][1])
    return JSONResponse(content={"prediction": probability_tumor})



    
    