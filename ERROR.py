import logging


def error_gpt(resp, data):
    if resp.status_code < 200 or resp.status_code >= 300:
        error = 'Произошла ошибка'
        logging.error(str(resp.status_code))
        return error
    if 'error' in data:
        error1 = 'Произошла ошибка на стороне сервера.'
        logging.error(str(f'{data["error"]}'))
        return error1


error3 = 'Произошла неизвестная ошибка!'

logging.basicConfig(filename='errors.cod.log', level=logging.ERROR, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

error = ('<b>Состояние: Превышено\n'
          'количество символов❗️️️️️️️️️️️</b>\n'
          '<i>Пожалуйста задайте новый\n'
          'вопрос, это обнулит ваш\n'
          'предыдущий диалог.</i>')

error1 = ('<b>Состояние: Нет вопроса❗️</b>\n'
          '<i>Вы не можете продолжить\n'
          'ответ, так как вы не задали\n'
          'вопрос который нужно\n'
          'продолжить.😢</i>')

stop = 'В доступе отказано!'

error5 = ('‼️Произошла непредвиденная ошибка.\n'
          'Попробуйте позже, если проблема остается,\n'
          'обратитесь за помощью!\n')