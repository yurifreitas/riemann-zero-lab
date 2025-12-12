def gram_failures(grams, zeros):
    failures = []
    zi = 0

    for g0, g1 in zip(grams, grams[1:]):
        count = 0
        start_zi = zi

        while zi < len(zeros) and zeros[zi] < g1:
            if zeros[zi] >= g0:
                count += 1
            zi += 1

        if count != 1:
            failures.append((g0, g1, count))

    return failures
