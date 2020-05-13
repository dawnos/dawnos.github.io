
import sys
import pybtex
import pybtex.database
import pybtex.plugin

import yaml


style = pybtex.plugin.find_plugin('pybtex.style.formatting', 'plain')()
backend = pybtex.plugin.find_plugin('pybtex.backends', 'html')()


def get_priority(entry):
    first_name_of_first_author = entry.persons['author'][0].first_names
    last_name_of_first_author = entry.persons['author'][0].last_names
    if len(first_name_of_first_author) == 1 and first_name_of_first_author[0] == 'Li' and \
       len(last_name_of_first_author) == 1 and last_name_of_first_author[0] == 'Tang':
        return 0
    else:
        return 1


def to_yaml(filename, n_select=3):

    items = []
    bibs = pybtex.database.parse_file(filename)
    priorities = [get_priority(bibs.entries[k]) for k in bibs.entries]
    sorted_priorities_index = sorted(range(len(priorities)),key=priorities.__getitem__)
    is_selected = [False, ] * len(priorities)
    for i in range(min(n_select, len(priorities))):
        is_selected[sorted_priorities_index[i]] = True

    for idx, citekey in enumerate(bibs.entries):
        item = {}
        entry = bibs.entries[citekey]
        item['ref'] = style.format_entry(0, entry).text.render(backend)
        item['citekey'] = citekey
        item['code'] = entry.fields['code'] if 'code' in entry.fields else ''
        item['pdf'] = '%s.pdf' % citekey
        item['bib'] = entry2bibtex(citekey, entry)
        item['selected'] = True if is_selected[idx] else False

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
