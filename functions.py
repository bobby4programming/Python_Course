
samples = ['ariana', 'grande', 'sleek247', 'amaka', 'disappointment']

def count_str(samples):
    "This function  counts string greater than 0r equal to 2 with same first and last letter"
    count = 0
    if isinstance(samples, list):
        if not samples:
            return count
        for sample in samples:
            if len(sample) >= 2 and (sample[0] == sample[-1]):
                count += 1
                return count
count_str(samples)
