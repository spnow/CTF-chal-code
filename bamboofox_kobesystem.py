'''
Created on 2016-2-29

@author: wenhuizone
'''
import base64
'''
a='iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOESURBVHhe7ZBJjiQxDAP7/5+uOXQgIVQKhkjbfRnGTSa1mD+fMCZhCSQsgYQlkLAEEpZAwhJIWAIJSyBhCSQsgYQlkLAEEpZAwhJIWAIJSyBhCZhh/ezBFBemuDBFJ2EJJCyB3bCoZ9BTuqi7OQgFhHPbVcxO1m6fS93NQSggnNuuYnaydvtc6m4OQgHh3HYVs5O13Qfe4BDPxdqZEW5ubzE7WXvzXKydGeHm9hazk7U3z8XamRFubm8xO1m7fS71uZc3OLouFbOTtdvnUp97eYOj61IxO1m7fS71uZc3OLouFbOTtRfOxVFAKCBc2L7G7GTthXNxFBAKCBe2rzE7WXvhXBwFhALChe1rzE7WiovpmX0AoYBwbruK2cna7XOpuzkIBYRz21XMTtZun0vdzUEoIJzbrmJ2staFKd0HqGcvHkzRMTtZ68IUMRrqc9tVzE7WujBFjIb63HYVv/Ms/KP7CcLGJ0+RsAQSloB5AefPoGfWhbXLiHr7xcYcwf4Z9My6sM6+TS2+2Jgj2D+DnlkX1tm3qcUXm90RHLJ9Lo4CQgeODhzuGWv8zl/Yv30ljgJCB44OHO4Za/zOX9i/fSWOAkIHjg4c7hlrzE7Wdqc8IHTSA44OHB04/pyEJZCwBHbDekAoIBQQOnDMoKcDxxKsOglLIGEJ+J1fcEg5hboDx7KL+uaLit/5BYd0x73BMfsS9YUXFb/zCw7pjnuDY/Yl6gsvKn7nETi/gNCBYwnWAkIBQSdhCSQsAbOTtS5MWf6EuoBQJOoCQgeODcwR7HdhyiyRB4QiURcQOnBsYI5gvwtTZok8IBSJuoDQgWMDcwT7xQvomX0SYQnWYqbuwLGBOYL9CWsC+xPWBPaLV1IvXx4QCgizLuqjmEO5qPvAGxzLLuoCQgFh1kV9FHMoF3UfeINj2UVdQCggzLqoj2IO5aLuA29wuF0LsBYQlpKNOYL94repxa4FWAsIS8nGHMF+8dvUYtcCrAWEpWRjjmC/+G3q2ZeoCwjdnAeETtrHHMpFy7894Jh1Icwk6gJCJ+1jDuWi5d8ecMy6EGYSdQGhk/Yxh3KReBM9s297MK6AcIKEJZCwBHbD8mDKcg6OAkIHjgJCAWGDhCWQsAQOjPh/SFgCCUsgYQkkLIGEJZCwBBKWQMISSFgCCUsgYQkkLIGEJZCwBBKWQMISSFgCCWvM5/MP+EQ35GJELB4AAAAASUVORK5CYII='
fkey=open('g:\kb.png','wb')
fkey.write(base64.b64decode(a))
'''
fkeyy=open('g:/admin.png','rb')
str=fkeyy.read()
b=base64.b64encode(str)
print b