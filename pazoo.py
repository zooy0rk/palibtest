#!/usr/bin/python

import pazoolib

paz = pazoolib.PaZoo()

paz.run(server='music.zooy0rk.net')
paz.list_clients()
#paz.request_update()