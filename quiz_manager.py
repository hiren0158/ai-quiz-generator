# File: quiz_manager.py
"""
Manages quiz state and scoring logic
"""


class QuizManager:
    """Manages quiz state and operations"""
    
    @staticmethod
    def calculate_score(quiz_data, user_answers):
        """Calculate the quiz score"""
        correct = 0
        total = len(quiz_data)
        
        for idx, question_data in enumerate(quiz_data):
            user_answer = user_answers.get(idx)
            if user_answer == question_data['correct_answer']:
                correct += 1
        
        return correct, total
    
    @staticmethod
    def get_score_message(percentage):
        """Get encouraging message based on score"""
        if percentage == 100:
            return "🏆 Perfect Score! Outstanding!"
        elif percentage >= 80:
            return "🌟 Great Job!"
        elif percentage >= 60:
            return "👍 Good Effort!"
        else:
            return "📚 Keep Learning!"
