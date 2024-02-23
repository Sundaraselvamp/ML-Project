#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
 #   return 'Hello, World!'

#if __name__ == '__main__':
#    app.run(debug=True)

import os
import pickle

from src.components.data_transformation import DataTransformation

# Create the `artifacts` directory if it doesn't exist
os.makedirs('artifacts', exist_ok=True)

# Create a DataTransformation object
data_transformation = DataTransformation()

# Get the preprocessor object
preprocessor = data_transformation.get_data_transformer_object()

# Save the preprocessor object to a file
with open('artifacts/preprocessor.pkl', 'wb') as f:
    pickle.dump(preprocessor, f)
