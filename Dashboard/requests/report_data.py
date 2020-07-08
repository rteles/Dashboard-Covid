
class ReportData(object):
    def __init__(self, json_data):
        self._codigo_autenticacao = json_data['codigoAutenticacao']

    @property
    def codigo_autenticidade(self):
        return self._codigo_autenticacao
