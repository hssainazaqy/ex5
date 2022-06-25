import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    return_list = []
    with open(input_json_path) as f:
        data = json.load(f)
    for id,student in data.items():
        if course_name in student['registered_courses']:
            return_list.append(student['student_name'])

    return return_list


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path) as f:
        data = json.load(f)
    new_dict = {}
    for k in data.keys():
        for course_name in data[k]['registered_courses']:
            if course_name in new_dict.keys():
                new_dict[course_name] = new_dict[course_name] + 1
            else:
                new_dict[course_name] = 1
    with open(output_file_path, 'w') as g:

        for course_name in sorted(new_dict):
            g.write('"')
            g.write(course_name)
            g.write('"')
            g.write(" ")
            g.write(str(new_dict[course_name]))
            g.write('\n')




def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    lecturers_dict = {}
    directory = json_directory_path

    for filename in os.listdir(directory):
        curr_file_path = os.path.join(directory, filename)
        if os.path.isfile(curr_file_path):
            if curr_file_path.endswith('json'):
                with open(curr_file_path) as f_path :

                    data = json.load(f_path)
                    for course_id in data.keys():

                        for lecturer in data[course_id]['lecturers']:

                            if lecturer in lecturers_dict.keys():
                                if data[course_id]['course_name'] not in lecturers_dict[lecturer]:
                                    lecturers_dict[lecturer].append(data[course_id]['course_name'])
                            else:
                                lecturers_dict[lecturer] = [data[course_id]['course_name']]


    with open(output_json_path,'w') as outPath:
        json.dump(lecturers_dict,outPath,indent=4)