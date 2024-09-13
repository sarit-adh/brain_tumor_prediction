// Fetch models from the API and populate the dropdown
async function fetchModels() {
    const response = await fetch('http://127.0.0.1:8080/models');
    const models = await response.json();
    const modelSelect = document.getElementById('model');

    models.forEach(model => {
        const option = document.createElement('option');
        option.value = model;
        option.text = model;
        modelSelect.appendChild(option);
    });
}

// Handle the image upload and form submission
document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const fileInput = document.getElementById('fileInput').files[0];
    const modelName = document.getElementById('model').value;
    const formData = new FormData();


    const filenameWithoutExtension = fileInput.name.replace('.keras', '');
    const [baseModelName, epochs] = filenameWithoutExtension.split('_');

    
    formData.append('base_model_name', baseModelName);
    formData.append('epochs', epochs);
    formData.append('image_file', fileInput);


    // Send the form data to the API
    const response = await fetch('http://127.0.0.1:8080/predict/', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('predictionResult').innerText = result.prediction;
});

// Initialize the page by fetching models
fetchModels();