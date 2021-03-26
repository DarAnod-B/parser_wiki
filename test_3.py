def appearance(intervals):
    time = []
    for k in range(0, len(intervals['pupil']), 2):
        for j in range(0, len(intervals['tutor']), 2):
            tests = {'lesson': intervals['lesson'],
                     'pupil': intervals['pupil'][k:k + 2],
                     'tutor': intervals['tutor'][j:j + 2]}
            les = range(tests['lesson'][0], tests['lesson'][1] + 1)
            pup = range(tests['pupil'][0], tests['pupil'][1] + 1)
            tut = range(tests['tutor'][0], tests['tutor'][1] + 1)
            alls = set(les).intersection(pup).intersection(tut)
            time.append(max(alls, default=0) - min(alls, default=0))
    return sum(time)
 