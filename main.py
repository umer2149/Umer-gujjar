from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from android.permissions import request_permissions, Permission
from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')

def get_all_apps():
    try:
        activity = PythonActivity.mActivity
        pm = activity.getPackageManager()
        PkgManager = autoclass('android.content.pm.PackageManager')
        packages = pm.getInstalledApplications(PkgManager.GET_META_DATA)
        app_list = []
        for i in range(packages.size()):
            info = packages.get(i)
            try:
                name = str(pm.getApplicationLabel(info))
                pkg = str(info.packageName)
                if pm.getLaunchIntentForPackage(pkg) is not None:
                    app_list.append((name, pkg))
            except:
                pass
        app_list.sort(key=lambda x: x[0].lower())
        return app_list
    except:
        return [("WhatsApp","com.whatsapp"),("YouTube","com.google.android.youtube"),("Imo","com.imo.android.imoim")]

def open_app(pkg):
    try:
        activity = PythonActivity.mActivity
        intent = activity.getPackageManager().getLaunchIntentForPackage(pkg)
        if intent:
            activity.startActivity(intent)
    except:
        pass

class UmarGujjarApp(App):
    def build(self):
        request_permissions([Permission.RECORD_AUDIO, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        self.all_apps = get_all_apps()
        main = BoxLayout(orientation='vertical', padding=10, spacing=10)
        main.add_widget(Label(text='UMAR GUJJAR JARVIS', size_hint_y=None, height=50, font_size='20sp', bold=True))
        self.search = TextInput(hint_text='App ka naam likho...', size_hint_y=None, height=50, multiline=False)
        self.search.bind(text=self.filter_apps)
        main.add_widget(self.search)
        scroll = ScrollView()
        self.grid = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        scroll.add_widget(self.grid)
        main.add_widget(scroll)
        self.show_apps(self.all_apps)
        return main

    def show_apps(self, apps):
        self.grid.clear_widgets()
        for name, pkg in apps:
            btn = Button(text=name, size_hint_y=None, height=55)
            btn.bind(on_press=lambda x, p=pkg: open_app(p))
            self.grid.add_widget(btn)

    def filter_apps(self, instance, value):
        if not value:
            self.show_apps(self.all_apps)
        else:
            self.show_apps([a for a in self.all_apps if value.lower() in a[0].lower()])

UmarGujjarApp().run()
