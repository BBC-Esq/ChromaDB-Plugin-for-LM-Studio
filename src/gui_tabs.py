from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QTextEdit, QTabWidget, QVBoxLayout, QWidget, QGroupBox, QPushButton, QHBoxLayout
from PySide6.QtCore import QUrl
from pathlib import Path
from gui_tabs_settings import GuiSettingsTab
from gui_tabs_tools import GuiSettingsTab as ToolsSettingsTab
from gui_tabs_databases import DatabasesTab
from gui_tabs_vector_models import VectorModelsTab
from gui_tabs_database_query import DatabaseQueryTab
from gui_tabs_manage_databases import ManageDatabasesTab
from functools import partial

def load_url(view, url):
    view.setUrl(QUrl.fromLocalFile(url))

def create_tabs():
    tab_widget = QTabWidget()
    tab_widget.setTabPosition(QTabWidget.South)
    
    tab_font = tab_widget.font()
    tab_font.setPointSize(13)
    tab_widget.setFont(tab_font)

    user_manual_folder = Path(__file__).parent / 'User_Manual'
    
    # SETTINGS TAB
    settings_tab = GuiSettingsTab()
    tab_widget.addTab(settings_tab, 'Settings')
    
    # USER GUIDE TAB
    user_guide_tab = QWidget()
    user_guide_layout = QVBoxLayout()

    menu_group = QGroupBox("")
    menu_layout = QHBoxLayout()

    buttons_dict = {
        'Tips': 'tips.html',
        'Settings': 'settings.html',
        'Embeddings': 'embedding_models.html',
        'Whisper': 'transcribe.html',
        'Vision': 'vision.html',
    }

    user_guide_view = QWebEngineView()
    user_guide_view.setHtml('<body style="background-color: #161b22;"></body>')

    default_url = user_manual_folder / 'tips.html'
    load_url(user_guide_view, str(default_url))

    light_blue_style = "QPushButton { background-color: #3498db; color: white; }"

    for button_name, html_file in buttons_dict.items():
        button = QPushButton(button_name)
        button.setStyleSheet(light_blue_style)
        button_url = user_manual_folder / html_file
        button.clicked.connect(partial(load_url, user_guide_view, str(button_url)))
        menu_layout.addWidget(button)

    menu_group.setLayout(menu_layout)
    user_guide_layout.addWidget(user_guide_view)
    user_guide_layout.addWidget(menu_group)
    user_guide_layout.setStretch(0, 9)
    user_guide_layout.setStretch(1, 1)

    user_guide_tab.setLayout(user_guide_layout)
    tab_widget.addTab(user_guide_tab, 'User Guide')

    # VECTOR MODELS TAB
    vector_models_tab = VectorModelsTab()
    tab_widget.addTab(vector_models_tab, 'Models')
    
    # TOOLS TAB
    tools_tab = ToolsSettingsTab()
    tab_widget.addTab(tools_tab, 'Tools')

    # CREATE DATABASE TAB
    databases_tab = DatabasesTab()
    tab_widget.addTab(databases_tab, 'Create Database')
    
    # MANAGE DATABASES TAB
    manage_databases_tab = ManageDatabasesTab()
    tab_widget.addTab(manage_databases_tab, 'Manage Databases')

    # DATABASE QUERY TAB
    database_query_tab = DatabaseQueryTab()
    tab_widget.addTab(database_query_tab, "Query Database")

    return tab_widget