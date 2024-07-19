# ATS Resume Tracker with Google Generative AI

![Project Logo](https://img.shields.io/badge/Google%20Generative%20AI-Project-blue) ![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Overview

**ATS Resume Tracker** is an advanced Applicant Tracking System (ATS) that leverages Google Generative AI to evaluate resumes against job descriptions. It provides detailed insights into resume fit, skill enhancement recommendations, and match percentages to streamline the recruitment process.

## 🛠️ Features

- **Resume Evaluation:** Analyze how well a resume matches the provided job description.
- **Skill Improvement Recommendations:** Get insights into skills enhancement areas.
- **Match Percentage:** Receive a percentage score indicating the resume's fit with the job description.
- **PDF Handling:** Upload and process resumes in PDF format.

## 📦 Installation

To set up and run the ATS Resume Tracker, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Bolliboinapavansai/ATS_Resume-Tracker.git
    cd ATS_Resume-Tracker
    ```

2. **Set Up Your Environment:**

    Ensure you have Python 3.8 or later. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables:**

    Create a `.env` file in the root directory with your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```

4. **Run the Application:**

    ```bash
    streamlit run app.py
    ```

## 📜 Usage

1. **Open the App:**

    Navigate to `http://localhost:8501` in your browser to open the Streamlit app.

2. **Input Job Description:**

    Enter the job description in the provided text area.

3. **Upload Your Resume:**

    Use the file uploader to upload your resume in PDF format.

4. **Submit Queries:**

    - **About the Resume:** Click to receive a detailed evaluation of how well the resume matches the job description.
    - **Skill Improvement:** Click to get recommendations for skill enhancement.
    - **Percentage Match:** Click to get a percentage score indicating the resume’s fit with the job description.

## 💡 Example

Here is an example of the output you might receive:

- **About the Resume:** "The candidate’s qualifications align well with the job requirements. Key strengths include..."
- **Skill Improvement:** "To better align with the job requirements, the candidate should focus on improving skills in..."
- **Percentage Match:** "The resume matches the job description by 85%. Missing keywords include..."

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository:**
    Click the “Fork” button at the top right of this page.

2. **Create a Branch:**
    ```bash
    git checkout -b feature/your-feature
    ```

3. **Make Changes and Commit:**
    ```bash
    git add .
    git commit -m "Add your feature"
    ```

4. **Push to Your Fork:**
    ```bash
    git push origin feature/your-feature
    ```

5. **Create a Pull Request:**
    Go to the “Pull Requests” tab and submit a new pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📧 Contact

For questions or feedback, please reach out to me at [pavansai.bolliboina@gmail.com]

---

**Built with** 🛠️ [Streamlit](https://streamlit.io), [Google Generative AI](https://cloud.google.com/generative-ai), and Python.

