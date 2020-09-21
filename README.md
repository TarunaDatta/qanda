# qanda
Question Answering Chatbot created for the purpose of the Lincode Hackathon

## Dataset

To construct the dataset

    cd data

    wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json -O data/train-v2.0.json

    wget https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json -O data/dev-v2.0.json

## Running the data/DataExploration.ipynb notebook
Warning: The file is very large(1.5gb) and loading the w2vec model consumes a lot of memory

Outside the qanda directory download and extract the W2Vec model using 
    
    cd qanda/../
    
    wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"
    
Go back into the qanda repo and start Jupyter Notebook

    cd qanda/data/
    
    jupyter-notebook
    
