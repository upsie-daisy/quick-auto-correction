##################
#
# A Stupid Script to Correct Words in your Python Code
#
# github.com/upsie-daisy/quick-auto-correction
# Made by @Upsie-Daisy
#
#################

def auto_correction(wrong, correct):
    correction = ""
    points = []
    for word in correct: 
        points.append(-0.7 * abs(len(word) - len(wrong)))
    
    for i in range(len(correct)):
        word = correct[i]
        
        if word.lower() == wrong.lower():
            points[i] += 100
        
        for j in range(len(wrong)):
            if len(word) > j:
                if wrong[j] != word[j]:
                    points[i] -= 1
                    
        for lettera in wrong:
            for letterb in word:
                if lettera == letterb:
                    points[i] += 1

    maximum = points[0]
    correction = correct[0]
    for i in range(len(correct)):
        if points[i] > maximum:
            maximum = points[i]
            correction = correct[i]   

    return correction