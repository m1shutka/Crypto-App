import flet as ft
from manager import Manager

def main(page: ft.Page):

    #Процедура регистрации пользователя
    def register(e):

        if len(user_pass_reg.value) > 30 or len(user_pass_reg.value) < 10:
            page.snack_bar = ft.SnackBar(ft.Text('Длина пароля должан быть не менее 10 и не более 30 символов!'))
            page.snack_bar.open = True

        else:
            message = mng.user_registration(user_login_reg.value, user_pass_reg.value, product_key.value)

            if message == 'Зарегестрировано':
                product_key.value = ''
                user_login_reg.value = ''
                page.snack_bar = ft.SnackBar(ft.Text(message))
                page.snack_bar.open = True

            elif message == 'Неверный ключ продукта!':
                product_key.value = ''
                page.snack_bar = ft.SnackBar(ft.Text(message))
                page.snack_bar.open = True

            elif message == 'Пользователь с таким логином уже существует!':
                user_login_reg.value = ''
                page.snack_bar = ft.SnackBar(ft.Text(message))
                page.snack_bar.open = True

            else:
                user_login_reg.value = ''
                product_key.value = ''
                page.snack_bar = ft.SnackBar(ft.Text('Что-то пошло не так...'))
                page.snack_bar.open = True

        user_pass_reg.value = ''
        btn_reg.disabled = True
        page.update()


    #Процедура авторизации пользователя
    def autorization(e):

        message = mng.user_autorization(user_login_auto.value, user_pass_auto.value)

        if message == 'Вход успешен':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

            if mng.userLogin() != None:
                page.navigation_bar.destinations.clear()
                user_login_acc.value = f'Пользователь: {mng.userLogin()}'

                if mng.isUserAdmin():
                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.VERIFIED_USER,
                            label='Учетная запись',
                            selected_icon=ft.icons.VERIFIED_USER_OUTLINED
                    ))

                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.BOOK,
                            label='Товары',
                            selected_icon=ft.icons.BOOK_OUTLINED
                    ))

                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.BOOKMARK_ADD,
                            label='Добавить товар',
                            selected_icon=ft.icons.BOOKMARK_ADD_OUTLINED
                    ))

                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.BOOKMARK_REMOVE,
                            label='Удалить товар',
                            selected_icon=ft.icons.BOOKMARK_REMOVE_OUTLINED
                    ))

                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.SUPERVISED_USER_CIRCLE_ROUNDED,
                            label='Изменить права',
                            selected_icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED
                    ))

                else:
                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.VERIFIED_USER,
                            label='Учетная запись',
                            selected_icon=ft.icons.VERIFIED_USER_OUTLINED
                    ))

                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.BOOK,
                            label='Товары',
                            selected_icon=ft.icons.BOOK_OUTLINED
                    ))

                    page.navigation_bar.destinations.append(ft.NavigationDestination(
                            icon=ft.icons.BOOKMARK_ADD,
                            label='Добавить товар',
                            selected_icon=ft.icons.BOOKMARK_ADD_OUTLINED
                    ))

                page.navigation_bar.selected_index = 0

                page.clean()
                page.add(account_form)

            else:
                page.snack_bar = ft.SnackBar(ft.Text('Что-то пошло не так...'))
                page.snack_bar.open = True

        elif message == 'Неверный логин или пароль!':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        elif message == 'Пользователя с таким логином не существует!':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        else:
            page.snack_bar = ft.SnackBar(ft.Text('Что-то пошло не так...'))
            page.snack_bar.open = True

        user_login_auto.value = ''
        user_pass_auto.value = ''
        btn_auto.disabled = True
        page.update()


    #Команда добавления товара
    def add_item(e):
        
        message = mng.add_item(item_name_add.value, item_price_add.value)

        if message == 'Товар успешно добавлен!':
            item_price_add.value = ''
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        elif message == 'Товар с таким названием уже существует!':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        else:
            item_price_add.value = ''
            page.snack_bar = ft.SnackBar(ft.Text('Что-то пошло не так...'))
            page.snack_bar.open = True

        item_name_add.value = ''
        btn_add.disabled = True
        page.update()


    #Команда удаления товара
    def delete_item(e):

        message = mng.delete_item(item_name_del.value)

        if message == 'Товар успешно удален!':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        elif message == 'Товара с таким названием не существует!':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        else:
            page.snack_bar = ft.SnackBar(ft.Text('Что-то пошло не так...'))
            page.snack_bar.open = True

        item_name_del.value = ''
        btn_del.disabled = True
        page.update()


    #Команда выхода из учетной записи
    def quit(e):

        mng.quit()
        items_list.clear()

        page.snack_bar = ft.SnackBar(ft.Text('Выход произведен'))
        page.snack_bar.open = True
        user_login_acc.value = f'Пользователь: {mng.userLogin()}'
        page.clean()
        page.add(autorization_form)

        page.navigation_bar.destinations.clear()
        page.navigation_bar.destinations.append(ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label='Регистрация'))
        page.navigation_bar.destinations.append(ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label='Авторизация'))
        page.navigation_bar.selected_index = 1

        page.update()
        

    #Команда изменения прав доступа пользователя
    def sudo_user(e):
        
        message = mng.sudo(user_login_sudo.value)

        if message == f'Поздравляем {user_login_sudo.value} с повышением!':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        elif message == 'Он уже админ... куда еще выше?':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        elif message == 'Пользователя с таким логином не существует!':
            page.snack_bar = ft.SnackBar(ft.Text(message))
            page.snack_bar.open = True

        else:
            page.snack_bar = ft.SnackBar(ft.Text('Что-то пошло не так...'))
            page.snack_bar.open = True

        user_login_sudo.value = ''
        btn_sudo.disabled = True
        page.update()


    #Верификация полей формы регистрации
    def validate_reg(e):

        if len(user_login_reg.value) > 30:
            page.snack_bar = ft.SnackBar(ft.Text('Длина логина должна быть не более 30 символов!'))
            page.snack_bar.open = True

        if len(user_login_reg.value) > 30 or len(user_login_reg.value) > 30:
            page.snack_bar = ft.SnackBar(ft.Text('Длина вводимого логина/пароля должна быть не более 30 символов!'))
            page.snack_bar.open = True

        if (0 < len(user_login_reg.value) <= 30) and (0 < len(user_pass_reg.value) <= 30) and (len(product_key.value) == 10):
            btn_reg.disabled = False

        else:
            btn_reg.disabled = True
            

        page.update()


    #Верификация полей формы авторизации
    def validate_auto(e):

        if len(user_login_auto.value) > 30 or len(user_login_auto.value) > 30:
            page.snack_bar = ft.SnackBar(ft.Text('Длина вводимого логина/пароля должна быть не более 30 символов!'))
            page.snack_bar.open = True

        if (0 < len(user_login_auto.value) <= 30) and (0 < len(user_pass_auto.value) <= 30):
            btn_auto.disabled = False

        else:
            btn_auto.disabled = True

        page.update()

    
    #Верификация полей формы добавления товара
    def validate_add(e):

        if len(item_name_add.value) > 50:
           page.snack_bar = ft.SnackBar(ft.Text('Длина наименования товара должна быть не более 50 символов!'))
           page.snack_bar.open = True

        if len(item_price_add.value) > 10:
           page.snack_bar = ft.SnackBar(ft.Text('Длина вводимого цены товара должна быть не более 10 символов!'))
           page.snack_bar.open = True

        if (0 < len(item_name_add.value) <= 50) and (0 < len(item_price_add.value) <= 10):
            btn_add.disabled = False

        else:
            btn_add.disabled = True

        if len(item_price_add.value) > 0:
            try:
                int(item_price_add.value)
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.Text('Недопустимы символ в поле цена!'))
                page.snack_bar.open = True
                btn_add.disabled = True

        page.update()

    #Верификация полей формы удаления товара
    def validate_del(e):

        if len(item_name_del.value) > 50:
           page.snack_bar = ft.SnackBar(ft.Text('Длина наименования товара должна быть не более 50 символов!'))
           page.snack_bar.open = True

        if (0 < len(item_name_del.value) <= 50):
            btn_del.disabled = False

        else:
            btn_del.disabled = True

        page.update()


    #Верификация полей формы изменения прав доступа
    def validate_sudo(e):

        if len(user_login_sudo.value) > 30:
            page.snack_bar = ft.SnackBar(ft.Text('Длина логина должна быть не более 30 символов!'))
            page.snack_bar.open = True

        if (0 < len(user_login_sudo.value) <= 30):
            btn_sudo.disabled = False

        else:
            btn_sudo.disabled = True

        page.update()


    #Обработка команд навигации
    def navigate(e):

        page_index = page.navigation_bar.selected_index
        page.clean()
        items_list.clear()

        if mng.userLogin() == None:
            if page_index == 0:
                page.add(register_form)

            elif page_index == 1:
                page.add(autorization_form)

        else:
            if page_index == 0:
                page.add(account_form)

            elif page_index == 1:
                items = mng.get_items_list()

                for i in items:
                    items_list.append(ft.Container(
                        content=ft.Text(i, color=ft.colors.ON_PRIMARY),
                        alignment=ft.alignment.center,
                        width=300,
                        height=50,
                        border_radius=5,
                        bgcolor=ft.colors.PRIMARY
                    ))

                page.theme = ft.Theme(
                    scrollbar_theme=ft.ScrollbarTheme(
                        track_visibility=True,
                        thickness=10,
                        main_axis_margin=5,
                        cross_axis_margin=5
                    )
                )

                page.add(view_form)

            elif page_index == 2:
                page.add(add_form)

            elif page_index == 3:
                page.add(delete_form)

            elif page_index == 4:
                page.add(sudo_form)

        page.update()

    #Настройки окна
    page.title = 'CryptoApp'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False

    #Виджеты формы регистрации
    user_login_reg = ft.TextField(label='Логин', width=200, on_change=validate_reg)
    user_pass_reg = ft.TextField(label='Пароль', password=True, width=200, on_change=validate_reg)
    product_key = ft.TextField(label='Ключ продукта', width=200, on_change=validate_reg)
    btn_reg = ft.OutlinedButton(text='Зарегестрироваться', width=200, on_click=register, disabled = True)

    #Виджеты формы аунтефикации
    user_login_auto = ft.TextField(label='Логин', width=200, on_change=validate_auto)
    user_pass_auto = ft.TextField(label='Пароль', password=True, width=200, on_change=validate_auto)
    btn_auto = ft.OutlinedButton(text='Войти', width=200, on_click=autorization, disabled = True)

    #Виджеты формы добавления товара
    item_name_add = ft.TextField(label='Название', width=200, on_change=validate_add)
    item_price_add = ft.TextField(label='Цена', password=False, width=200, on_change=validate_add)
    btn_add = ft.OutlinedButton(text='Добавить', width=200, on_click=add_item, disabled = True)

    #Виджеты формы удаления товара
    item_name_del = ft.TextField(label='Название', width=200, on_change=validate_del)
    btn_del = ft.OutlinedButton(text='Удалить', width=200, on_click=delete_item, disabled = True)

    #Список товаров
    items_list = []

    #Виджеты формы изменения прав доступа
    user_login_sudo = ft.TextField(label='Логин пользователя', width=200, on_change=validate_sudo)
    btn_sudo = ft.OutlinedButton(text='Изменить', width=200, on_click=sudo_user, disabled = True)

    #Объект класса для работы с бд
    mng = Manager()

    #Виджеты формы учетной записи
    user_login_acc = ft.Text(f'Пользователь: {mng.userLogin()}')
    btn_quit = ft.OutlinedButton(text='Выйти', width=200, on_click=quit, disabled = False)

    #Панель навигации
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label='Регистрация'),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label='Авторизация')
        ], 
        on_change=navigate,
        selected_index = 1
    )

    #Форма регистрации
    register_form = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Регистрация'),
                    user_login_reg,
                    user_pass_reg,
                    product_key,
                    btn_reg
                ]
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Форма авторизации
    autorization_form = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Авторизация'),
                    user_login_auto,
                    user_pass_auto,
                    btn_auto
                ]
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Форма учетной записи
    account_form = ft.Row(
        [
            ft.Column(
                [
                    user_login_acc,
                    btn_quit
                ]
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Форма просмотра товаров
    view_form = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Список товаров'),
                    ft.Container(
                        content=ft.Column(
                            items_list,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            scroll=ft.ScrollMode.ALWAYS, 
                            height=300
                        ),
                        bgcolor=ft.colors.PRIMARY_CONTAINER,
                        width=400,
                        border_radius=5
                    )
                ]
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Форма добавления товаров
    add_form = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Добавить товар'),
                    item_name_add,
                    item_price_add,
                    btn_add
                ]
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Форма удаления товаров
    delete_form = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Удалить товар'),
                    item_name_del,
                    btn_del
                ]
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Форма изменения прав доступа
    sudo_form = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Изменить права доступа'),
                    user_login_sudo,
                    btn_sudo
                ]
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Загружаем начальную страницу
    page.add(
       autorization_form
    )

ft.app(target=main, view=ft.AppView.FLET_APP)