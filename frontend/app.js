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


    const filenameWithoutExtension = modelName.replace('.keras', '');
    const [baseModelName, epochs] = filenameWithoutExtension.split('_');

    
    // Show the loading spinner
    document.getElementById('loading').style.display = 'block';

    formData.append('base_model_name', baseModelName);
    formData.append('epochs', epochs);
    formData.append('image_file', fileInput);

    try {
        // Send the form data to the API
        const response = await fetch('http://127.0.0.1:8080/predict/', {
            method: 'POST',
            body: formData
        });

        // Check if the response is okay
        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }

        const result = await response.json();
        const probabilityTumor = result.prediction;

        console.log(probabilityTumor)


        // Display the result in a user-friendly format
        const predictionText = `Probability of brain tumor: ${(probabilityTumor * 100).toFixed(2)}%`;
        document.getElementById('predictionResult').innerText = predictionText;

        // Change the text color based on the probability
        const predictionElement = document.getElementById('predictionResult');
        if (probabilityTumor > 0.75) {
            predictionElement.style.color = 'darkred';  // High probability of brain tumor
        } else if (probabilityTumor > 0.5) {
            predictionElement.style.color = 'orange';  // Medium-high probability
        } else if (probabilityTumor > 0.25) {
            predictionElement.style.color = 'yellowgreen';  // Medium-low probability
        } else {
            predictionElement.style.color = 'darkgreen';  // Low probability of brain tumor
        }

    } catch (error) {
        console.error("Error during file upload and prediction:", error);
        alert("An error occurred while uploading the file or fetching the prediction.");
    } finally {
        // Hide the loading spinner
        document.getElementById('loading').style.display = 'none';
    }


});

// Initialize the page by fetching models
fetchModels();