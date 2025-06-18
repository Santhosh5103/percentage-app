from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PercentageApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.subject_count_label = Label(text='Enter number of subjects:')
        self.layout.add_widget(self.subject_count_label)

        self.subject_count_input = TextInput(multiline=False, input_filter='int')
        self.layout.add_widget(self.subject_count_input)

        self.submit_button = Button(text='Submit', on_press=self.create_subject_inputs)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def create_subject_inputs(self, instance):
        try:
            self.num_subjects = int(self.subject_count_input.text)
        except ValueError:
            self.subject_count_label.text = "Invalid number. Enter again:"
            return

        self.layout.clear_widgets()
        self.credit_inputs = []
        self.percent_inputs = []

        for i in range(self.num_subjects):
            self.layout.add_widget(Label(text=f'Subject {i + 1} Credits:'))
            credit_input = TextInput(multiline=False, input_filter='int')
            self.layout.add_widget(credit_input)
            self.credit_inputs.append(credit_input)

            self.layout.add_widget(Label(text=f'Subject {i + 1} Percentage:'))
            percent_input = TextInput(multiline=False, input_filter='float')
            self.layout.add_widget(percent_input)
            self.percent_inputs.append(percent_input)

        self.calc_button = Button(text='Calculate', on_press=self.calculate_percentage)
        self.layout.add_widget(self.calc_button)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

    def calculate_percentage(self, instance):
        try:
            total_credits = 0
            weighted_sum = 0
            for credit_input, percent_input in zip(self.credit_inputs, self.percent_inputs):
                credits = int(credit_input.text)
                percent = float(percent_input.text)
                total_credits += credits
                weighted_sum += credits * percent

            if total_credits == 0:
                self.result_label.text = "Total credits cannot be zero."
            else:
                final_percent = weighted_sum / total_credits
                self.result_label.text = f'Overall Percentage: {final_percent:.2f}'
        except:
            self.result_label.text = "Please fill all inputs correctly."

if __name__ == '__main__':
    PercentageApp().run()
