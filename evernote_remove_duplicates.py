# -*- coding: utf-8 -*-

import getpass
import pandas as pd
import evernote.edam.notestore.NoteStore as NoteStore
from evernote.api.client import EvernoteClient


def get_notebook_list(_note_store):
    notebooks = _note_store.listNotebooks()
    notebook_list = {}
    for notebook in notebooks:
        try:
            notebook_list[notebook.name] = \
                [notebook.name.split('-')[0].strip(), notebook.name.split('-')[1].strip(), notebook.guid]
        except IndexError:
            notebook_list[notebook.name] = \
                ['', notebook.name, notebook.guid]
    notebook_list = pd.DataFrame(notebook_list).T
    notebook_list.columns = ['tag', 'name', 'guid']
    notebook_list.index = range(1, len(notebook_list) + 1, 1)
    return notebook_list


def search_note(notebook, notebook_list):
    notebookguid = [item for item in notebook_list[notebook_list['name'] == notebook]['guid']][0]
    f = NoteStore.NoteFilter(notebookGuid=notebookguid)
    note_list = []
    result_spec = NoteStore.NotesMetadataResultSpec(includeTitle=True)
    for _note in noteStore.findNotesMetadata(
            token, f, 0, 999, result_spec).notes:
        note_list.append(_note)
    return note_list


def get_note_list(notebook_list, para=None):
    note_dict = []
    trans = notebook_list['name']
    if para is not None:
        trans = [para]
    count = 1
    for item in trans:
        note = search_note(item, notebooklist)
        for item2 in note:
            note_dict.append([item2.title, item2.guid])
        count += 1
        if count % 5 == 0:
            print('已统计 {} 个笔记本'.format(count))
    note_dict = pd.DataFrame(note_dict, columns=['name', 'guid'])
    note_dict.sort_values(by='name', inplace=True)
    return note_dict


def writer_to_excel(data, filename):
    write = pd.ExcelWriter(address + r'\{}.xlsx'.format(filename))
    data.to_excel(write, sheet_name=filename)
    write.save()
    write.close()


# 参数

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
address = r'C:\Users\{}\Desktop'.format(getpass.getuser())
token = '填入你的 token'
check = None

# 连接印象笔记

client = EvernoteClient(token=token, sandbox=False, china=True)
userStore = client.get_user_store()
noteStore = client.get_note_store()

# 正文

notebooklist = get_notebook_list(noteStore)
notelist = get_note_list(notebooklist, para=check)
writer_to_excel(notelist, '印象笔记')

# 查找与删除重复项

after = []
drop_list = []
for i, v in notelist.iterrows():
    if notelist.loc[i]['name'] not in after:
        after.append(notelist.loc[i]['name'])
    else:
        print(v['name'])
        drop_list.append(v['guid'])
for i in drop_list:
    noteStore.deleteNote(token, i)
