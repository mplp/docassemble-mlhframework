def strip_end_punctuation(text, punctuation_marks=None):
    """Removes any punctuation marks from the end of the text."""
    if text is None or not isinstance(text, str):
        return text
        
    if punctuation_marks is None:
        punctuation_marks = ['.', ',', '?', '!', ':', ';']
    
    if not isinstance(punctuation_marks, list):
        punctuation_marks = list(punctuation_marks)
    
    text = text.rstrip()
    
    while text and any(text.endswith(mark) for mark in punctuation_marks):
        for mark in punctuation_marks:
            if text.endswith(mark):
                text = text[:-len(mark)]
                text = text.rstrip()
                break
                
    return text