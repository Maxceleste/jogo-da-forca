from forca import Forca
import pytest

game = Forca()

class TestClass():

    #Teste da exibição_letras

    def teste_um(self):
        assert game.exibição_letras('teste', ()) == ' _  _  _  _  _ '
    
    def teste_dois(self):
        assert game.exibição_letras('teste', ('a',)) == ' _  _  _  _  _ '
    
    def teste_tres(self):
        assert game.exibição_letras('teste', ('e',)) == ' _ e _  _ e'
    
    def teste_quatro(self):
        assert game.exibição_letras('teste', ('t', 's')) == 't _ st _ '
    
    def teste_cinco(self):
        assert game.exibição_letras('teste', ('t', 'e', 's',)) == 'teste'

    #Teste da letra_certa

    def teste_seis(self):
        assert not game.letra_certa('g', 'teste')

    def teste_sete(self):
        assert not game.letra_certa('b', 'teste')
    
    def teste_oito(self):
        assert game.letra_certa('e', 'teste')
    
    def teste_nove(self):
        assert game.letra_certa('s', 'teste')
    
    def teste_dez(self):
        assert game.letra_certa('t', 'teste')