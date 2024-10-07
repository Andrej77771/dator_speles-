import itertools


class Spēle:
  Spēles_nosaukums = ''
  Žanrs = 'Šuteri'
  Cena = 0
  id_iter = itertools.count()


  def __init__(self, nosaukums=None, cena=20):
     self.Spēles_id = next(self.id_iter) + 1
     self.Spēles_nosaukums = nosaukums
     self.Spēles_cena = cena


  def Spēles_info(self):
     return [self.Spēles_nosaukums, self.Žanrs, self.Spēles_cena]


  def Spēles_info_print(self):
     print('Spēles nosaukums: ' + str(self.Spēles_nosaukums))
     print('Žanrs: ' + str(self.Žanrs))
     print('Cena: ' + str(self.Spēles_cena) + ' EUR\n')


class Spēlētājs:
   Vārds = ''
   Uzvārds = ''
   Vecums = 0
   id_iter_player = itertools.count()


   def __init__(self, vārds, uzvārds, vecums):
      self.Spēlētāja_id = next(self.id_iter_player) + 1
      self.Vārds = vārds
      self.Uzvārds = uzvārds
      self.Vecums = vecums


   def Spēlētāja_info(self):
      return [self.Vārds, self.Uzvārds, self.Vecums]


   def Spēlētāja_info_print(self):
        print('Spēlētāja vārds: ' + str(self.Vārds))
        print('Spēlētāja uzvārds: ' + str(self.Uzvārds))
        print('Vecums: ' + str(self.Vecums) + '\n')


class Spēle_Spēlēšana:
    Spēlēšanas_sākuma_laiks = 0
    Spēlēšanas_beigu_laiks = 0
    id_Spēle = 0
    id_Spēlētājs = 0
    id_iter_spēlēšana = itertools.count()


    def __init__(self, sākums, beigas, spēle_id, spēlētājs_id):
      self.Spēlēšanas_id = next(self.id_iter_spēlēšana) + 1
      self.Spēlēšanas_sākuma_laiks = sākums
      self.Spēlēšanas_beigu_laiks = beigas
      self.id_Spēle = spēle_id
      self.id_Spēlētājs = spēlētājs_id


    def Kopējais_spēlēšanas_laiks(self):
       return self.Spēlēšanas_beigu_laiks - self.Spēlēšanas_sākuma_laiks


    def Spēlēšanas_info_print(self):
      print('Spēlēšanas sākuma laiks: ' + str(self.Spēlēšanas_sākuma_laiks))
      print('Spēlēšanas beigu laiks: ' + str(self.Spēlēšanas_beigu_laiks))
      print('Spēle id: ' + str(self.id_Spēle))
      print('Spēlētājs id: ' + str(self.id_Spēlētājs))
      print('Kopējais spēlēšanas laiks: ' + str(self.Kopējais_spēlēšanas_laiks()) + ' stundas\n')



spēle1 = Spēle("Counter-Strike: Global Offensive", 30)
spēle2 = Spēle("Call of Duty: Modern Warfare", 60)
spēle3 = Spēle("Apex Legends", 40)


print(spēle1.Spēles_id)
spēle1.Spēles_info_print()
print(spēle2.Spēles_id)
spēle2.Spēles_info_print()
print(spēle3.Spēles_id)
spēle3.Spēles_info_print()


spēlētājs1 = Spēlētājs('Kristaps', 'Bērziņš', 18)
spēlētājs2 = Spēlētājs('Mārtiņš', 'Kļaviņš', 21)
spēlētājs3 = Spēlētājs('Līga', 'Grīnberga', 17)


print(spēlētājs1.Spēlētāja_id)
spēlētājs1.Spēlētāja_info_print()
print(spēlētājs2.Spēlētāja_id)
spēlētājs2.Spēlētāja_info_print()
print(spēlētājs3.Spēlētāja_id)
spēlētājs3.Spēlētāja_info_print()


spēlēšana1 = Spēle_Spēlēšana(14.00, 16.00, spēle1.Spēles_id, spēlētājs1.Spēlētāja_id)
spēlēšana1.Spēlēšanas_info_print()


spēlēšana2 = Spēle_Spēlēšana(12.30, 15.00, spēle2.Spēles_id, spēlētājs2.Spēlētāja_id)
spēlēšana2.Spēlēšanas_info_print()


spēlēšana3 = Spēle_Spēlēšana(17.00, 19.00, spēle3.Spēles_id, spēlētājs3.Spēlētāja_id)
spēlēšana3.Spēlēšanas_info_print()