class Config:
    tfidf_pipeline = 'models/ml/preprocess.sav'
    model = 'models/ml/LogisticRegression.sav'
    id_to_category = {0: 'course',
                      1: 'football',
                      2: 'basketball',
                      3: 'athletisme',
                      4: 'course-hippique',
                      5: 'equitation',
                      6: 'voile',
                      7: 'golf',
                      8: 'handball',
                      9: 'jeux-olympiques',
                      10: 'omnisport',
                      11: 'hiver',
                      12: 'tennis',
                      13: 'cyclisme',
                      14: 'boxe',
                      15: 'escrime',
                      16: 'judo',
                      17: 'volleyball',
                      }