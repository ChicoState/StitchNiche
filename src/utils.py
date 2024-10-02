"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
class stitch_calculator():
    def __init__(self):
        pass
    def rectangle_calculator(self, gauge_w, width, s_multiple, s_remainder, gauge_l, length, r_multiple, r_remainder ):
        stitches = self.one_dim_calculator(gauge_w, width, s_multiple, s_remainder)
        rows = self.one_dim_calculator(gauge_l, length, r_multiple, r_remainder)
        return (stitches, rows)

    def one_dim_calculator(self, gauge, x, multiple , remainder):
        estimate = int(x / gauge)
        difference = (estimate -  remainder)% multiple
        if difference == 0:
            return estimate
        elif difference  == 1:
            return estimate + 1
        else:
            option1 = estimate - difference + multiple
            option2 = estimate - difference
            if difference > abs(multiple - difference):
                return option1
            else:
                return option2