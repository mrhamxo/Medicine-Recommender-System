# Medicine Recommender System

## Project Summary
The **Medicine Recommender System** is designed to provide alternative medicine recommendations based on content similarity. It helps users find alternatives for medicines by leveraging a dataset of pharmaceutical products and applying machine learning techniques to identify similar drugs based on their descriptions and reasons for usage.

This tool is built using Python and Streamlit, with the machine learning model employing cosine similarity to suggest alternatives. The recommender is useful in cases where a particular medicine is unavailable or the user seeks cheaper or more effective alternatives.

## Methodology
The project follows a content-based filtering approach:
1. **Data Preprocessing**: Each medicine's description and reason for use are tokenized, stemmed, and concatenated into tags. These tags are then converted into vectors using the `CountVectorizer`.
2. **Cosine Similarity**: The similarity between medicines is calculated using cosine similarity on the generated vectors.
3. **Recommendation Algorithm**: For a given medicine, the system ranks other medicines based on their similarity score and suggests the top alternatives.

Key technologies used include:
- **Streamlit**: For building the interactive web application.
- **scikit-learn**: For vectorization and cosine similarity calculation.
- **NLTK**: For text preprocessing (stemming).

## Dataset
The dataset consists of a CSV file containing medicine names, descriptions, and reasons for their use. It was cleaned to remove duplicates and null values, and the textual data was processed to create meaningful tags for each medicine.

### Dataset Features: [Dataset Link](https://www.kaggle.com/datasets/saratchendra/medicine-recommendation)
- `Drug_Name`: The name of the medicine.
- `Description`: A brief description of the medicine.
- `Reason`: The reason the medicine is prescribed or its use case.


The dataset was transformed into a format suitable for machine learning by processing the text and creating vectors for each medicine's "tags".

## Project Workflow
1. **Load Dataset**: Load and preprocess the dataset of medicines.
2. **Preprocess Data**: Tokenize and stem the descriptions and reasons for medicines.
3. **Generate Tags**: Concatenate the tokens into a single "tags" column.
4. **Vectorization**: Use `CountVectorizer` to convert tags into vectors.
5. **Cosine Similarity**: Compute the similarity matrix using cosine similarity.
6. **Recommendations**: Based on the cosine similarity, recommend top 5 alternative medicines.

## Application Snapshot
Here’s a snapshot of the **Medicine Recommender System** interface:

User Interface App Screenshot
![user interface](https://github.com/user-attachments/assets/65a52e2d-2ba0-4195-ba6d-a02be3ae9779)

## Conclusion
The **Medicine Recommender System** provides an efficient solution for recommending alternative medicines. By utilizing text-based similarity measures, it identifies related medicines that could serve as substitutes for the queried medicine. This approach is flexible and can easily be adapted to other domains where text-based recommendation is relevant.

### Future Enhancements
- **Incorporate User Ratings**: Improve recommendations by incorporating user feedback or reviews.
- **Advanced NLP**: Use more sophisticated NLP techniques like word embeddings to enhance the similarity measure.
- **Price-Based Recommendations**: Factor in price when recommending medicines to provide cheaper alternatives.
