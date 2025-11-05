from pyscript import display, document

def general_weighted_average(e):
    document.getElementById('student_info').innerHTML = ''
    document.getElementById('summary').innerHTML = ''
    document.getElementById('output').innerHTML = ''

    subjects = ['Astronomy', 'Charms', 'Defence', 'Herbology', 'Potions', 'Transfiguration']
    units_subject = (5, 4, 3, 2, 1, 1)

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    astronomy = float(document.getElementById('astronomy').value)
    charms = float(document.getElementById('charms').value)
    defence = float(document.getElementById('defence').value)
    herbology = float(document.getElementById('herbology').value)
    potions = float(document.getElementById('potions').value)
    transfiguration = float(document.getElementById('transfiguration').value)

    weighted_sum = (
        astronomy * units_subject[0] + 
        charms * units_subject[1] + 
        defence * units_subject[2] + 
        herbology * units_subject[3] + 
        potions * units_subject[4] + 
        transfiguration * units_subject[5]
    )

    total_units = sum(units_subject)
    gwa = weighted_sum / total_units

    summary = (
        f"{subjects[0]}: {astronomy:.0f}\n"
        f"{subjects[1]}: {charms:.0f}\n"
        f"{subjects[2]}: {defence:.0f}\n"
        f"{subjects[3]}: {herbology:.0f}\n"
        f"{subjects[4]}: {potions:.0f}\n"
        f"{subjects[5]}: {transfiguration:.0f}"
    )

    display(f"Name: {first_name} {last_name}", target="student_info")
    display(summary, target="summary")
    display(f"Your Fate is {gwa:.2f}", target="output")
