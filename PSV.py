# pyside6 사용에 필요한 모듈
import sys
import re
from datetime import datetime

# PySide6 모듈을 효율적으로 import
from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QTableWidgetItem,
    QVBoxLayout, QDockWidget, QWidget, QHBoxLayout, QPushButton
)
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView

from ui_PSV import Ui_MainWindow


# ------------------------------------------------
# 메인 윈도우 클래스 정의
# ------------------------------------------------


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("AstroPSV")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.textBrowser_2.setText(f"[{now}] 프로그램이 시작되었습니다.")
        
        self.pushButton.clicked.connect(self.PSV_output)
        self.pushButton_3.clicked.connect(self.PSV_Save)
        self.pushButton_4.clicked.connect(self.Menual_PDF_Open)
        self.pushButton_5.clicked.connect(self.PSV_Open)

        # 체크박스 상태에 따라 lineEdit_7 활성/비활성 및 변수 저장
        self.checkBox.stateChanged.connect(self.handle_checkbox_state)
        self.MPC_Code = self.lineEdit_7.text()  # 초기값

        # spinBox 값이 바뀔 때마다 tableWidget의 row 개수를 spinBox 값으로 설정
        self.spinBox.valueChanged.connect(self.update_table_rows)

        # lineEdit의 값이 변경될 때마다 변수에 저장
        self.lineEdit.textChanged.connect(self.save_lineedit1_value)
        # lineEdit의 초기값을 변수에 저장
        self.lineedit1_value = self.lineEdit.text()

        # lineEdit_2의 값이 변경될 때마다 변수에 저장
        self.lineEdit_2.textChanged.connect(self.save_lineedit2_value)
        # lineEdit_2의 초기값을 변수에 저장
        self.lineedit2_value = self.lineEdit_2.text()

        # lineEdit_3의 값이 변경될 때마다 변수에 저장
        self.lineEdit_3.textChanged.connect(self.save_lineedit3_value)
        # lineEdit_3의 초기값을 변수에 저장
        self.lineedit3_value = self.lineEdit_3.text()

        # lineEdit_4의 값이 변경될 때마다 변수에 저장
        self.lineEdit_4.textChanged.connect(self.save_lineedit4_value)
        # lineEdit_4의 초기값을 변수에 저장
        self.lineedit4_value = self.lineEdit_4.text()

        # lineEdit_5의 값이 변경될 때마다 변수에 저장
        self.lineEdit_5.textChanged.connect(self.save_lineedit5_value)
        # lineEdit_5의 초기값을 변수에 저장
        self.lineedit5_value = self.lineEdit_5.text()

        # lineEdit_6의 값이 변경될 때마다 변수에 저장
        self.lineEdit_6.textChanged.connect(self.save_lineedit6_value)
        # lineEdit_6의 초기값을 변수에 저장
        self.lineedit6_value = self.lineEdit_6.text()

        # comboBox에서 CCD/CMOS 선택 시 변수에 저장
        self.comboBox.currentTextChanged.connect(self.save_sensor_type)
        self.sensor_type = self.comboBox.currentText()
        if self.sensor_type == "CCD":
            self.sensor_type = "CCD"
        elif self.sensor_type == "CMOS":
            self.sensor_type = "CMO"
        else:
            self.sensor_type = ""

        # comboBox_2에서 밴드 타입 선택 시 변수에 저장
        self.comboBox_2.currentTextChanged.connect(self.save_band_type)
        self.band_type = self.comboBox_2.currentText()
        if self.band_type == "U":
            self.band_type = "U"
        elif self.band_type == "B":
            self.band_type = "B"
        elif self.band_type == "G":
            self.band_type = "G"
        elif self.band_type == "V":
            self.band_type = "V"
        elif self.band_type == "R":
            self.band_type = "R"
        elif self.band_type == "I":
            self.band_type = "I"
        else:
            self.band_type = ""

    def save_sensor_type(self, text):
        if text == "CCD":
            self.sensor_type = "CCD"
        elif text == "CMOS":
            self.sensor_type = "CMO"
        else:
            self.sensor_type = ""

    def save_band_type(self, text):
        if text == "U":
            self.band_type = "U"
        elif text == "B":
            self.band_type = "B"
        elif text == "G":
            self.band_type = "G"
        elif text == "V":
            self.band_type = "V"
        elif text == "R":
            self.band_type = "R"
        elif text == "I":
            self.band_type = "I"
        else:
            self.band_type = ""

    def handle_checkbox_state(self, state):
        if state:  # 체크됨
            self.lineEdit_7.setReadOnly(True)
            self.MPC_Code = "XXX"
            self.lineEdit_7.setText(self.MPC_Code)
        else:
            self.lineEdit_7.setReadOnly(False)
            self.MPC_Code = self.lineEdit_7.text()

    def save_lineedit1_value(self, text): # 망원경 구경
        self.lineedit1_value = text

    def save_lineedit2_value(self, text): # 망원경 종류
        self.lineedit2_value = text

    def save_lineedit3_value(self, text): # 위도
        self.lineedit3_value = text

    def save_lineedit4_value(self, text): # 경도
        self.lineedit4_value = text

    def save_lineedit5_value(self, text): # 고도
        self.lineedit5_value = text

    def save_lineedit6_value(self, text): # 관측자 이름
        self.lineedit6_value = text

    def update_table_rows(self, value):
        self.tableWidget.setRowCount(value)

    def PSV_output(self):
        # PSV 기본 형태를 변수 값으로 채워서 메모리에 저장
        # PSV 헤더 및 메타데이터 작성
        psv_lines = [
            "# version=2017",
            "# observatory",
            f"! mpcCode {self.lineEdit_7.text()}",
            "# submitter",
            f"! name {self.lineedit6_value}",
            "# telescope",
            f"! aperture {self.lineedit1_value}",
            f"! design {self.lineedit2_value}",
            f"! detector {self.sensor_type}",
            "# observers",
            f"! name {self.lineedit6_value}",
            "# measurers",
            f"! name {self.lineedit6_value}",
            "# comment",
            f"! line Long. {self.lineedit4_value}, Lat. {self.lineedit3_value}, Alt. {self.lineedit5_value}m, Google Earth",
            "permID |mode|stn |obsTime                 |ra         |dec        |astCat|mag  |band|remarks"
        ]

        # 각 행을 PSV 형식으로 변환 (필드 매핑 및 고정값 적용)
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            # 각 열에서 필요한 값 추출
            permID   = self.tableWidget.item(row, 0).text() if self.tableWidget.item(row, 0) else ""
            obsTimei = self.tableWidget.item(row, 1)
            obsTime  = obsTimei.text() + "Z" if obsTimei and obsTimei.text() else ""
            ra       = self.tableWidget.item(row, 2).text() if self.tableWidget.item(row, 2) else ""
            dec      = self.tableWidget.item(row, 3).text() if self.tableWidget.item(row, 3) else ""
            mag      = self.tableWidget.item(row, 4).text() if self.tableWidget.item(row, 4) else ""
            mode     = self.sensor_type
            band     = self.band_type
            stn      = self.lineEdit_7.text() if self.lineEdit_7.text() else "XXX"
            astCat   = "USNOB1"
            
            remarks  = ""

            # 고정 폭 필드 지정
            fields = [
            permID.rjust(7),
            mode.rjust(4),
            stn.ljust(4),
            obsTime.ljust(24),
            ra.ljust(11),
            dec.ljust(11),
            astCat.ljust(6),
            mag.ljust(5),
            band.rjust(4),
            remarks
            ]
            psv_line = "|".join(fields)
            psv_lines.append(psv_line)

        self.psv_content = "\n".join(psv_lines)

        # 고정폭 글꼴 적용 (윈도우, 맥 모두 호환되는 글꼴로 설정)
        font_family = "Consolas" if sys.platform.startswith("win") else "Menlo"
        self.textBrowser.setFontFamily(font_family)
        self.textBrowser.setFontPointSize(11)
        self.textBrowser.setText(self.psv_content)

        # tabWidget에서 tab_4 창을 띄움
        self.tabWidget.setCurrentWidget(self.tab_4)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.textBrowser_2.append(f"[{now}] 입력된 데이터를 PSV 형식으로 변환하였습니다.")


    def PSV_Save(self):
        # PSV 내용을 .psv 파일로 저장
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "PSV 파일 저장",
            "",
            "PSV Files (*.psv);;All Files (*)",
            options=options
        )
        if file_path:
            # 확장자가 .psv가 아니면 추가
            if not file_path.lower().endswith(".psv"):
                file_path += ".psv"
            # textBrowser의 텍스트를 UTF-8로 저장
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.textBrowser.toPlainText())

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.textBrowser_2.append(f"[{now}] PSV 파일을 저장하였습니다: {file_path}")


    def Menual_PDF_Open(self):
        # PDF 파일 선택
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "PDF 설명서 열기",
            "",
            "PDF Files (*.pdf);;All Files (*)",
            options=options
        )
        if file_path:
            # QDockWidget을 사용하여 PDF를 본 창에 도킹
            dock = QDockWidget("PDF 설명서", self)
            dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea)
            pdf_view = QPdfView(dock)
            # QPdfDocument의 parent를 dock으로 명확히 지정
            pdf_doc = QPdfDocument(dock)
            pdf_doc.load(file_path)
            pdf_view.setDocument(pdf_doc)

            # 도킹 위젯의 초기 크기를 명시적으로 지정
            dock.resize(700, 600)

            # 도킹 위젯을 플로팅 상태로 띄움 (메인 윈도우에 붙지 않음)
            dock.setFloating(True)
            dock.show()

            # 확대/축소 + 페이지 이동 버튼 추가
            controls = QWidget(dock)
            layout = QHBoxLayout(controls)
            btn_prev = QPushButton("이전 페이지", controls)
            btn_next = QPushButton("다음 페이지", controls)
            btn_zoom_in = QPushButton("확대", controls)
            btn_zoom_out = QPushButton("축소", controls)
            layout.addWidget(btn_prev)
            layout.addWidget(btn_next)
            layout.addWidget(btn_zoom_in)
            layout.addWidget(btn_zoom_out)
            layout.addStretch()
            controls.setLayout(layout)

            # 도킹 위젯의 메인 위젯(pdf_view)와 컨트롤을 수직으로 배치
            container = QWidget(dock)
            vlayout = QVBoxLayout(container)
            vlayout.setContentsMargins(0, 0, 0, 0)
            vlayout.addWidget(controls)
            vlayout.addWidget(pdf_view)
            container.setLayout(vlayout)
            dock.setWidget(container)

            # 페이지 이동 기능 구현
            def goto_prev():
                current = pdf_view.pageNavigator().currentPage()
                if current > 0:
                    pdf_view.pageNavigator().jump(current - 1, QPointF(0, 0))

            def goto_next():
                current = pdf_view.pageNavigator().currentPage()
                if current < pdf_doc.pageCount() - 1:
                    pdf_view.pageNavigator().jump(current + 1, QPointF(0, 0))

            btn_prev.clicked.connect(goto_prev)
            btn_next.clicked.connect(goto_next)

            def zoom_in():
                scale = pdf_view.zoomFactor()
                pdf_view.setZoomFactor(scale * 1.2)

            def zoom_out():
                scale = pdf_view.zoomFactor()
                pdf_view.setZoomFactor(scale / 1.2)

            btn_zoom_in.clicked.connect(zoom_in)
            btn_zoom_out.clicked.connect(zoom_out)

            # dock이 GC로 사라지지 않도록 참조 유지
            if not hasattr(self, "_pdf_docks"):
                self._pdf_docks = []
            self._pdf_docks.append(dock)
    

    def PSV_Open(self):
        # PSV 파일을 열어서 textBrowser에 표시하고, 메타데이터를 lineEdit 등에 복원
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "PSV 파일 열기",
            "",
            "PSV Files (*.psv);;All Files (*)",
            options=options
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 고정폭 글꼴 적용 (윈도우, 맥 모두 호환)
            font_family = "Consolas" if sys.platform.startswith("win") else "Menlo"
            self.textBrowser.setFontFamily(font_family)
            self.textBrowser.setFontPointSize(11)
            self.textBrowser.setText(content)

            # tabWidget에서 tab_4 창을 띄움
            self.tabWidget.setCurrentWidget(self.tab_4)

            # PSV 헤더에서 메타데이터 추출
            lines = content.splitlines()
            for line in lines:
                if line.startswith("! aperture "):
                    self.lineEdit.setText(line.replace("! aperture ", "").strip())
                elif line.startswith("! design "):
                    self.lineEdit_2.setText(line.replace("! design ", "").strip())
                elif line.startswith("! name "):
                    # 관측자 이름은 여러 곳에 있으나, 첫 번째만 사용
                    if not self.lineEdit_6.text():
                        self.lineEdit_6.setText(line.replace("! name ", "").strip())
                elif line.startswith("! line Long."):
                    # 예: ! line Long. 127 02 09.5 E, Lat. 36 00 50.4 N, Alt. 67m, Google Earth
                    m = re.search(
                        r"Long\.\s*([\d\s.+-]+[EW]),\s*Lat\.\s*([\d\s.+-]+[NS]),\s*Alt\.\s*([\d.+-]+)m",
                        line
                    )
                    if m:
                        self.lineEdit_4.setText(m.group(1).strip())  # 경도 (예: 127 02 09.5 E)
                        self.lineEdit_3.setText(m.group(2).strip())  # 위도 (예: 36 00 50.4 N)
                        self.lineEdit_5.setText(m.group(3).strip())  # 고도 (예: 67)
            # 센서 타입 복원
            for line in lines:
                if line.startswith("! detector "):
                    sensor = line.replace("! detector ", "").strip()
                    # PSV 파일에서는 CMOS가 "CMO"로 저장되어 있으므로 변환
                    if sensor == "CMO":
                        sensor = "CMOS"
                    idx = self.comboBox.findText(sensor)
                    if idx != -1:
                        self.comboBox.setCurrentIndex(idx)

            # 밴드 타입 복원
            # 데이터 라인에서 첫 번째 band 값만 추출
            for line in lines:
                if "|" in line:
                    fields = [f.strip() for f in line.split("|")]
                    if len(fields) >= 9:
                        band = fields[8]
                        idx = self.comboBox_2.findText(band)
                        if idx != -1:
                            self.comboBox_2.setCurrentIndex(idx)
                            break  # 첫 데이터 라인만 사용
            
            # 관측소 코드 복원
            # 관측소 코드 복원 (체크박스와 lineEdit_7의 상태를 일시적으로 조정)
            for line in lines:
                if line.startswith("! mpcCode "):
                    mpc_code = line.replace("! mpcCode ", "").strip()
                    # 체크박스와 lineEdit_7의 시그널 일시적으로 차단
                    self.checkBox.blockSignals(True)
                    self.lineEdit_7.blockSignals(True)
                    if mpc_code == "XXX":
                        self.checkBox.setChecked(True)
                        self.lineEdit_7.setReadOnly(True)
                        self.lineEdit_7.setText(mpc_code)
                    else:
                        self.checkBox.setChecked(False)
                        self.lineEdit_7.setReadOnly(False)
                        self.lineEdit_7.setText(mpc_code)
                    self.checkBox.blockSignals(False)
                    self.lineEdit_7.blockSignals(False)
                    # "XXX"일 때는 handle_checkbox_state에서 텍스트가 자동으로 들어감
                    if mpc_code != "XXX":
                        self.lineEdit_7.setText(mpc_code)
                    break
            
            # 망원경 종류 복원 (이미 위에서 처리)
            # 기타 값들은 이미 위에서 처리됨

            # 테이블 데이터 복원
            # 데이터 라인 찾기 (헤더 이후)
            data_started = False
            data_lines = []
            for line in lines:
                if line.strip().startswith("permID"):
                    data_started = True
                    continue
                if data_started:
                    if line.strip() == "" or line.strip().startswith("#"):
                        continue
                    data_lines.append(line)
            self.spinBox.setValue(len(data_lines))
            self.tableWidget.setRowCount(len(data_lines))
            for row_idx, data_line in enumerate(data_lines):
                # PSV 데이터는 |로 구분, 고정폭 필드이므로 strip 후 split
                fields = [f.strip() for f in data_line.split("|")]
                # 필드: permID, mode, stn, obsTime, ra, dec, astCat, mag, band, remarks
                # 테이블에는 permID, obsTime, ra, dec, mag (0~4열)만 복원
                if len(fields) >= 9:
                    self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(fields[0]))
                    # obsTime에서 끝의 'Z' 제거
                    obs_time = fields[3]
                    if obs_time.endswith("Z"):
                        obs_time = obs_time[:-1]
                    self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(obs_time.strip()))
                    self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(fields[4]))
                    self.tableWidget.setItem(row_idx, 3, QTableWidgetItem(fields[5]))
                    self.tableWidget.setItem(row_idx, 4, QTableWidgetItem(fields[7]))

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.textBrowser_2.append(f"[{now}] PSV 파일을 열었습니다: {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()