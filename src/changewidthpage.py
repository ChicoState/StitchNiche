

class  ChangeWidthPage(App):
    def build(self):
        self.sc = StitchCalculator()
        layout = BoxLayout(orientation='vertical', spacing=30, size_hint=(1, 1))


        title_label = Label(text="Stitch Niche", font_size='32sp', color=(0.5, 0, 0.5, 1))
        layout.add_widget(title_label)

        title_label = Label(text="Stitch Calculator - Rectangle", font_size='20sp', color=(0.5, 0, 0.5, 1))
        layout.add_widget(title_label)

        # form
        style = Styles(
            label_color=(0.5, 0, 0.5, 1),
            header_color = (0.8, 0, 0.1),
            size_hint=(1, 1),
            height=35,
            background_color=(1, 1, 1, 1),
            padding=5,
            spacing=20
        )
        input_fields = {
            "Project Measurements:": {                                                                              # header
                "start_width_input": (                                                                                # variable associated with input
                    "Starting Width Input",                                                                              # label text for input
                    "8.0",                                                                                      # default value
                    "How wide your finished piece should be at first row. Can be entered as a decimal or whole number." # tooltip
                ),
                "end_width_input": (  # variable associated with input
                    "Ending Width Input",  # label text for input
                    "16.0",  # default value
                    "How wide your finished piece should be at final row. Can be entered as a decimal or whole number."
                # tooltip
                ),
                "length_input": (
                    "Length Input",
                    "60.0",
                    "How long you want your finished piece to be. Can be entered as a decimal or whole number."
                ),
                "gauge_width_input": (
                    "Gauge Width Input",
                    "7.14",
                    "The ratio of stitches to an inch for your specific pattern worked by you. Calculated by dividing the count of stitches within a section of a row by the width of that section. Can be entered as a decimal or whole number."
                ),
                "gauge_length_input": (
                    "Gauge Length Input",
                    "6.0",
                    "The ratio of rows to an inch for your specific pattern worked by you. Calculated by dividing the count of rows within a section of length by the length of the section. Can be entered as a decimal or whole number."
                )
            },
            "Pattern:": {
                "Stitch Multiple": (
                    "Stitch Multiple",
                    "5",
                    "Based on the constraints your pattern has for casting on, if your pattern calls for working a multiple of x stitches plus y, your stitch_multiple is x. If it doesn’t have any requirements, enter 1. This value is always a whole number."
                ),
                "Stitch Remainder": (
                    "Stitch Remainder",
                    "0",
                    "Based on the constraints your pattern has for casting on, if your pattern calls for working a multiple of x stitches plus y, your stitch_remainder is y. If it doesn’t have any requirements or just calls for a multiple x, enter 0. This value is always a whole number."
                ),
                "Row Multiple": (
                    "Row Multiple",
                    "1",
                    "Based on whether it matters the row on which you quit your stitch pattern. If your pattern has x rows and calls for repeating rows n through m, then your row_multiple is (m - n + 1). If it does not matter where you end the pattern and bind off, then enter 1. This value is always a whole number."
                ),
                "Row Remainder": (
                    "Row Remainder",
                    "0",
                    "Based on whether it matters the row on which you quit your stitch pattern. If your pattern has x rows and calls for repeating rows n through m, then your row_remainder is (x - m + n - 1).  If it does not matter where you end the pattern and bind off, then enter 0. This value is always a whole number."
                )
            }
        }

        gen = GenerateWidgets()
        layout, text_inputs, self.result_label = gen.generate_number_form(
            layout = layout,
            input_fields = input_fields,
            styles=style,
            submit_handler=self.submit,
        )
        self.start_width_input = text_inputs['start_width_input']
        self.end_width_input = text_inputs['end_width_input']
        self.length_input = text_inputs['length_input']
        self.gauge_width_input = text_inputs['gauge_width_input']
        self.gauge_length_input = text_inputs['gauge_length_input']
        self.pattern_inputs = []
        self.pattern_inputs.append(text_inputs['Stitch Multiple'])
        self.pattern_inputs.append(text_inputs['Stitch Remainder'])
        self.pattern_inputs.append(text_inputs['Row Multiple'])
        self.pattern_inputs.append(text_inputs['Row Remainder'])


        return layout

    def submit(self, instance):
        # Capture all inputs into a dictionary
        outputs = {
            "Starting Width": float(self.start_width_input.text),
            "Ending Width": float(self.end_width_input.text),
            "Length": float(self.length_input.text),
            "Gauge Width": float(self.gauge_width_input.text),
            "Gauge Length": float(self.gauge_length_input.text),
            "Patterns": {f"Pattern {chr(65 + i)}": input_field.text for i, input_field in
                         enumerate(self.pattern_inputs)}
        }

        self.sc.setpattern(float(self.pattern_inputs[0].text),  # Sets Pattern restrictions for stitch calculator
                           float(self.pattern_inputs[1].text),
                           float(self.pattern_inputs[2].text),
                           float(self.pattern_inputs[3].text), )

        result = self.sc.change_width_calculator(float(self.start_width_input.text),
                                              float(self.end_width_input.text),
                                              float(self.length_input.text),
                                              float(self.gauge_width_input.text),
                                              float(self.gauge_length_input.text),
                                              )

        # Print or process the outputs as needed (for demonstration)
        # print(outputs)  # You can remove this line later
        # Refresh the app by resetting input fields
        self.end_width_input.text = ""
        self.start_width_input.text = ""
        self.length_input.text = ""
        self.gauge_width_input.text = ""
        self.gauge_length_input.text = ""
        for input_field in self.pattern_inputs:
            input_field.text = ""

        self.result_label.text = str(result)


if __name__ == "__main__":
    ChangeWidthPage().run()
