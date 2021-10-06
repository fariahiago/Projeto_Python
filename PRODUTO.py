import datetime as dt

#Produtos
class produto: 
     def __init__(self, id, nome, vr_compra = 0.00, qtde_produto = 0, vr_venda = 0):
          self.id = id
          self.nome = nome
          self.vr_compra = vr_compra
          self.qtde_produto = qtde_produto

     def LANCA_PROD(self, id, qtde_entrada):
          self.id = input("Digite o ID do produto: ")
          self.qtde_produto = input("Digite a quantidade a ser lançada em sistema: ")
          NF = int(input("Digite o numero da Nota fiscal de entrada: "))
          arquivo = open(log_entrada.txt, 'a') 
          diacompra = dt.datetime.strftime("%d %B %Y")
          log = [NF, self.id, qtde_entrada, self.qtde_produto, diacompra, "\n"]
          arquivo.write(log)
          arquivo.close()
     
     def GERA_VR_VENDA(self, id, vr_margem, delta_custofixo):
          self.vr_venda = (self.vr_compra * (vr_margem * delta_custo)) 

     def VENDA (self, id, qtd_venda, vr_venda):
          if qtd_venda < self.qtde_produto:
               print("Estoque insuficiente!")
          else: 
               self.qtde_produto = self.qtde_produto - qtd_venda
               arquivo = open(log_venda.txt, 'a')
               diavenda = dt.datetime.strftime("%d %B %Y")
               log = [NF, self.id, qtd_venda, self.qtde_produto, diavenda, "\n"]
               arquivo.write(log)
               arquivo.close()
          

          