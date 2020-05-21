def solution(genres, plays):
    answer = []
    playsDict = {}
    playsIndexDict = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playsDict[genre] = playsDict.get(genre, 0) + play
        playsIndexDict[genre] = playsIndexDict.get(genre, []) + [(play, i)]
        
    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    print(playsIndexDict)
    for (genre, total) in genreSort:
        playsIndexDict[genre] = sorted(playsIndexDict[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in playsIndexDict[genre][:2]]

    return answer