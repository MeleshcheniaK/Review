## Данная программа предназначена для генерации текста на основе цепей Маркова.
[*Кратко о генерации текстов на цепях Маркова*](https://tproger.ru/translations/markov-chains/)

При генерации текстов данным способом после обучения на модели вы будете иметь возможность создать необходимое количество текста с помощью учёта вероятностей для пар слов.
#### Для создания модели запустите файл *train.py* со следующими флагами:
>	- --input-dir - путь к директории, в которой лежит коллекция документов(*текстовых файлов*), не обязательный аргумент, по умолчанию stdin.(*Для корректного использования добавляйте файлы с достаточным количеством слов*)
>	- --model - путь к файлу, в который сохраняется модель.
>	- --lc - Приводит тексты к lowercase, необязательный аргумент.
>	- --ngram - Строит модель на основе n-грамм, необязательный фргумент.
#### Для построения текста по уже существующей модели запустите файл *generate.py* со следующими флагами:
>	- --model - путь к файлу, из которого загружается модель.
>	- --seed - необязательный аргумент. Начальное слово. Если не указано, выбираем слово случайно из всех слов (не учитывая частоты).
>	- --length - длина генерируемой последовательности.
>	- --output - необязательный аргумент. Файл, в который будет записан результат. Если аргумент отсутствует, выводить в stdout.

*Запуск примера с англоязычным корпусом:*
```
git clone https://github.com/MeleshcheniaK/Review.git
cd Review
python train.py --input-dir Sources/Joker.txt --model model.txt --lc 1
python generate.py --model model.txt --seed I --length 20 --output result.txt	
```
*Запуск примера с русскоязычным корпусом:*
```
git clone https://github.com/MeleshcheniaK/Review.git
cd Review
python train.py --input-dir Sources/Alien_vs_Predator.txt --model model.txt --lc 1 --ngram 1
python generate.py --model model.txt --length 20 --output result.txt	
```
*Результат:*
```
Высокотехнологичный женский комбинезон мечта фетешиста.
```
*Примечание: Для запуска подойдёт любой текстовый файл, примеры для русского и английского текста различаются только названиями исходных файлов*
## Данная программа предназначена для генерации текста на основе цепей Маркова.
[*Кратко о генерации текстов на цепях Маркова*](https://tproger.ru/translations/markov-chains/)

При генерации текстов данным способом после обучения на модели вы будете иметь возможность создать необходимое количество текста с помощью учёта вероятностей для пар слов.
#### Для создания модели запустите файл *train.py* со следующими флагами:
>	- --input-dir - путь к директории, в которой лежит коллекция документов(*текстовых файлов*), не обязательный аргумент, по умолчанию stdin.(*Для корректного использования добавляйте файлы с достаточным количеством слов*)
>	- --model - путь к файлу, в который сохраняется модель.
>	- --lc - Приводит тексты к lowercase, необязательный аргумент.
#### Для построения текста по уже существующей модели запустите файл *generate.py* со следующими флагами:
>	- --model - путь к файлу, из которого загружается модель.
>	- --seed - необязательный аргумент. Начальное слово. Если не указано, выбираем слово случайно из всех слов (не учитывая частоты).
>	- --length - длина генерируемой последовательности.
>	- --output - необязательный аргумент. Файл, в который будет записан результат. Если аргумент отсутствует, выводить в stdout.

*Запуск примера с англоязычным корпусом:*
```
git clone https://github.com/MeleshcheniaK/Review.git
cd Review
python train.py --input-dir Examples/Joker.txt --model model.txt --lc 1
python generate.py --model model.txt --seed I --length 20 --output result.txt	
```
*Запуск примера с русскоязычным корпусом:*
```
git clone https://github.com/MeleshcheniaK/Review.git
cd Review
python train.py --input-dir Examples/Alien vs Predator.txt --model model.txt --lc 1
python generate.py --model model.txt --length 20 --output result.txt	
```
*Результат:*
```
Высокотехнологичный женский комбинезон мечта фетешиста.
```
*Примечание: Для запуска подойдёт любой текстовый файл, примеры для русского и английского текста различаются только названиями исходных файлов*