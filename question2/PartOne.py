def shape(code):
    return "Rock" if code in ("A", "X") else ("Paper" if code in ("B", "Y") else "Scissors")


def shapeScore(shape):
    return 1 if shape == 'Rock' else (2 if shape == 'Paper' else 3)


def winLoseScore(theirShape, myShape):
    if ((theirShape == 'Rock' and myShape == "Paper") or
            (theirShape == 'Paper' and myShape == 'Scissors') or
            (theirShape == 'Scissors' and myShape == 'Rock')):
        return 6

    if theirShape == myShape:
        return 3

    return 0


with open('question_data.txt') as f:
    score = 0
    for line in f:
        theirShape, myShape = [shape(s.strip()) for s in line.split(' ')]
        score += shapeScore(myShape) + winLoseScore(theirShape, myShape)

    print(score)
