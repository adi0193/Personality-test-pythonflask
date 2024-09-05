from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/submit-test', methods=['POST'])
def submit_test():
    answers = request.json  
    score, personality_type =calculate_score_and_personality(answers)  
    return jsonify({'score': score, 'personality_type': personality_type})

def calculate_score_and_personality(answers):
  
    score = 0
    personality_tally = {'E': 0, 'I': 0}

    
    for questions, answer in answers.items():
        if answer == "Agree":
            score += 2
            if questions in ['1', '4']:  
                personality_tally['E'] += 1
            else:
                personality_tally['I'] += 1
        elif answer == "Neutral":
            score += 1
            
        elif answer == "Disagree":
            if questions in ['1', '4']:  
                personality_tally['I'] += 1
            else:
                personality_tally['E'] += 1

    
    personality_type = 'Extrovert' if personality_tally['E'] > personality_tally['I'] else 'Introvert'
    
    return score, personality_type


if __name__ == '__main__':
    app.run(debug=True)
