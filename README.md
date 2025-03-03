<img src="https://github.com/Stratisra/AI-Medical-Diagnosis/blob/4ea41bf9463fe422653ce1447bdd79405186ad12/Logo/Personal%20Project_logo_full.png" alt="Logo" width="500"/>

***AI Medical Diagnosis*** is an AI-powered system that can provide a diagnosis based on the symptoms a patient has. The system uses information from the [Disease-Symptom Knowledge Database](https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/) which contains disease-symptom associations. The dataset includes 149 diseases and 404 symptoms in total. Each disease is represented by an asymmetric binary vector, in which a value of 1 for a specific symptom indicates that it is present, whereas 0 indicates that it is not.

AIMD consists of a webpage that contains a mega-menu with the 404 symptoms. The user can select the symptoms that are present in the patient by clicking on them. Pressing the “submit” button at the bottom of the menu triggers a CSV file, containing a binary vector with the user’s selections, to download. Afterward, the Python script calculates the similarity between this vector and each of the disease vectors using Jaccard Similarity, sorts them, and outputs the three most probable diseases the patient might have, along with the confidence level. These diseases are then shown on a “results” webpage.

### [Video Presentation](https://www.youtube.com/watch?v=lntI06v1HxU&t=21s) 
