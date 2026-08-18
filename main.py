from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import notification

class CamSocLoApp(App):
    def build(self):
        self.title = "Cấm sóc lọ"
        
        # Giao diện chính
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.status_label = Label(
            text="Trạng thái: Đang bảo vệ...",
            font_size=20,
            halign='center'
        )
        layout.add_widget(self.status_label)
        
        btn_test = Button(
            text="Thử nghiệm thông báo",
            size_hint=(1, 0.3),
            background_color=(0.9, 0.2, 0.2, 1)
        )
        btn_test.bind(on_press=self.send_warning)
        layout.add_widget(btn_test)
        
        # Lên lịch kiểm tra định kỳ mỗi 5 giây
        Clock.schedule_interval(self.check_background_activity, 5)
        
        return layout

    def send_warning(self, instance):
        # Gửi thông báo đẩy giả lập
        notification.notify(
            title="Cấm sóc lọ",
            message="Phát hiện lọ lọ, dừng tay ngay!",
            app_name="Cấm sóc lọ",
            timeout=5
        )

    def check_background_activity(self, dt):
        self.status_label.text = "Đang giám sát hệ thống..."

if __name__ == '__main__':
    CamSocLoApp().run()