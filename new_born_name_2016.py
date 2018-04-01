from flask import Flask, abort, request
from get_newborn_names import get_new_born_names


app = Flask(__name__)

@app.route('/names')

def names_in_year():
    
    url = 'https://apidata.mos.ru/v1/datasets/2009/rows?api_key=c2d33ae9cb563b3664b30f55149e1934&'
    newborn_names = get_new_born_names(url)
    year = request.args.get('year')
    table_str = '''<table>
            <tr>
                <th>Год рождения</th>
                <th>Месяц рождения</th>
                <th>Количество детей</th>
                <th>Имя ребенка</th>
            </tr>'''
    for items in newborn_names:
        names = items.get('Cells')
        if year in names.values():
            table_str = table_str + '''
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>''' % (names['Year'], names['Month'], names['NumberOfPersons'], names['Name'])
    table_str += '</table>'
    return table_str

if __name__ == '__main__':
    app.run()
