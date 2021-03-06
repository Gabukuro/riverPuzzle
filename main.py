# Regras: 
# O bote pode carregar apenas 2 pessoas por vez.
# Apenas a mãe, o pai e o policial podem operar o bote.
# A mãe não pode ser deixada sozinha com os filhos.
# O pai não pode ser deixado sozinho com as filhas.
# O ladrão não pode ser deixado sozinho com ninguém sem o policial.

def main():
  persons = ['mother', 'father', 'policeOfficer', 'son1', 'son2', 'daughter1', 'daughter2', 'robber']
  left_side = set(persons)
  right_side = set([])

  while left_side != set([]):
    
    should_continue = False
    while should_continue == False:
      print('pessoas disponíveis: ', left_side)
      p1 = input('escolha pessoa 1 => ')
      p2 = input('escolha pessoa 2 => ')
      left_side, right_side, should_continue = moveTwo(p1, p2, left_side, right_side)

    if left_side == set([]):
      break

    should_continue = False
    while should_continue == False:
      print('pessoas disponíveis: ', right_side)
      p3 = input('escolha uma pessoa para voltar => ')
      left_side, right_side, should_continue = moveBack(p3, left_side, right_side)

    print('lado esquerdo: ', left_side)
    print('lado direito: ', right_side)
    print('\n\n\n\====================================\n\n')
    

  print('Fim de jogo!')

def moveTwo(p1, p2, left, right):
  should_continue = True
  temp_left = left
  temp_right = right

  temp_left = set(temp_left - set([p1, p2]))
  temp_right.update([p1, p2])
  
  if (validate_crew(p1, p2) == True) and (validate_sides(temp_left, temp_right) == True):
    print('\nmovido!\n')
  else:
    print('\nmovimento inválido!\n')
    should_continue = False
    return left, right, should_continue

  return temp_left, temp_right, should_continue

def moveBack(p3, left, right):
  should_continue = True
  temp_left = left
  temp_right = right

  temp_right = set(temp_right - set([p3]))
  temp_left.update([p3])

  if (validate_crew(p3) == True) and (validate_sides(temp_left, temp_right) == True):
    print('\nmovido!\n')
  else:
    print('\nmovimento inválido!\n')
    should_continue = False
    return left, right, should_continue

  return temp_left, temp_right, should_continue
  
def validate_crew(p1, p2 = ''):
  drivers = ['mother', 'father', 'policeOfficer']

  if not p2 and (p1 not in drivers):
    return False
  elif p2 and ((p1 not in drivers) and (p2 not in drivers)):
    return False
  else:
    return True

def validate_sides(left, right):
  restrictions = list([
    ['mother', 'son1', 'son2'],
    ['father', 'daughter1', 'daughter2'],
  ])

  for restriction in restrictions:
    if restriction == left or restriction == right:
      print('você esbarrou a restrição => ', restriction)
      print('\n')
      return False

  for side in [left, right]:
    if ("robber" in side) and len(side) > 1 and ("policeOfficer" not in side):
      print("você esbarrou a retrição => ladrão está sozinho com alguém")
      print('\n')
      return False

  return True

main()