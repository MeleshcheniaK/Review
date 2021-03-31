## Данная программа предназначена для генерации текста на основе цепей Маркова.
*(Цепи Маркова — это вероятности получения события на основе предыдущего события. Таким образом можно генерировать текст.)*
#### Для корректного использования добавляйте файлы с достаточным количеством слов. Для создания модели запустите файл *train.py* со следующими флагами:
>	- --input-dir - путь к директории, в которой лежит коллекция документов, не обязательный аргумент, по умолчанию stdin.
>	- --model - путь к файлу, в который сохраняется модель.
>	- --lc - Приводит тексты к lowercase, необязательный аргумент.
#### Для построения текста по уже существующей модели запустите файл *generate.py* со следующими флагами:
>	- --model - путь к файлу, из которого загружается модель.
>	- --seed - необязательный аргумент. Начальное слово. Если не указано, выбираем слово случайно из всех слов (не учитывая частоты).
>	- --length - длина генерируемой последовательности.
>	- --output - необязательный аргумент. Файл, в который будет записан результат. Если аргумент отсутствует, выводить в stdout.
Запускайте файл и наслаждайтесь результатом)
##### Пример запуска:
*Запуск примера с англоязычным корпусом*
```
git clone https://github.com/MeleshcheniaK/Review.git
cd Review
python train.py --input-dir Joker.txt --model model.txt --lc 1
python generate.py --model model.txt --seed I --length 20 --output result.txt	
```
*Запуск примера с русскоязычным корпусом*
```
git clone https://github.com/MeleshcheniaK/Review.git
cd Review
python train.py --input-dir Чужой против хищника.txt --model model.txt --lc 1
python generate.py --model model.txt --seed I --length 20 --output result.txt	
```
![Один интересный пример](https://github.com/MeleshcheniaK/Review/blob/div/Results/Example.jpg)
*Примечание: Для запуска подойдёт любой текстовый файл, примеры для русского и английского текста различаются только названиями исходников*
