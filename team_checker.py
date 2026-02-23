from pyscript import display, document

def intrams_team(e):
    document.getElementById('output').innerHTML = " "

    grade = document.getElementById('grade').value
    section = document.getElementById('section').value

    reg_yes = document.getElementById('input1').checked
    med_yes = document.getElementById('input3').checked

    if reg_yes == False:
        display(f'Please register online.', target='output')
    elif med_yes == False:
        display(f'Please get a medical certificate.', target='output')
    elif grade == "0":
        display(f'Please put your grade.', target='output')
    else:
        if section == "emerald":
            team = "Blue Bears"
        elif section == "ruby":
            team = "Red Bulldogs"
        elif section == "sapphire":
            team = "Green Hornets"
        elif section == "topaz":
            team = "Yellow Tigers"
        display(f'You are a part of the ' + team, target='output')