from random import randint


class Cat:

    def __init__(self):
        self.name = ''
        self.old = 1
        self.mood = 40
        self.satiety = 40
        self.cat_activity = True
        self.cat_image = 'images/cat.jpg'
        self.option = ''

    def action(self, cat_action=None):
        if cat_action is None:
            return self._render_cat()
        elif cat_action == 'feed':
            self._feed()
        elif cat_action == 'play':
            self._play()
        elif cat_action == 'sleep':
            self._sleep()

        self._cat_test()
        return self._render_cat()

    def _render_cat(self):
        return {
            'cat_name': self.name,
            'cat_image': self.cat_image,
            'cat_old': self.old,
            'cat_mood': self.mood,
            'cat_satiety': self.satiety,
            'option': self.option,
        }

    def _feed(self):
        self.mood += 5
        self.satiety += 15

    def _play(self):
        rage = randint(0, 99)
        if self.cat_activity:
            self.mood += 15
            self.satiety -= 10
            if rage <= 33:
                self.mood = 0
        else:
            self.mood -= 5
            self.cat_activity = True

    def _sleep(self):
        if self.cat_activity:
            self.option = 'disabled'
            self.cat_activity = False
        else:
            self.option = ''
            self.mood += 10
            self.satiety -= 5
            self.cat_activity = True

    def _cat_test(self):
        if self.mood < 33:
            self.cat_image = 'images/cat.jpg'
        elif 33 < self.mood < 66:
            self.cat_image = 'images/cat5.jpg'
        elif self.mood > 66:
            self.cat_image = 'images/cat3.jpeg'
        if self.option == 'disabled':
            self.cat_image = 'images/cat2.jpg'
        if self.satiety < 0:
            self.satiety = 0
        elif self.satiety > 100:
            self.satiety = 100
            self.mood -= 30
            self.cat_image = 'images/cat6.jpg'
        if self.mood > 100:
            self.mood = 100
        elif self.mood < 0:
            self.mood = 0
