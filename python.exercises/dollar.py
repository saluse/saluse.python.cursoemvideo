#==================================================
   2 # Cotacao do dolar
   3 #==================================================
   4 import urllib
   5 import re
   6 
   7 def pegar_cotacao_dolar():
   8    
   9     '''Funcao para pegar a cotacao do dolar.
  10     Retorna uma tupla com o : valor de compra e o valor de venda
  11     do dia.'''
  12    
 13     
  14     # pegando o conteudo da pagina    
  15     pagina = urllib.urlopen( 'http://www.bc.gov.br/htms/infecon/taxas/taxas.htm' )
  16     pagina = pagina.read()
  17     
  18     # obtendo os valores de compra e venda do dolar
  19     taxa_compra, taxa_venda = re.findall( '[0-9],[0-9][0-9][0-9]', pagina )
  20     
  21     # retornando esses valores
  22     return ( taxa_compra, taxa_venda )
  23     
  24 print pegar_cotacao_dolar()