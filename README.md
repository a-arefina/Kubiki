# Kubiki

Это игрушечный проект, который родился во время игры с детскими кубиками. 
У меня не получилось составить несколько очень простых слов одновременно и, 
покрутив эти кубики в руках, я поняла, что для слов, которые я задумала, это невозможно. 
Но процедура проверки была довольно долгой и я решила попробовать запрограммировать ее. 

## Более формальное описание

Детская игрушка кубики с буквами состоит из нескольких кубиков с нарисованными на каждой грани буквами. 
Из кубиков можно составлять слова, но не любой набор слов можно сделать из имеющихся кубиков. 
Например, если в словах некоторая буква встречается чаще, чем на кубиках, или если слова содержат 2 буквы, 
которые нарисованы на одном и том же кубике и ни на каком другом. 

Функция check_word_set в файле CheckWordSet.py проверяет, можно ли составить заданные слова из данного набора кубиков одновременно. 
Для примера работы функции можно запустить скрипт CheckWordSet.py без аргументов. 

Тестовый набор кубиков и примеры сделаны на русском языке, но проверка может быть сделана для любого языка и алфавита.

## English

Children's toy ABC blocks consists of several blocks with letters drawn on each face. 
You can make words from blocks, but not any set of words can be made from the available blocks. 
For example, if some letter occurs more often in words than in blocks, 
or if the words contain 2 letters that are present on the same block and on no other. 

check_word_set function in CheckWordSet.py checks if it is possible to make the given words from the given set of blocks. 
For an example one can run the script CheckWordSet.py with no arguments. 

The test set of cubes and examples are in Russian, but the check can be done for any language and alphabet.
