#Основная функция, которая запускает парсер.
from parser import get_user_ratings, save_data_to_excel

def main():
    #В случае, если мы хотим чтобы польсователь сам вводил свой id всегда, можно удалить знак решётки в user_id на 6 строчке,и добавить его на 7 строчку (и наоборот если хотим вернуть проворачиваем схему в обратном порядке).
    #user_id = input('Введите user_id пользователя, оценки которого хотите увидеть: ')
    user_id = "23721363"
    user_ratings = get_user_ratings(user_id)
    save_data_to_excel(user_ratings, 'user_ratings.xlsx')
    print("Данные записаны в файл Excel.")

if __name__ == "__main__":
    main()

