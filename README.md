# anti-phase_noise_generator
Dataset : https://github.com/microsoft/DNS-Challenge  
`git clone https://github.com/microsoft/DNS-Challenge`

## Environment Setting through the docker
### run the python docker image
`sudo docker run -it -v /home/gsethan/DNS-Challenge:/home/workspace/DNS-Challenge --name ANG python /bin/bash`
`cd home/workspace/DNS-Challenge`

### Install libraries which is needed
`pip install pandas`
`pip install librosa`
`pip install soundfile`

### Install Git LFS Function
`curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash`  
`apt install git-lfs`  

### Install Git Large File Storage for faster download of the datasets
`git lfs install`
`git lfs track "*.wav"`  
`git add .gitattributes`

### solve the "sndfile library not found" error
`apt-get install libsndfile1`

### Create dataset
`python noisyspeech_synthesizer_singleprocess.py`

