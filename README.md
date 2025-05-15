# Django ML Prediction API

This project is a Django REST API that serves multiple machine learning models to predict student exam scores based on input features.

---

## API Endpoint

### API Key `https://ml-project-1e2k.onrender.com`
### POST `/api/predict/`

Predicts exam scores based on provided features and selected ML model.

---

## Request Format

Content-Type: `application/x-www-form-urlencoded`

---

## Request Parameters

| Parameter                      | Type    | Description                                               | Required | Example    |
|-------------------------------|---------|-----------------------------------------------------------|----------|------------|
| age                           | float   | Student's age in years                                     | Yes      | 18         |
| study_hours_per_day            | float   | Average number of hours the student studies per day       | Yes      | 3.5        |
| social_media_hours             | float   | Average hours spent on social media per day                | Yes      | 2          |
| netflix_hours                 | float   | Average hours spent watching Netflix per day               | Yes      | 1.5        |
| attendance_percentage          | float   | Percentage of classes attended                             | Yes      | 90         |
| sleep_hours                   | float   | Average hours of sleep per night                            | Yes      | 7          |
| exercise_frequency            | float   | Frequency of exercise (numeric scale, e.g., 0-7 days/week) | Yes      | 4          |
| mental_health_rating          | float   | Self-reported mental health rating (e.g., 1-10 scale)      | Yes      | 5          |
| dq_e                          | int     | Diet quality encoded (0=Poor, 1=Fair, 2=Good)              | Yes      | 2          |
| pel_e                         | int     | Parental education level encoded (0=High School, 1=Bachelor, 2=Master) | Yes | 1          |
| iq_e                          | int     | Internet quality encoded (0=Poor, 1=Average, 2=Good)       | Yes      | 2          |
| gender_Male                   | int     | Gender dummy variable (1 if Male, 0 otherwise)              | Yes      | 1          |
| gender_Other                  | int     | Gender dummy variable (1 if Other, 0 otherwise)             | Yes      | 0          |
| part_time_job_Yes             | int     | Part-time job dummy variable (1 if yes, 0 if no)            | Yes      | 0          |
| extracurricular_participation_Yes | int | Extracurricular participation dummy (1 if yes, 0 if no)    | Yes      | 1          |
| model                         | string  | Machine learning model to use: `linear`, `ridge`, `lasso`, or `random_forest` | Yes | `random_forest` |

---

## Sample Request (form data)

