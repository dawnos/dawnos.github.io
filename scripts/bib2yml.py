
import sys
import pybtex
import pybtex.database
import pybtex.plugin

import yaml


style = pybtex.plugin.find_plugin('pybtex.style.formatting', 'plain')()
backend = pybtex.plugin.find_plugin('pybtex.backends', 'html')()


def to_yaml(filename):

    items = []

    bibs = pybtex.database.parse_file(filename)

    for citekey in bibs.entries:
        item = {}
        entry = bibs.entries[citekey]
        item['ref'] = style.format_entry(0, entry).text.render(backend)
        item['citekey'] = citekey
        item['code'] = ''
        item['pdf'] = '%s.pdf' % citekey
        item['bib'] = entry2bibtex(citekey, entry)

        #
        # item['ref'] = item['ref'].replace("Li&nbsp;Tang", "<b>Li&nbsp;Tang</b>")
        # item['ref'] = item['ref'].replace("Li Tang", "<b>Li Tang</b>")

        items.append(item)

    return items


def entry2bibtex(citekey, entry):
    bib_data = pybtex.database.BibliographyData()
    bib_data.add_entry(citekey, entry)
    bib_data = bib_data.to_string('bibtex')
    if bib_data[-1] == '\n':
        bib_data = bib_data[:-1]
    return bib_data.replace('\n', '<br/>')



pub = [
    {
        'name': 'Journals', 
        'list': to_yaml("assets/bibs/journals.bib"),
    },
    {
        'name': 'Conferences',
        'list': to_yaml("assets/bibs/conferences.bib"),
    }
]

with open('_data/publications.yml', 'w') as f:
    yaml.dump(pub, f)