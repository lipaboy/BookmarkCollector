# BookmarkCollector

## Что уже есть:

Перебирает все закладки в html формате, создаёт нужные папки по тегам < h3 > и скачивает в нужные места, создавая папку для каждой закладки. Так сделано, чтобы в дальнейшем хранить там описания в возможно хэштеги.

## Чего не хватает:

1) Описания
2) Хэштегов

### Возможная реализация

1) Описание можно хранить в текстовом файле.
2) Хэштеги можно хранить в имени файла, чтобы можно было искать в поиске операционной системы.

## Возможные проблемы

1) Главная проблема: длина имени файла. Имена закладок бывают длины, превыщающей допустимую длину имени файла в ОС. Я ограничил 100. НО: 100 для имени файла страницы и для названия папки и того 200. Т.е. всего 56 символов для пути. Возможно страницу не стоит называть тем же именем. А каким тогда?
