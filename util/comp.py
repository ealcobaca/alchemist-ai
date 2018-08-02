import re
import numpy as np

def compounddic2atomsfraction(compounds):

    def createNewDic(dic, multiplyby):
        values = list(dic.values())
        keys = dic.keys()
        newValues = np.array(values)*multiplyby
        newDic = dict(zip(keys, newValues))
        return newDic

    def composition2atoms(cstr):
        lst = re.findall(r'([A-Z][a-z]?)(\d*\.?\d*)', cstr)
        dic = {}
        for i in lst:
            if len(i[1]) > 0:
                try:
                    dic[i[0]] = int(i[1])
                except ValueError:
                    dic[i[0]] = float(i[1])
            else:
                dic[i[0]] = 1
        return dic

    dic = {}

    for key in compounds.keys():
        baseValue = compounds[key]
        atoms = composition2atoms(key)
        for a in atoms.keys():
            dic[a] = dic.get(a, 0) + atoms[a]*baseValue

    multiplyby = 1/np.sum(list(dic.values()))
    atomsF = createNewDic(dic, multiplyby)

    return atomsF


###############################################################################
#                                   Exemplo                                   #
###############################################################################

AvailableCompounds = ['Ag2O', 'Al2O3', 'As2O3', 'As2O5', 'B2O3', 'BaO',
                      'Bi2O3', 'CaO', 'CdO', 'Ce2O3', 'CeO2', 'Cl', 'Cs2O',
                      'Cu2O', 'CuO', 'Er2O3', 'F', 'Fe2O3', 'Fe3O4', 'FeO',
                      'Ga2O3', 'Gd2O3', 'GeO', 'GeO2', 'I', 'K2O', 'La2O3',
                      'Li2O', 'MgO', 'Mn2O3', 'Mn2O7', 'Mn3O4', 'MnO', 'MnO2',
                      'Mo2O3', 'Mo2O5', 'MoO', 'MoO2', 'MoO3', 'N', 'N2O5',
                      'NO2', 'Na2O', 'Nb2O3', 'Nb2O5', 'P2O3', 'P2O5', 'Pb3O4',
                      'PbO', 'PbO2', 'SO2', 'SO3', 'Sb2O3', 'Sb2O5', 'SbO2',
                      'SiO', 'SiO2', 'Sn2O3', 'SnO', 'SnO2', 'SrO', 'Ta2O3',
                      'Ta2O5', 'TeO2', 'TeO3', 'Ti2O3', 'TiO', 'TiO2', 'V2O3',
                      'V2O5', 'VO2', 'VO6', 'WO3', 'Y2O3', 'Yb2O3', 'ZnO',
                      'ZrO2']

# isto é o que o usuário pode dar de input, qualquer quantidade (numeros reais
# positivos) de um ou mais dos compostos da lista AvailableCompounds:

compostoDic = {
    'Al2O3': 1,
    'SiO': 0
}

atomDic = compounddic2atomsfraction(compostoDic)

print(atomDic)

# Do dicionário atomDic você tem os valores de fração atômica de cada átomo para por na rede

#ompound2atomfraction.py
#Exibindo compound2atomfraction.py.