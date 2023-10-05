from database import *

connect() # ПОДКЛЮЧЕНИЕ БД

def main():
	print("1 - Добавить игру")
	print("2 - Поиск игры")
	print("3 - Удалить игру")
	print("4 - Изменить данные игры")
	print("5 - Список всех игр")
	while True:
		choice = input("\n\nВведите номер действия от 1 до 5: ")

		#ДОБАВЛЕНИЕ ИГРЫ
		if choice == '1':
			name = input('\n\nВведите название игры:')
			publisher = input('\nВведите издателя игры:')
			year = input('\nВведите год издания игры:')
			Games.create(name=name, publisher=publisher, year=year)
			print('\n\nДобавил игру!\n\n')
	
		#ПОИСК ИГРЫ
		elif choice =='2':
			name = input("Введите название игры для поиска: ")
			publisher = input("Введите издателя игры для поиска: ")
			year = input("Введите год издания игры для поиска: ")
			if Games.select().where(Games.name == name, Games.publisher == publisher, Games.year == year):
				print(f'\n\nНазвание: {name}, Издатель: {publisher}, Год издания: {year}')
			else:
				print('\n\nИгры по заданным параметрам не найдено!\n\n')
		
		#УДАЛЕНИЕ ИГРЫ
		elif choice == '3':
			name = input('\n\nВведите название игры:')
			publisher = input('\nВведите издателя игры:')
			year = input('\nВведите год издания игры:')
			if Games.select().where(Games.name == name, Games.publisher == publisher, Games.year == year):
				gamesInfo = Games.select().where(Games.name == name, Games.publisher == publisher, Games.year == year)[0]
				gamesInfo.delete_instance(Games.name == name)
				print('\n\nУдалил игру!\n\n')
			else:
				print('\n\nИгры по заданным параметрам не найдено!')

		#РЕДАКТИРОВАНИЕ ИГРЫ
		elif choice == '4':
			name = input('\n\nВведите название игры:')
			if Games.select().where(Games.name == name):
				newname = input('\n\nВведите новое название игры:')
				newpublisher = input('\n\nВведите нового издателя игры:')
				newyear = input('\n\nВведите новый год издания игры:')
				Games.update(name=newname, publisher=newpublisher, year=newyear).where(Games.name == name).execute()
				print('\n\nИзменил!\n\n')
			else:
				print('Игры с таким названием не найдено!')
	
		#ВЫВОД ВСЕХ ИГР
		elif choice == '5':
			for games in Games.select():
				print(f'\nНазвание: {games.name}, Издатель: {games.publisher}, Год издания: {games.year}')
		else:
			#если цифра введена не верно
			print("Номер не найден!")

if __name__ == '__main__':
	main()