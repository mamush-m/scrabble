def scrabbleScore(word):
    if not word or len(word) == 0:
        return 'Please input a valid word'
    
    search_word = word.upper()
    total_score = 0
    letter_scores = {
        '1_point': {
            'point_value': 1,
            'letters': ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U']
        },
        
        '2_point': {
            'point_value': 2,
            'letters': ['D', 'G']
        },
        
        '3_point': {
            'point_value': 3,
            'letters': ['B', 'C', 'M', 'P']
        },
        
        '4_point': {
            'point_value': 4,
            'letters': ['F', 'H', 'V', 'W', 'Y']
        },
        
        '5_point': {
            'point_value': 5,
            'letters': ['K']
        },
        
        '8_point': {
            'point_value': 8,
            'letters': ['J', 'X']
        },
        
        '10_point': {
            'point_value': 10,
            'letters': ['Q', 'Z']
        }
    }
    
    
    
    
    
scrabbleScore('FIZZBUZZ')
scrabbleScore('')