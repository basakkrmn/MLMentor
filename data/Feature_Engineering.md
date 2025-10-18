# Feature Engineering and Data Preprocessing

Feature engineering transforms raw data into **informative inputs** for models.

## Techniques
- **Normalization:** Scaling features to [0,1] range.
- **Standardization:** Scaling features to zero mean and unit variance.
- **Encoding Categorical Variables:** Convert categories to numbers (One-Hot Encoding, Label Encoding).
- **Handling Missing Data:** Imputation with mean/median/mode or deletion.
- **Feature Selection:** Choosing most relevant features using correlation, mutual information, or model-based methods.

## Importance
- Reduces overfitting
- Improves model accuracy
- Reduces computational cost

## Example
- For predicting house prices: size, location, age of house as features. One-hot encode categorical variables like neighborhood.
