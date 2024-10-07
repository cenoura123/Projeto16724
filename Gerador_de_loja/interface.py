import flet as ft
import time
from functions import Verificar_se_nome_existe,Criar_Arquivo_Base_Shop,Criar_Conta,Criar_lojas,Som,Verificar_Version,Nomes_lojas,Enter_Cont

def Main(page:ft.Page):
    page.title="Gerador de Loja"
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    
    

    def Create_Acount(e):
        nome = Login_User.value
        senha = Login_password.value
        c_senha = Create_Acount_Con_Password.value
        verificacao_name = Verificar_se_nome_existe(nome)

        if nome:
            if senha and c_senha:
                if verificacao_name:
                    if senha == c_senha:
                        Criar_Conta(nome, c_senha)
                        Som("_internal/sucess.mp3")
                        Tela_Sucess()
                        time.sleep(4)
                        Sucess_Back()
                    else:
                        Info_create.value = "* Senhas não iguais"
                        Info_create.update()
                else:
                    Info_create.value = "* Nome ja existente por favor escolha outro"
                    Info_create.update()
            else:
                Info_create.value="* Campos não preenchidos"
                Info_create.update()
        else:
            Info_create.value="* Campos não preenchidos"
            Info_create.update()
    
    def Enter(e):
        senha = Login_password.value
        senha_c = Enter_Cont(Login_User.value)
        if senha == False:
            Info_create.value="* Usuário não encontrado"
            Info_create.update()
        else:
            if senha:
                if senha == senha_c:
                    Nome = Login_User.value
                    Som("_internal/sucess.mp3")
                    Entrar_Main(Nome)
                    time.sleep(.2)
                    Btn_Main_Home.selected = True
                    Conteudo_de_Pagina_Main.content = Tela_Inicio_
                    Conteudo_de_Pagina_Main.offset.x = 0
                    time.sleep(.1)
                    Conteudo_de_Pagina_Main.update()
                else:
                    Info_create.value="* Usuário ou senhas incorretos"
                    Info_create.update()
            else:
                Info_create.value="* Campos não preenchidos"
                Info_create.update()
    
    def Creat_Shops(e):
        if Cria_Loja_Text_field.value:
            Nome_Loja = Cria_Loja_Text_field.value
            Criar_Arquivo_Base_Shop()
            Criar_lojas(Nome_Loja)
            Som("_internal/sucess.mp3")
            Conteudo_de_Pagina_Main.offset.x = 2
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Conteudo_de_Pagina_Main.content = Tela_Sucess_Creat_Shop
            Conteudo_de_Pagina_Main.offset.x = 0
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            time.sleep(1)
            Image_sucess_creat_shop.opacity = 1
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
        else:
            Info_create.value="* Nome não digitado"
            Info_create.update()

    
    def Tela_Config(e):
        if Btn_Main_Home.selected:
            Conteudo_de_Pagina_Main.offset.x = 2
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Conteudo_de_Pagina_Main.content = Tela_Config_
            Btn_Main_Home.selected = False
            time.sleep(.1)
            Side_menu_Main.update()
            time.sleep(.3)
            Conteudo_de_Pagina_Main.offset.x = 0
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            time.sleep(.1)
            Btn_Main_Settings.selected = True

        elif Btn_Main_Settings.selected:
            pass
        
        else:
            Conteudo_de_Pagina_Main.offset.x = 2
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Conteudo_de_Pagina_Main.content = Tela_Config_
            Conteudo_de_Pagina_Main.offset.x = 0
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Btn_Main_Settings.selected = True
            
        
    
    def Tela_Home_Main(e):
        if Btn_Main_Settings.selected:
            Conteudo_de_Pagina_Main.offset.x = 2
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Conteudo_de_Pagina_Main.content = Tela_Inicio_
            Btn_Main_Settings.selected = False
            time.sleep(.3)
            Conteudo_de_Pagina_Main.offset.x = 0
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Btn_Main_Home.selected = True
        
        elif Btn_Main_Home.selected:
            ...
        else:
            Conteudo_de_Pagina_Main.offset.x = 2
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Conteudo_de_Pagina_Main.content = Tela_Inicio_
            Conteudo_de_Pagina_Main.offset.x = 0
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()
            Btn_Main_Home.selected = True

            
    def Animete_Enter_Creat_Shop(e):
        if Btn_Main_Home.selected:
            Conteudo_de_Pagina_Main.offset.x = 2
            time.sleep(.2)
            Btn_Main_Home.selected = False
            Conteudo_de_Pagina_Main.update()
            Conteudo_de_Pagina_Main.content = Tela_Cria_Loja
            Conteudo_de_Pagina_Main.offset.x = 0
            time.sleep(.2)
            Conteudo_de_Pagina_Main.update()

    def Animete_Side_menu(e):
        mouse = False
        while mouse == False:
            Side_menu_Main.offset.x = 0
            Btn_Main_Home.offset.x = 0
            Btn_Main_Settings.offset.x = 0
            Btn_Main_Exit.offset.x = 0
            Text_Main_Home.opacity = 1
            Text_Main_Settings.opacity = 1
            Text_Main_Exit.opacity = 1
            
            Side_menu_Main.update()
            time.sleep(3)
            mouse=True
        while mouse:
            Side_menu_Main.offset.x = -.6
            Btn_Main_Home.offset.x = 2.3
            Btn_Main_Settings.offset.x = 2.3
            Btn_Main_Exit.offset.x = 2.3
            Text_Main_Home.opacity = 0
            Text_Main_Settings.opacity = 0
            Text_Main_Exit.opacity = 0
            Side_menu_Main.update()
            time.sleep(.1)
            mouse=False
    
    def Entrar_Main(nome):
        page.remove(Container)
        page.add(Container_Main)
        Text_Main.value = f"Olá {nome}"
        Text_Main.update()
        page.update()
    
    def Main_Back_Login(e):
        page.remove(Container_Main)
        page.add(Container)
        page.update()

    def Tela_Sucess(e=None):
        page.remove(Container2)
        page.add(Sucess)
        page.update()
    
    def Sucess_Back(e=None):
        page.remove(Sucess)
        page.add(Container)
        page.update()

    def Enter_C_Acount(e):
        page.remove(Container)
        page.add(Container2)
        page.update()
    
    def Back_Login(e):
        page.remove(Container2)
        page.add(Container)
        page.update()
    
    
    def Animate_sucess(e=None):
        mouse = True
        while mouse:
            image_sucess.offset.y=-0.8
            image_sucess.update()
            time.sleep(.5)
            mouse = False
        while mouse == False:
            image_sucess.offset.y=0
            image_sucess.update()
            time.sleep(.5)
            mouse = True

            

    Login_User = ft.TextField(
        width=319,
        height=115,
        color=ft.colors.WHITE,
        hint_text="Digite seu Nome",
        prefix_icon=ft.icons.PERSON,
        hint_style=ft.TextStyle(
            color=ft.colors.WHITE
        ),
        border_color=ft.colors.WHITE,
        border_radius=15
    )

    Login_password = ft.TextField(
        width=319,
        height=115,
        color=ft.colors.WHITE,
        hint_text="Digite sua Senha",
        prefix_icon=ft.icons.LOCK,
        password=True,
        hint_style=ft.TextStyle(
            color=ft.colors.WHITE
        ),
        border_color=ft.colors.WHITE,
        border_radius=15,
    )

    Create_Acount_Con_Password = ft.TextField(
        width=319,
        height=115,
        color=ft.colors.WHITE,
        hint_text="Confirme sua Senha",
        prefix_icon=ft.icons.LOCK,
        password=True,
        hint_style=ft.TextStyle(
            color=ft.colors.WHITE
        ),
        border_color=ft.colors.WHITE,
        border_radius=15,
    )

    Login_txt = ft.Text(
                value="Login",
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
                size=45
            )

    Creat_txt = ft.Text(
                value="Register",
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
                size=45
            )

    Info_create = ft.Text(
                value="",
                color=ft.colors.RED,
                weight=ft.FontWeight.BOLD,
                size=16
            )

    Login_btn_Enter = ft.ElevatedButton(
        width=319,
        height=55,
        text="Entrar",
        on_click=Enter,
        style=ft.ButtonStyle(
            bgcolor={
                ft.MaterialState.DEFAULT:ft.colors.WHITE,
                ft.MaterialState.HOVERED:ft.colors.TRANSPARENT
            },
            color={
                ft.MaterialState.DEFAULT:ft.colors.BLACK,
                ft.MaterialState.HOVERED:ft.colors.WHITE
            },
        )
    )

    Creat_Acount_Btn = ft.ElevatedButton(
        width=319,
        height=55,
        text="Criar Conta",
        on_click=Create_Acount,
        style=ft.ButtonStyle(
            bgcolor={
                ft.MaterialState.DEFAULT:ft.colors.WHITE,
                ft.MaterialState.HOVERED:ft.colors.TRANSPARENT
            },
            color={
                ft.MaterialState.DEFAULT:ft.colors.BLACK,
                ft.MaterialState.HOVERED:ft.colors.WHITE
            },
        )
    )
    

    back_page_login = ft.ElevatedButton(
        width=319,
        height=55,
        text="Voltar",
        on_click=Back_Login,
        style=ft.ButtonStyle(
            bgcolor={
                ft.MaterialState.DEFAULT:ft.colors.WHITE,
                ft.MaterialState.HOVERED:ft.colors.TRANSPARENT
            },
            color={
                ft.MaterialState.DEFAULT:ft.colors.BLACK,
                ft.MaterialState.HOVERED:ft.colors.WHITE
            },
        )
    )

    Login_btn_Enter_Create_Acount =  ft.ElevatedButton(
        width=319,
        height=55,
        text="Criar Conta",
        on_click=Enter_C_Acount,
        style=ft.ButtonStyle(
            bgcolor={
                ft.MaterialState.DEFAULT:ft.colors.WHITE,
                ft.MaterialState.HOVERED:ft.colors.BLACK
            },
            color={
                ft.MaterialState.DEFAULT:ft.colors.BLACK,
                ft.MaterialState.HOVERED:ft.colors.WHITE
            },
        )
    )

    Btn_Main_Home = ft.IconButton(
        icon=ft.icons.HOME,
        icon_color=ft.colors.BLACK,
        icon_size=35,
        offset=ft.Offset(2.3, 0),
        animate_offset=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE),
        on_click=Tela_Home_Main,
        selected=None,
        selected_icon=ft.icons.HOME,
        selected_icon_color=ft.colors.PURPLE_900
    )

    Text_Main_Home = ft.Text(
        value="Início",
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        size=16,
        opacity=0,
        animate_opacity=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE),
    )

    

    Btn_Main_Settings = ft.IconButton(
        icon=ft.icons.SETTINGS,
        icon_color=ft.colors.BLACK,
        icon_size=35,
        offset=ft.Offset(2.3, 0),
        animate_offset=ft.Animation(duration=450, curve=ft.AnimationCurve.EASE),
        on_click=Tela_Config,
        selected=None,
        selected_icon=ft.icons.SETTINGS,
        selected_icon_color=ft.colors.PURPLE_900
    )

    Text_Main_Settings = ft.Text(
        value="Configurações",
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        size=16,
        opacity=0,
        animate_opacity=ft.Animation(duration=450, curve=ft.AnimationCurve.EASE),
    )

    Btn_Main_Exit = ft.IconButton(
        icon=ft.icons.EXIT_TO_APP,
        icon_color=ft.colors.BLACK,
        icon_size=35,
        offset=ft.Offset(2.3, 0),
        animate_offset=ft.Animation(duration=450, curve=ft.AnimationCurve.EASE),
        on_click=Main_Back_Login
    )

    Text_Main_Exit = ft.Text(
        value="Sair",
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        size=16,
        opacity=0,
        animate_opacity=ft.Animation(duration=450, curve=ft.AnimationCurve.EASE),
    )

    
    Side_menu_colum_btn = ft.Container(
        content=ft.Column([
            ft.Row([
                Btn_Main_Home,
                Text_Main_Home
            ],vertical_alignment='center'),
            ft.Row([
                Btn_Main_Settings,
                Text_Main_Settings
            ],vertical_alignment='center'),
            ft.Row([
                Btn_Main_Exit,
                Text_Main_Exit
            ],vertical_alignment='center')
        ])
    )
    
    

    Side_menu_Main = ft.Container(
                width=185,
                height=855,
                bgcolor=ft.colors.BLACK12,
                offset=ft.Offset(x=-.6, y=0),
                animate_offset=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE),
                on_hover=Animete_Side_menu,
                content=Side_menu_colum_btn
                )

    Text_Main = ft.Text(
                            value="",
                            weight=ft.FontWeight.BOLD,
                            size=25,
                            color=ft.colors.BLACK
                        )

    Body_Login = ft.Column(
        col=16,
        controls=[
            ft.Container(
                content=Login_txt,
                margin=ft.margin.only(top=25)
            ),
            ft.Container(
                content=ft.Column([
                    Info_create,
                    Login_User,
                    Login_password
                ]),
                margin=ft.margin.only(top=33)
            ),
            ft.Container(
                content=ft.Column([
                    Login_btn_Enter,
                    Login_btn_Enter_Create_Acount
                ]),
                margin=ft.margin.only(bottom=33)
            )
            
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    image_sucess = ft.Image(
        src="_internal/marca-de-verificacao.png",
        offset=ft.Offset(x=0, y=0),
        animate_offset=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE)
    )

    image_Version_Antgia = ft.Image(
        src="_internal/alert_icon-icons.com_66469.png",
        offset=ft.Offset(x=0, y=-.2),
        animate_offset=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE)
    )
    # Tela Inicio
    text_Inicio = ft.Text(
                    value="Início",
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    size=35,
                    #offset=ft.Offset(0,0),
                    animate_offset=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE)
                )


    # Tela CONFIG
    text_Config = ft.Text(
                    value="Configuração",
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    size=35,
                    #offset=ft.Offset(2,0),
                    animate_offset=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE)
                )
    
    Btn_Creat_Shop = ft.ElevatedButton(
        icon=ft.icons.SHOP,
        text="Criar Loja",
        width=222,
        height=55,
        style=ft.ButtonStyle(
            bgcolor={
                ft.MaterialState.DEFAULT:ft.colors.PINK_300,
                ft.MaterialState.HOVERED:ft.colors.PINK_500
            },
            color={
                ft.MaterialState.DEFAULT:ft.colors.BLACK,
                ft.MaterialState.HOVERED:ft.colors.WHITE
            },
        ),
        on_click=Animete_Enter_Creat_Shop,
    )

    Tela_Config_ = ft.Column(
        controls=[
            ft.Container(
                margin=ft.margin.all(15),
                content=text_Config
            ),
            ft.Container(
                content=ft.Icon(
                    ft.icons.SETTINGS,
                    color=ft.colors.BLACK,
                    size=411,
                    opacity=.2,
                    offset=ft.Offset(.2,.2)
                ),
                margin=ft.margin.all(15)
            )
        ],
        
    )

    gv = ft.Row(width=999, wrap=True,)
    t = Nomes_lojas()
    if Criar_Arquivo_Base_Shop():
        for i in t: 
            
            gv.controls.append(
                ft.Container(
                    width=199,
                    height=233,
                    border_radius=15,
                    shadow=ft.BoxShadow(blur_radius=9, color=ft.colors.BLACK),
                    content=ft.Column([
                        ft.Image(
                            src="_internal/shop_base.png",
                            offset=ft.Offset(.3,.1)
                        ),
                        ft.Divider(),
                        ft.Container(
                            content=ft.Text(
                                value=f"{i}",
                                color=ft.colors.BLACK,
                                weight=ft.FontWeight.BOLD,
                                size=19
                                ),
                            margin=ft.margin.all(5)
                        )
                    ]),
                    bgcolor=ft.colors.WHITE,
                    margin=ft.margin.all(15),
                    on_click=None,
                ),
            )

    Tela_Inicio_ = ft.Column(
        scroll=True,
        controls=[
            ft.Container(
                content=text_Inicio,
                margin=ft.margin.all(15)
            ),
            ft.Container(
                content=Btn_Creat_Shop,
                margin=ft.margin.all(15)
            ),
            ft.Container(
                content=ft.Text(
                    value="Lojas",
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    size=35,
                ),
                margin=ft.margin.all(15)
            ),
            gv
            
        ],
    )

    Cria_Loja_Text_field = ft.TextField(
        width=555,
        hint_text="Digite o nome da loja",
        hint_style=ft.TextStyle(
            color=ft.colors.BLACK
        ),
        border_radius=25,
        color=ft.colors.BLACK
    )

    Btn_Cria_Loja = ft.ElevatedButton(
         width=555,
         height=55,
         text="Criar Loja",
         style=ft.ButtonStyle(
             bgcolor={
                ft.MaterialState.DEFAULT:ft.colors.BLUE_900,
                ft.MaterialState.HOVERED:ft.colors.BLUE_800,
                },
            
            color={
                ft.MaterialState.DEFAULT:ft.colors.WHITE
            }
         ),
         on_click=Creat_Shops        
    )

    Tela_Cria_Loja = ft.Column(
        controls=[
            ft.Container(
                margin=ft.margin.all(15),
                content=ft.Text(
                    value="Criar loja",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLACK
                )
            ),
            Info_create,
            ft.Container(
                content=Cria_Loja_Text_field,
                margin=ft.margin.all(15),
            ),
            ft.Container(
                margin=ft.margin.all(15),
                content=Btn_Cria_Loja
            ),
            ft.Container(
                content=ft.Icon(
                    ft.icons.SHOP,
                    size=299,
                    color=ft.colors.BLACK,
                    opacity=.2,
                    offset=ft.Offset(.5,.2)
                )
            )
        ]
    )

    Text_sucess_creat_shop = ft.Text(
                    value="Parabéns, você criou a sua loja!",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLACK
                )
    
    Image_sucess_creat_shop = ft.Image(
                    src="_internal/lancamento-de-produto.png",
                    offset=ft.Offset(.6,0)
                )

    Tela_Sucess_Creat_Shop = ft.Column(
        controls=[
            ft.Container(
                content=Image_sucess_creat_shop
            ),
            ft.Container(
                margin=ft.margin.all(15),
                content=Text_sucess_creat_shop
            )
        ]
    )

    Conteudo_de_Pagina_Main = ft.Container(
                            width=page.window_width - 99,
                            height=799,
                            bgcolor=ft.colors.WHITE,
                            content=None,
                            offset=ft.Offset(2,0),
                            animate_offset=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE),
                        )

    Body_Sucess_Login_and_Creat = ft.Column(
        col=16,
        controls=[
            ft.Container(
                width=222,
                height=222,
                margin=ft.margin.only(top=199),
                content=image_sucess,
                on_hover=Animate_sucess
            )
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    Body_Versao_antiga = ft.Column(
        col=16,
        controls=[
            ft.Container(
                width=222,
                height=222,
                margin=ft.margin.only(top=199),
                content=ft.Column([
                    image_Version_Antgia,
                    ft.Text(
                        value="🤖Essa Versão está desatualizada!",
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        size=25
                    )
                ], spacing=5)
            )
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    Body_Create_Acount = ft.Column(
        col=16,
        controls=[
            ft.Container(
                content=Creat_txt,
                margin=ft.margin.only(top=25)
            ),
            ft.Container(
                content=ft.Column([
                    Info_create,
                    Login_User,
                    Login_password,
                    Create_Acount_Con_Password
                ]),
                margin=ft.margin.only(top=33)
            ),
            ft.Container(
                content=ft.Column([
                    Creat_Acount_Btn,
                    back_page_login
                ]),
                margin=ft.margin.only(bottom=33)
            )
            
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    Body_Main = ft.Column(
        col=16,
        controls=[
            
            ft.Container(
                width=page.window_width - 15,
                height=855,
                bgcolor=ft.colors.WHITE,
                border_radius=15,
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            width=page.window_width - 15,
                            height=71,
                            bgcolor=ft.colors.WHITE,
                            shadow=ft.BoxShadow(blur_radius=22, color=ft.colors.BLACK),
                            padding=ft.padding.only(
                                left=25,
                            ),
                            content=ft.Row([
                                ft.Icon(
                                    ft.icons.BOLT,
                                    color=ft.colors.BLACK,
                                    size=35
                                ),
                                Text_Main
                            ])
                        )
                    ], alignment=ft.MainAxisAlignment.START),
                    ft.Row([
                        Side_menu_Main,
                        Conteudo_de_Pagina_Main
                    ],spacing=0)
                ],spacing=0)
            )
        ],spacing=0
    )
    
    Container = ft.Container(
        width=399,
        height=655,
        margin=ft.margin.all(35),
        bgcolor=ft.colors.BLACK,
        shadow=ft.BoxShadow(blur_radius=111, color=ft.colors.GREY),
        border_radius=15,
        content=Body_Login
    )

    Container2 = ft.Container(
        width=399,
        height=655,
        bgcolor=ft.colors.BLACK,
        margin=ft.margin.all(35),
        shadow=ft.BoxShadow(blur_radius=111, color=ft.colors.GREY),
        border_radius=15,
        content=Body_Create_Acount
    )

    Sucess = ft.Container(
        width=399,
        height=655,
        bgcolor=ft.colors.BLACK,
        margin=ft.margin.all(35),
        shadow=ft.BoxShadow(blur_radius=111, color=ft.colors.GREY),
        border_radius=15,
        content=Body_Sucess_Login_and_Creat
    )

    Version_Antiga = ft.Container(
        width=399,
        height=655,
        bgcolor=ft.colors.BLACK,
        margin=ft.margin.all(35),
        shadow=ft.BoxShadow(blur_radius=111, color=ft.colors.GREY),
        border_radius=15,
        content=Body_Versao_antiga
    )

    Container_Main = ft.Container(
        width=page.window_width - 15,
        height=855,
        bgcolor=ft.colors.WHITE,
        margin=ft.margin.all(35),
        shadow=ft.BoxShadow(blur_radius=111, color=ft.colors.PURPLE_900),
        border_radius=15,
        content=Body_Main,
        
    )

    Versao=3
    version = Verificar_Version()
    if version == Versao:
        page.add(Container)
    else:
        page.add(Version_Antiga)

if __name__ == "__main__":
    ft.app(target=Main)