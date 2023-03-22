# Create docker image
docker build --tag <image_name> .

# Create container with volume and run the API 
docker run -p 5000:5000 id_image

# Open a new terminal tab and create a new python environment (if needed), you may use the requirements.txt file in this process
pip install -r requires.txt

# Send a request to the API given the wav file path

python request.py --filepath=<your_wav_file_path> 








