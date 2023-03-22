
# Create docker image
docker build --tag <image_name> .

# Create container with volume and run API (specify where you want to store your wav files in your host in the "source" option, target must be kept unchanged)
docker run  -p <host_port>:5000 --name <container_name> --mount type=bind,source=<your_local_wav_path>,target=/app/wav <image_name>

# Call the API: give the wav name
python request.py --fileName=<your_file_name> --host_port=<host_port>