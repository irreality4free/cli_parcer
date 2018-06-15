from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.uix.button import Button
from kivy.core.window import Window



layer1=[[83, 675, 88, 677, 91, 683, 88, 689, 83, 691, 77, 689, 74, 683, 77, 677, 83, 675], [180, 675, 185, 677, 188, 683, 185, 689, 180, 691, 174, 689, 171, 683, 174, 677, 180, 675], [277, 675, 282, 677, 285, 683, 282, 689, 277, 691, 271, 689, 269, 683, 271, 677, 277, 675], [374, 675, 379, 677, 382, 683, 379, 689, 374, 691, 368, 689, 366, 683, 368, 677, 374, 675], [471, 675, 477, 677, 479, 683, 477, 689, 471, 691, 465, 689, 463, 683, 465, 677, 471, 675], [568, 675, 574, 677, 576, 683, 574, 689, 568, 691, 562, 689, 560, 683, 562, 677, 568, 675], [665, 675, 671, 677, 673, 683, 671, 689, 665, 691, 659, 689, 657, 683, 659, 677, 665, 675], [762, 675, 768, 677, 770, 683, 768, 689, 762, 691, 756, 689, 754, 683, 756, 677, 762, 675], [857, 682, 858, 681, 860, 682, 860, 683, 860, 685, 858, 685, 857, 685, 856, 683, 857, 682], [1126, 675, 1131, 677, 1134, 683, 1131, 688, 1126, 691, 1120, 688, 1118, 683, 1120, 677, 1126, 675], [1223, 681, 1224, 681, 1225, 682, 1224, 684, 1223, 684, 1222, 684, 1221, 682, 1222, 681, 1223, 681], [1489, 675, 1495, 677, 1497, 683, 1495, 689, 1489, 691, 1484, 689, 1481, 683, 1484, 677, 1489, 675], [1586, 675, 1592, 677, 1595, 683, 1592, 689, 1586, 691, 1581, 689, 1578, 683, 1581, 677, 1586, 675], [1684, 675, 1689, 677, 1692, 683, 1689, 689, 1684, 691, 1678, 689, 1676, 683, 1678, 677, 1684, 675], [1779, 681, 1784, 679, 1790, 681, 1793, 687, 1790, 693, 1784, 695, 1779, 693, 1776, 687, 1779, 681]]

# Start polyline (129) id: (1,); dir: (1,); n: 9;
# ('-27.74, -32.21    ',)
# ('-27.71, -32.19    ',)
# ('-27.70, -32.17    ',)
# ('-27.71, -32.14    ',)
# ('-27.74, -32.13    ',)
# ('-27.76, -32.14    ',)
# ('-27.77, -32.17    ',)
# ('-27.76, -32.19    ',)
# ('-27.74, -32.21    ',)


class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(0,1,0,1)
            # Ellipse(pos = (100,100), size = (50,50))
            # Line(points = (526,79,529,81,530,83,529,86,526,87,524,86,523,83,524,81,526,79), close = False, width = 5)
            self.line_list=list()

            self.layer=[[83, 675, 88, 677, 91, 683, 88, 689, 83, 691, 77, 689, 74, 683, 77, 677, 83, 675], [180, 675, 185, 677, 188, 683, 185, 689, 180, 691, 174, 689, 171, 683, 174, 677, 180, 675], [277, 675, 282, 677, 285, 683, 282, 689, 277, 691, 271, 689, 269, 683, 271, 677, 277, 675], [374, 675, 379, 677, 382, 683, 379, 689, 374, 691, 368, 689, 366, 683, 368, 677, 374, 675], [471, 675, 477, 677, 479, 683, 477, 689, 471, 691, 465, 689, 463, 683, 465, 677, 471, 675], [568, 675, 574, 677, 576, 683, 574, 689, 568, 691, 562, 689, 560, 683, 562, 677, 568, 675], [665, 675, 671, 677, 673, 683, 671, 689, 665, 691, 659, 689, 657, 683, 659, 677, 665, 675], [762, 675, 768, 677, 770, 683, 768, 689, 762, 691, 756, 689, 754, 683, 756, 677, 762, 675], [857, 682, 858, 681, 860, 682, 860, 683, 860, 685, 858, 685, 857, 685, 856, 683, 857, 682], [1126, 675, 1131, 677, 1134, 683, 1131, 688, 1126, 691, 1120, 688, 1118, 683, 1120, 677, 1126, 675], [1223, 681, 1224, 681, 1225, 682, 1224, 684, 1223, 684, 1222, 684, 1221, 682, 1222, 681, 1223, 681], [1489, 675, 1495, 677, 1497, 683, 1495, 689, 1489, 691, 1484, 689, 1481, 683, 1484, 677, 1489, 675], [1586, 675, 1592, 677, 1595, 683, 1592, 689, 1586, 691, 1581, 689, 1578, 683, 1581, 677, 1586, 675], [1684, 675, 1689, 677, 1692, 683, 1689, 689, 1684, 691, 1678, 689, 1676, 683, 1678, 677, 1684, 675], [1779, 681, 1784, 679, 1790, 681, 1793, 687, 1790, 693, 1784, 695, 1779, 693, 1776, 687, 1779, 681]]
            # Line(points=(526, 79, 529, 81, 530, 83), close=False, width=10)
            # self.line = Line(points = (), width = 10, joint = 'miter')
            for li in self.layer:
                print(li)
                line_l = Line(points=(), width=1)
                self.line_list.append(line_l)

            for x,line in enumerate(self.line_list):

                for num_,point in enumerate(self.layer[x]):
                    if num_ % 2 == 0:
                        line.points+=(self.layer[x][num_],self.layer[x][num_+1])



    # def on_touch_down(self, touch):
    #     self.line.points +=(touch.x, touch.y)
    #
    #     with self.canvas:
    #         Color(0,0,1,1)
    #         rad = 30
    #         Ellipse(pos = (touch.x - rad/2,touch.y - rad/2), size = (rad,rad))
    #         touch.ud['line'] = Line(points=(touch.x, touch.y), width = 15)
    #
    # def on_touch_move(self, touch):
    #     touch.ud['line'].points +=(touch.x, touch.y)

class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text = 'Clear', on_press = self.clear_canvas, size = (100,50)))
        parent.add_widget(Button(text = 'Save', on_press = self.save, size = (100,50), pos = (100,0)))
        parent.add_widget(Button(text = 'Screen', on_press = self.screen, size = (100,50), pos = (200,0)))

        return  parent

    def clear_canvas(self,instance):
        self.painter.canvas.clear()

    def save(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')


    def screen(self, instance):
        Window.screenshot('screen.png')



if __name__ == '__main__':
    PaintApp().run()
