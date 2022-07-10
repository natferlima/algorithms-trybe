def study_schedule(permanence_period, target_time):
    num_students = 0
    try:
        for entry, exit in permanence_period:
            if target_time >= entry and target_time <= exit:
                num_students += 1
    except TypeError:
        return None
    return num_students
