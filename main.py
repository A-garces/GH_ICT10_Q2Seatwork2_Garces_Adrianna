from pyscript import document, display



def grading(e):
    firname = document.getElementById('firstname').value
    lasname = document.getElementById('lastname').value

    Science = float(document.getElementById('Scigrade').value)
    Math = float(document.getElementById('Mathgrade').value)
    English = float(document.getElementById('Enggrade').value)
    Filipino = float(document.getElementById('filgrade').value)
    Ict = float(document.getElementById('ICTgrade').value)
    Pe = float(document.getElementById('PEgrade').value)
    
    grades = [Science, Math, English, Filipino, Ict, Pe]
    average = sum(grades) / len(grades)
    final = round(average, 0)

    output = document.getElementById("output")
    output.innerHTML = ""


    display(f'Name: {firname} {lasname}', target="name", append="False")

    display(f'Science: {Science}', target="output")
    display(f'Math: {Math}', target="output")
    display(f'English: {English}', target="output")
    display(f'Filipino: {Filipino}', target="output")
    display(f'ICT: {Ict}', target="output")
    display(f'PE: {Pe}', target="output")

    display(f'Average Grade: {final}', target="finalgrade", append="False")

    