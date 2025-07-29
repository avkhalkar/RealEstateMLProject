## 🏠 Real Estate Price Prediction using ML**

This is a full-stack machine learning project to predict real estate prices based on user input. The application allows users to input property details via a simple front-end and returns predicted prices using a trained ML model served by a Flask backend.

## 📁 Project Structure

RealEstateMLProject/
│
├── Client/ # Front-end interface (HTML/CSS/JS or framework)
├── Server/ # Flask API backend
├── Model/ # Jupyter Notebooks, dataset, columns and trained model pickle file
├── BHP.csv # Dataset used
└── README.md # Project overview

## Workflow

1. **User Input**  
   The user enters details like location, BHK, sqft, etc. via the front-end interface.

2. **API Request**  
   The data is sent to a Flask backend via an HTTP request.

3. **Model Prediction**  
   The server loads a trained regression model and returns the predicted property price.

4. **Result Display**  
   The prediction is shown to the user in a user-friendly format.

## 🛠 Technologies Used

- Python
- Flask(back-end)
- Pandas, NumPy, Scikit-learn
- HTML/CSS/JS (basic front-end)
- Git & GitHub

## 📊 Dataset

-Used a tabular dataset from kaggle
- Link: https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data
- Source: `BHP.csv`
- Contains real estate data from Bangalore including various raw unprocessed features and price.

## 🧠 Model Information
- **Model Used**: The optimal model after fine-tune on GridSearchCV on few of standard ML regressor models like Lasso, DecisionTree, etc and grid of parameters.
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
- **Feature Engineering**: Added price per sqft which is important feature as per domain knowledge
- **Preprocessing**: Handling null values, cleaning and formatting columns having raw data  
- **Outlier Removal**:Using domain knowledge and k-standard deviation techniques
-**Dimensionality Reduction**: Labelling all the locations having very few records as others and then performing One-Hot Encoding
-**Training and Validation**:Used R2 score and k-fold cross validation
-**Testing and Prediction**:Define a custom function for prediction and testing
-**Saving**:Model is saved as pickle file

## How to Run

1. Clone the repo:

    Execute this command to clone the repo

   git clone https://github.com/avkhalkar/RealEstateMLProject.git


Set up a virtual environment and install dependencies, provided in requirements.txt and pythonversion.txt.

Run the Flask server:

cd Server
python app.py
Open Client/index.html in a browser to access the UI.

## Screenshot of the web app

![Preview of Real Estate App](<bhp_website.png>)

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with proper attribution.