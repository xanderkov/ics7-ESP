from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from copy import deepcopy

from ui.gui import Ui_Start
from task1 import DEFAULT, runExperiment, NORMAL, INTER, BUILDIN


class TaskWindow(QMainWindow):
    def __init__(self):
        super(TaskWindow, self).__init__()
        self.ui = Ui_Start()
        self.ui.setupUi(self)

        self.ui.run.clicked.connect(self.run)

    def run(self):
        params = deepcopy(DEFAULT)
        params['RELY'] = float(self.ui.rely.text().replace(',', '.'))
        params['DATA'] = float(self.ui.data.text().replace(',', '.'))
        params['CPLX'] = float(self.ui.cplx.text().replace(',', '.'))
        params['TIME'] = float(self.ui.time.text().replace(',', '.'))
        params['STOR'] = float(self.ui.stor.text().replace(',', '.'))
        params['VIRT'] = float(self.ui.virt.text().replace(',', '.'))
        params['TURN'] = float(self.ui.turn.text().replace(',', '.'))
        params['ACAP'] = float(self.ui.acap.text().replace(',', '.'))
        params['AEXP'] = float(self.ui.aexp.text().replace(',', '.'))
        params['PCAP'] = float(self.ui.pcap.text().replace(',', '.'))
        params['VEXP'] = float(self.ui.vexp.text().replace(',', '.'))
        params['LEXP'] = float(self.ui.lexp.text().replace(',', '.'))
        params['MODP'] = float(self.ui.modp.text().replace(',', '.'))
        params['TOOL'] = float(self.ui.tool.text().replace(',', '.'))
        params['SCED'] = float(self.ui.sced.text().replace(',', '.'))

        size = float(self.ui.code.text().replace(',', '.'))
        salary = int(self.ui.salary.text())
        variant = NORMAL
        if self.ui.radio_inter.isChecked():
            variant = INTER
        elif self.ui.radio_buildin.isChecked():
            variant = BUILDIN

        res = runExperiment(params, variant, size, salary)

        self.ui.tableWorkTime.setItem(0, 0, QTableWidgetItem(str('{:.3f}'.format(res['laborCosts']))))
        self.ui.tableWorkTime.setItem(0, 1, QTableWidgetItem(str('{:.3f}'.format(res['time']))))
        self.ui.tableWorkTime.setItem(1, 0, QTableWidgetItem(str('{:.3f}'.format(res['planWork']))))
        self.ui.tableWorkTime.setItem(1, 1, QTableWidgetItem(str('{:.3f}'.format(res['planTime']))))

        self.ui.tableLife.setItem(0, 0, QTableWidgetItem(str('{:.3f}'.format(res['planWorkSingle']))))
        self.ui.tableLife.setItem(0, 1, QTableWidgetItem(str('{:.3f}'.format(res['planTimeSingle']))))
        self.ui.tableLife.setItem(0, 2, QTableWidgetItem(str(res['planPeople'])))

        self.ui.tableLife.setItem(1, 0, QTableWidgetItem(str('{:.3f}'.format(res['designWork']))))
        self.ui.tableLife.setItem(1, 1, QTableWidgetItem(str('{:.3f}'.format(res['designTime']))))
        self.ui.tableLife.setItem(1, 2, QTableWidgetItem(str(res['designPeople'])))

        self.ui.tableLife.setItem(2, 0, QTableWidgetItem(str('{:.3f}'.format(res['detailWork']))))
        self.ui.tableLife.setItem(2, 1, QTableWidgetItem(str('{:.3f}'.format(res['detailTime']))))
        self.ui.tableLife.setItem(2, 2, QTableWidgetItem(str(res['detailPeople'])))

        self.ui.tableLife.setItem(3, 0, QTableWidgetItem(str('{:.3f}'.format(res['codingWork']))))
        self.ui.tableLife.setItem(3, 1, QTableWidgetItem(str('{:.3f}'.format(res['codingTime']))))
        self.ui.tableLife.setItem(3, 2, QTableWidgetItem(str(res['codingPeople'])))

        self.ui.tableLife.setItem(4, 0, QTableWidgetItem(str('{:.3f}'.format(res['integWork']))))
        self.ui.tableLife.setItem(4, 1, QTableWidgetItem(str('{:.3f}'.format(res['integTime']))))
        self.ui.tableLife.setItem(4, 2, QTableWidgetItem(str(res['integPeople'])))

        self.ui.tableCOCOMO.setItem(0, 0, QTableWidgetItem(str(res['analysis'])))
        self.ui.tableCOCOMO.setItem(0, 1, QTableWidgetItem(str('{:.3f}'.format(res['anPeople']))))

        self.ui.tableCOCOMO.setItem(1, 0, QTableWidgetItem(str(res['design'])))
        self.ui.tableCOCOMO.setItem(1, 1, QTableWidgetItem(str('{:.3f}'.format(res['dePeople']))))

        self.ui.tableCOCOMO.setItem(2, 0, QTableWidgetItem(str(res['coding'])))
        self.ui.tableCOCOMO.setItem(2, 1, QTableWidgetItem(str('{:.3f}'.format(res['coPeople']))))

        self.ui.tableCOCOMO.setItem(3, 0, QTableWidgetItem(str(res['planning'])))
        self.ui.tableCOCOMO.setItem(3, 1, QTableWidgetItem(str('{:.3f}'.format(res['plPeople']))))

        self.ui.tableCOCOMO.setItem(4, 0, QTableWidgetItem(str(res['ver'])))
        self.ui.tableCOCOMO.setItem(4, 1, QTableWidgetItem(str('{:.3f}'.format(res['verPeople']))))

        self.ui.tableCOCOMO.setItem(5, 0, QTableWidgetItem(str(res['office'])))
        self.ui.tableCOCOMO.setItem(5, 1, QTableWidgetItem(str('{:.3f}'.format(res['ofPeople']))))

        self.ui.tableCOCOMO.setItem(6, 0, QTableWidgetItem(str(res['quality'])))
        self.ui.tableCOCOMO.setItem(6, 1, QTableWidgetItem(str('{:.3f}'.format(res['quPeople']))))

        self.ui.tableCOCOMO.setItem(7, 0, QTableWidgetItem(str(res['manuals'])))
        self.ui.tableCOCOMO.setItem(7, 1, QTableWidgetItem(str('{:.3f}'.format(res['maPeople']))))

        self.ui.budget.setText(str('{:.3f}'.format(res['budget'])))