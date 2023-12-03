from llama_index import PromptTemplate
import google.generativeai as palm
import os


palm.configure(api_key='AIzaSyAUPvte86iecn23zfWaZOCORwovAm7EI7U')
template = '''
you are a university professor teaching data structures and algorithms for computer science students. 

generate a problem statement/question about {subject} that is similar to leetcode problems.

defficulity: {level}
format: only output the text.
Don't give the solution
'''


promt_template = PromptTemplate(template)

def Palm_request(level,subject):
    prompt =promt_template.format(subject =subject , level =level)
    response = palm.generate_text(prompt=prompt)
    return response.result


def Solve_problem(question,lang):
    template2 = '''
        you are an profisional computer scientest know for your talent in solving algorithims problems.
        you are taske to solve the following problem in {lang} language
        Problem:
        {problem}


        think step by step

    '''
    promt_template = PromptTemplate(template2)
    prompt2 =promt_template.format(problem = question, lang = lang)
    response2 = palm.generate_text(prompt=prompt2)
    return response2.result





