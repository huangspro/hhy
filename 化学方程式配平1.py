import re
import string
from sympy import solve, symbols
def h(a):
    m=[]
    while a[0] in "1234567890":
          m.append(a[0])
          a=a.replace(a[0],'',1)
    c=''.join(m)
    b=a.replace('2','₂').replace('3','₃').replace('4','₄').replace('5','₅').replace('6','₆').replace('7','₇').replace('8','₈').replace('9','₉').replace('10','¹₁₀').replace('11','₁₁').replace('12','₁₂').replace('13','₁₃')
    return(c+b)

def n(a):
    m1=[]
    m2=[]
    k,l=a.split('=')[0],a.split('=')[1]
    u=k.split('+')
    for o in u:
        m1.append(h(o))
    h1='+'.join(m1)
    u1=l.split('+')
    for o1 in u1:
        m2.append(h(o1))
    h2='+'.join(m2)
    print(h1+'='+h2)
while True:
      a=input('请输入化学方程式')
      ChemicalEquationsList = [a]
      

      ELEMENT = re.compile(R'([A-Z][a-z]?|<(?:\d|{[A-Za-z0-9+-]})?e[+-]>)')


      def max_gys(num1, num2):  # 两个数最大公约数
          while num2:
              temp = num1 % num2
              num1, num2 = num2, temp
          return num1


      def min_gbs(num1, num2):  # 两个数最小公倍数
          return num1 * num2 // max_gys(num1, num2)


# 将二层列表中的内容转成一层列表
      get_all = lambda _, __ = eval("[]"): __.clear() or [[__.append(____) for ____ in ___ if ____] for ___ in _] and __


      def handle_double_elements_list_scale(element1, element2, chemicals, scale_group):  # 同步两个元素组中相同的元素
          shared = list(set(chemicals[element1]) & set(chemicals[element2]))
          if shared:
              multiply = min_gbs(scale_group[element1][shared[0]], scale_group[element2][shared[0]])
              shared1 = scale_group[element1][shared[0]]
              for item in scale_group[element1]:
                  scale_group[element1][item] *= (multiply // shared1)
              shared2 = scale_group[element2][shared[0]]
              for item in scale_group[element2]:
                  scale_group[element2][item] *= (multiply // shared2)
          return element2


      def calc_equations(left_item_list, right_item_list):
          elements = list(set(get_all([ELEMENT.findall(item) for item in left_item_list if item not in list('+-')])))
          right_elements = list(set(get_all([ELEMENT.findall(item) for item in right_item_list if item not in list('+-')])))
          assert set(elements) == set(right_elements), '化学方程式两方元素不守恒！'
          symbols_list = symbols([item for item in (left_item_list + right_item_list) if item not in list('+-')], positive=True, integer=True, real=True)  # 为每个化学物质创建元素符号
          for symbol in symbols_list:
              globals()[str(symbol)] = symbol  # 将符号变量释放到全局，为下文eval()字符串转变量算式做基础
          scale_group = {element: {} for element in elements}
          left_item_dict = {item: {} for item in left_item_list if item not in list('+-')}
          right_item_dict = {item: {} for item in right_item_list if item not in list('+-')}
          for item_list, item_dict in ((left_item_list, left_item_dict), (right_item_list, right_item_dict)):
              for item in item_list:
                  if item not in list('+-'):
                      for element in re.compile(R'([A-Z][a-z]?)(\d*)').findall(item):
                          if element[0] not in item_dict[item]:
                              item_dict[item][element[0]] = 0
                          item_dict[item][element[0]] += element[1].isdigit() and int(element[1]) or 1
          for element in elements:
              for item_dict in (left_item_dict, right_item_dict):
                  for item in item_dict:
                      if element in item:
                          scale_group[element][item] = item_dict[item][element]
          solve_list = []
          for element in elements:
              temp_str = ''
              temp = []
              for item in left_item_dict:
                  index = scale_group[element].get(str(item), "")
                  if index:
                      temp.append(f'{index}*{str(item)}')
              temp_str += '+'.join(temp)
              temp = []
              for item in right_item_dict:
                  index = scale_group[element].get(str(item), "")
                  if index:
                      temp.append(f'{index}*{str(item)}')
              if temp:
                 temp_str += '-' + '-'.join(temp)
              solve_list.append(eval(temp_str))
          res = solve(solve_list, symbols_list)
          can_zhao = [item for item in symbols_list if str(item) == list(set(list(left_item_dict.keys()) + list(right_item_dict.keys())) - set(list(map(str, res.keys()))))[0]][0]
          for item in res:
              res[item] /= can_zhao
          res[can_zhao] = 1
          fen_mu = re.compile(R'/(\d+)?').findall(str(res))
          if fen_mu:
              bs = int(fen_mu[0])
              for item in res:
                  res[item] *= bs
          chemical_equations = []
          for item_dict in (left_item_dict, right_item_dict):
              all_item = []
              all_index = []
              for item in item_dict:
                  all_item.append(item)
                  all_index.append(res[[i for i in symbols_list if str(i) == item][0]])
              chemical_equations.append(' + '.join([f'{"" if all_index[i] == 1 else all_index[i]}{all_item[i]}' for i in range(len(item_dict))]))
          chemical_equations = ' = '.join(chemical_equations)
          return chemical_equations


      for ChemicalEquations in ChemicalEquationsList:
          for space in string.whitespace:
              ChemicalEquations = ChemicalEquations.replace(space, '')
          if '=' not in ChemicalEquations and ';' in ChemicalEquations:
              all_items = ChemicalEquations.split(';')
              pass  # 自动化合价计算等式先不做，先做元素配平
          elif 'e+>' in ChemicalEquations or 'e->' in ChemicalEquations or '{' in ChemicalEquations or '.' in ChemicalEquations:
              pass  # 暂时不搞电子<e+>/<e->和含./{n}的化学物质等的运算
          else:
              left, right = ChemicalEquations.split('=')
              items = re.compile(R'[+-]?(<(?:\d+|{[A-Za-z0-9+-]+})?e[+-]>|(?:(?:\(?(?:[A-Z][a-z]?\.?)+(?:\d+|{[A-Za-z0-9+-]+})?\)?)+(?:<(?:\d+|{[A-Za-z0-9+-]+})?e[+-]>)?)+)(?:\([gls]\))?([+-]?)')
              left_items, right_items = items.findall(left), items.findall(right)
              r=calc_equations(list(get_all(left_items)), list(get_all(right_items)))
              print(n(r.replace(' ',"")))