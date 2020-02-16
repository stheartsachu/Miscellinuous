scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
def fun():
    max_element = scores[0]
    min_element = scores[0]
    max_count = 0
    min_count = 0
    for score in scores:
        if score > max_element:
            max_element = score
            max_count += 1
        if score < min_element:
            min_element = score
            min_count += 1
        return print([max_count, min_count])
fun()
