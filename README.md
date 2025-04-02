# Indian Traffic Violation Analysis

This project analyzes traffic violation data from India to identify patterns and trends.

## Installation
```sh
pip install -r requirements.txt
```

## ✅ Run tests with coverage

```sh
coverage run -m unittest discover -s tests
```

## 📊 Generate coverage report:
```sh
coverage report -m
```


##  Generating graphics
```sh
python -m scripts.run_analysis
```

![driver_age_distribution](https://github.com/user-attachments/assets/5f225547-d8be-46cd-8cb7-2c9131e44906)


![driver_gender_distribution](https://github.com/user-attachments/assets/a48e3087-7f3a-4534-8ceb-2616422bfbc3)


![fine_amount_distribution](https://github.com/user-attachments/assets/dcce5712-ddfd-4f32-a80e-9095d327aa46)


![regional_distribution](https://github.com/user-attachments/assets/531d176a-266d-4a00-a61d-4ca9dd796271)


![time_analysis](https://github.com/user-attachments/assets/b3194d54-ad31-4431-afd1-adc0353831b7)


![time_of_day_distribution](https://github.com/user-attachments/assets/5bd74f9d-7204-4e08-ae48-4cdac0301800)


![violation_types](https://github.com/user-attachments/assets/46855acb-7c1d-4906-a14e-4dbf85e200a8)

## Algorithm Complexity

Detailed analysis:
Initial checks (`isinstance`, `len`) - O(1)

DataFrame copy (`df.copy()`) - O(n) where n is number of rows

Null removal in critical columns (`dropna`) - O(n) (must check each row)

Filling of null values (`fillna`):

For specific columns - O(n) per column.

For categorical columns - O(m*n) where m is the number of categorical columns

Text cleanup (`str.strip`, `str.title`) - O(n) per column of text

Gender validation (`apply` with lambda) - O(n)

Duplicate removal (`drop_duplicates`) - O(n log n) in worst case (need to sort)

Location validation (`apply` with lambda) - O(n)

Second elimination of nulls and duplicates - O(n) + O(n log n) -> `O(n log n)`






